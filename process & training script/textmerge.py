"""
filepath = []

for i in range(14):
    filepath.append(f"./hitler_text/process/{i}.txt")

filepath.append("./hitler_text/process/Hitlers_Second_Book.txt")
filepath.append("./hitler_text/process/Hitlers_table_talk.txt")
filepath.append("./hitler_text/process/meinkampf.txt")

ctext = ""
j = 0
for fp in filepath:
    with open(fp, "r", encoding="utf-8") as file:
        j+=1
        text = file.read()
        if j!=1:
            text = " " + text
        ctext += text

#print(combined_text)

with open("./hitler_text/process/totaltext.txt", "w", encoding="utf-8") as file:
    file.write(ctext)
"""

"""
import re
#print(combined_text)
ctext = ""
with open("./hitler_text/process/totaltext.txt", "r", encoding="utf-8") as file:
    ctext = file.read()

#ctext.replace()
text = ctext
#text = re.sub(r'"(\S)', r'"\1', ctext)
#text = re.sub(r'([.?!])(?![\s"]|$)', r'\1 {}'.format("<|endoftext|>"), text)
#text = re.sub(r'\s+([.?!])', r'\1 {}'.format("<|endoftext|>"), text)
#text = re.sub(r'(?<=\S)\s+(?=[.?!"]|$)', "<|endoftext|>", text)
replacement_text = "<|endoftext|>"
text = re.sub(r'(\.)([A-Z])', r'.\1 \2', text)
text = re.sub(r'(\?)([A-Z])', r'.\1 \2', text)
text = re.sub(r'(!)([A-Z])', r'.\1 \2', text)

text = re.sub(r'\.(")([A-Z])', r'.\1 \2', text)
text = re.sub(r'!(")([A-Z])', r'.\1 \2', text)
text = re.sub(r'\?(")([A-Z])', r'.\1 \2', text)

#- eos 마킹 전에 번호 파트는 예외처리 되어야 한다. - 어차피 14까지만 있으니 손으로 처리하자 

text = text.replace('. ', '.{}'.format(replacement_text))
text = text.replace('. ', '.{}'.format(replacement_text))
text = text.replace('! ', '!{}'.format(replacement_text))
text = text.replace('? ', '?{}'.format(replacement_text))

pattern = r'(\."\s*)([A-Z])'
text = re.sub(r'(\.")(\s*)([A-Z])', r'\1{}\3'.format(replacement_text), text)
text = re.sub(r'(!")(\s*)([A-Z])', r'\1{}\3'.format(replacement_text), text)
text = re.sub(r'(\?")(\s*)([A-Z])', r'\1{}\3'.format(replacement_text), text)

#text = text.replace('.\" ', '.\"{}'.format(replacement_text))
#text = text.replace('!\" ', '.\"{}'.format(replacement_text))
#text = text.replace('?\" ', '.\"{}'.format(replacement_text))

text = re.sub(pattern, r'\1{}\2'.format(replacement_text), text)

#text = text.replace('. ', '.{}'.format(replacement_text))
#text = text.replace('. ', '.{}'.format(replacement_text))
text = text.replace('<|endoftext|><|endoftext|>', '<|endoftext|>')


with open("./hitler_text/process/totalp.txt", "w", encoding="utf-8") as file:
    file.write(text)
"""


ctext = ""
lines1 = []
with open(f"./hitler_text/process/totalp.txt", 'r', encoding="utf-8") as file1:
    ctext = file1.read()

lines1 = ctext.split("<|endoftext|>")


for i in range(len(lines1)):
    lines1[i] = lines1[i].replace('"', '\\"')

    fstr = f"{lines1[i]}<|endoftext|>"
    mtxt = '{"text":"' + fstr + '"}'

    with open('./hitler_text/process/totalf.txt', 'ab') as file:
        file.write((mtxt).encode('utf-8'))
        file.write(b'\n')


#f"### 질문: {x['instruction']}\n\n### 답변: {x['output']}<|endoftext|>"
# f"###QST: {x['instruction']}\n\n###ANS: {x['output']}<|endoftext|>"