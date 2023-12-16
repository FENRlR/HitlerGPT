# -*- coding: utf-8 -*-
import locale
locale.getpreferredencoding = lambda: "UTF-8"


outfolder = "model"

newtrain = 1 
checkpoint = 360000 
resumep = f"./{outfolder}/checkpoint-{checkpoint}"

from datasets import load_dataset
data = load_dataset('json', data_files='hitlerbook.json')
#data = load_dataset('json', data_files='tqna.json')

maxse = 2*int(data.num_rows.get('train')) 


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_id = "EleutherAI/pythia-410m-deduped"
#model_id = "EleutherAI/pythia-160m-deduped"
#model_id = "EleutherAI/pythia-70m-deduped"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})


data = data.map(lambda samples: tokenizer(samples["text"]), batched=True)

from peft import prepare_model_for_kbit_training

model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

def print_trainable_parameters(model):
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainable%: {100 * trainable_params / all_param}"
    )

from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["query_key_value"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)
print_trainable_parameters(model)


import transformers

# needed for gpt-neo-x tokenizer
tokenizer.pad_token = tokenizer.eos_token

trainer = transformers.Trainer(
    model=model,
    train_dataset=data["train"],
    args=transformers.TrainingArguments(
        save_strategy="epoch", 
        #save_strategy="steps",  
        #save_steps= saveinterval,
        per_device_train_batch_size=2,
        gradient_accumulation_steps=1,
        # warmup_steps=200,
        max_steps=maxse,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=10,
        output_dir=outfolder,
        #optim="paged_adamw_8bit"
    ),
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False

if newtrain == 1:
    trainer.train()
elif newtrain == 0:
    trainer.train(resume_from_checkpoint=resumep)

model.save_pretrained(f"./{outfolder}")


model.eval()
model.config.use_cache = True


#- export
from huggingface_hub import login
hf_token = ""
repository = "https://huggingface.co/FENRlR/HitlerGPT"
login(token=hf_token)
model.push_to_hub(repository)