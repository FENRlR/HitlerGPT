import re

def replace_numbering(text):
    pattern = r'\(\d+\)'
    matches = re.findall(pattern, text)
    for i, match in enumerate(matches):
        number = str(i + 1)
        text = text.replace(match, ' '+number + '.')

    return text

def textcleanse(input_file, output_file):
    with open(input_file, 'r', encoding="utf-8") as file:
        text = file.read()

    text = replace_numbering(text)

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

    """   
    #- 히틀러 커피톡 전용
    text = re.sub(r'(\d{2,}\s[A-Z]{4,}.+?$)', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'([A-Z]{4,}\s\d{2,}.+?$)', ' ', text, flags=re.MULTILINE)
    """

    #"""
    # ... 제거
    # text = text.replace('....', '.')
    #text = text.replace('...', '')

    text = text.replace('- \n', '')

    text = text.replace('-\n', '')

    #text = text.replace('\n', '')
    text = text.replace('\n', ' ')

    text = re.sub(' +', ' ', text)

    text = re.sub(r'\s*([!?;.,])', r'\1', text)
    
    #모든 느낌표가 한칸 띄워져있으니 그 부분도 수정할것
    #text = re.sub('([.?!])', r'\1 ', text)
    text = re.sub(r'(?<=[^.!?])$', ' ', text)
    #"""


    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(text)



#"""
# "./hitler_text/process/meinkampf.txt"
#input = "./hitler_text/meinkampf.txt"
input = "./hitler_text/Hitlers_Second_Book.txt"
output = './hitler_text/process/Hitlers_Second_Book.txt'
textcleanse(input, output)
#"""
