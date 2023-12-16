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

#"""
import re
#print(combined_text)
ctext = ""
with open("./hitler_text/Mein Kampf.txt", "r", encoding="utf-8") as file:
    ctext = file.read()

#ctext.replace()
text = ctext

for i in range(14):
    text = text.replace(f'({i+1})', f'{i+1}.')

while True:
    start_index = text.find('(')
    if start_index == -1:
        break
    end_index = text.find(')', start_index)
    if end_index == -1:
        break
    text = text[:start_index] + text[end_index + 1:]

while True:
    start_index = text.find('[')
    if start_index == -1:
        break
    end_index = text.find(']', start_index)
    if end_index == -1:
        break
    text = text[:start_index] + text[end_index + 1:]

while True:
    start_index = text.find('{')
    if start_index == -1:
        break
    end_index = text.find('}', start_index)
    if end_index == -1:
        break
    text = text[:start_index] + text[end_index + 1:]

text = text.replace('\n\n', '\n')
text = text.replace('\n', ' ')
text = text.replace('   ', ' ')
text = text.replace('  ', ' ')

#text = re.sub(r'"(\S)', r'"\1', ctext)


#text = text.replace('.\" ', '.\"{}'.format(replacement_text))
#text = text.replace('!\" ', '.\"{}'.format(replacement_text))
#text = text.replace('?\" ', '.\"{}'.format(replacement_text))


#text = re.sub(pattern, r'\1{}\2'.format(replacement_text), text)

#text = text.replace('. ', '.{}'.format(replacement_text))
#text = text.replace('. ', '.{}'.format(replacement_text))
#text = text.replace('<|endoftext|><|endoftext|>', '<|endoftext|>')

with open("./hitler_text/meinkampf.txt", "w", encoding="utf-8") as file:
    file.write(text)
#"""

