import PyPDF2
import re


# ./hitler_text/Kaltenborn-InterviewHitlerAugust-1967.pdf
# ./hitler_text/meinkampf.pdf
# ./hitler_text/Hitlers_table_talk.pdf
with open('./hitler_text/Hitlers_table_talk.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    num_pages = len(reader.pages)
    #print(num_pages)

    start_number = 2
    for page in range(46,766): #766
        #text = reader.pages[page].extract_text()#.split("\n")
        text = reader.pages[page].extract_text().split("\n")
        extext = ""
        if len(text)>5:
            #print(text[0])
            #print(text[1])
            if page != 206:
                text[0] = ""
                extext = "\n".join(text)
            if page == 642:
                text[0] = ""
                text[1] = ""
                text[2] = ""
                text[3] = ""
                extext = "\n".join(text)
            else:
                extext = "\n".join(text)
            # 67, 138페이지도 예외대상



        """
        start_index = text.find(str(start_number))
        if start_index == -1:
            return text

        dot_index = text.find('.', start_index)
        if dot_index == -1:
            return text

        processed_text = text[:start_index] + text[dot_index + 1:]
        """


        if page>46 and len(extext)>50:
            while page<766:
                pattern = r'\b{}\s+[a-zA-Z0-9]'.format(start_number)
                if start_number == 11:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("II")
                elif start_number == 32:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format(33)
                elif page == 203 or page == 204 or page == 205:
                    break
                elif start_number == 100:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("loo")
                elif start_number == 101:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("IOI")
                elif start_number == 110:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("no")
                elif start_number == 111:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("ill")
                elif start_number == 116:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("Il6")
                elif start_number == 118:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("It8")
                elif start_number == 120:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("12O")
                elif start_number == 132:
                    start_number += 1
                    break
                elif start_number == 142:
                    start_number += 1
                    break
                elif start_number == 181:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("181 ,")
                elif start_number == 200:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2OO")
                elif start_number == 201:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2OI")
                elif start_number == 202:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2O2")
                elif start_number == 210:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2IO")
                elif start_number == 216:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2l6")
                elif start_number == 218:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2l8")
                elif start_number == 221:
                    start_number = 227
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format(start_number)
                elif start_number == 261:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format(201)
                elif start_number == 262:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format(202)
                elif start_number == 271 and page==642:
                    start_number += 1
                    break
                elif start_number == 292:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("2§2")
                elif start_number == 318:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("3l8")
                elif start_number == 327:
                    pattern = r'\b{}\s+[a-zA-Z0-9]'.format("3557") # 아 제발


                match = re.search(pattern, extext)
                if match:
                    print(f"found - page{page + 1} - {start_number}")
                    start_index = match.start()
                    dot_index = extext.find('.', start_index)
                    if dot_index != -1:
                        extext = extext[:start_index] + extext[dot_index + 1:]
                        start_number += 1
                else:
                    break

            """
            pattern = r'\b{}\s+[A-Z0-9]'.format(start_number)
            match = re.search(pattern, extext)
            if match:
                print(f"found - page{page+1}")
                start_index = match.start()
                dot_index = extext.find('.', start_index)
                if dot_index != -1:
                    extext = extext[:start_index] + extext[dot_index + 1:]
                    start_number+=1
            """

        extext = " \n" + extext

        #print(text)
        #text[0].strip()
        #extext = "\n".join(text)
        #print(text)

        mpath = open("./hitler_text/process/Hitlers_table_talk.pdf.txt", 'a', encoding="utf-8")
        mpath.write(extext)
        # mpath.write(text)

    print(start_number)