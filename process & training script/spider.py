import os
import shutil
import urllib.request
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup as soup
from bs4.dammit import UnicodeDammit


mag = ["http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Trial/hitletrial.htm",
            "http://www.worldfuturefund.org/Reports2013/hitlerenablingact.htm",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Hitler%20Speech%201937.01.30.html",
            "http://www.worldfuturefund.org/Articles/Hitler/hitler1939.html",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Hitler%20Speech%201940.01.30.htm",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Hitler%20Speech%201941.01.30.html",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Hitler%20Speech%201942.01.30.htm",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Hitler%20on%20Art%20English.htm",
            "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Trial/hitletrial.htm",
            "http://www.worldfuturefund.org/Reports2013/hitlerenablingact.htm"
            ]

##- 예비용 구문
#-> 아래의 링크로부터 구성
# http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/hitler%20key%20speeches%20index.htm
up = "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Trial/hitletrial.htm"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
# headers = {"cookie": "CONSENT=YES+cb.20230531-04-p0.en+FX+908"}
#sneak = urlopen(Request(up, headers=headers)).info()
#print(sneak)


cont = requests.get(url=up, headers=headers, timeout=(0.05, 27)).text

fsoup = soup(cont, 'html.parser')
#print(cont)

#ftcont = fsoup.find_all("span",{'class':'bodytext'})
ftcont = fsoup.find_all("td",{'valign':'top'}) #<td valign="top">
# rows = soup.find('table').find_all( lambda tag: tag.name == 'tr' and 'hidden' not in tag.get('class', '') )
#- 올드 스타일 파싱
# soup.select('div > p')[1].get_text(strip=True)
# find_all
ptxt = ""
for k in ftcont :
    ptxt += k.text.strip()
#ptxt
print(ptxt.encode("utf-8")) #.text.strip(), .get_text(strip=True)
#quit()

def txtload(up):
    #up = "http://www.worldfuturefund.org/wffmaster/reading/hitler%20speeches/Trial/hitletrial.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    cont = requests.get(url=up, headers=headers).text


    """
    dammit = UnicodeDammit(cont, is_html=True, override_encodings=['windows-1252'])
    decoded_html = dammit.unicode_markup
    fsoup = soup(decoded_html, 'html.parser', from_encoding='windows-1252')
    """

    fsoup = soup(cont, 'html.parser')
    #fsoup = soup(cont, 'lxml')

    ftcont = fsoup.find_all("td", {'valign': 'top'})  # <td valign="top">
    ptxt = ""
    for k in ftcont:
        ptxt += k.text.strip()
    return ptxt
    #print(ptxt)


#"""
##- save that damn thing.
e = "textstorage"
try:
    shutil.rmtree(e)  # cleanup
except:
    print("exception : 굴러 이놈아")
os.makedirs(e)
os.chdir(e)
print("- all green")
#"""


for i in range(len(mag)):
    #txtload(mag[i])
    mpath = open(f"{i}.txt", 'w', encoding="utf-8")
    mpath.write(txtload(mag[i]))


print(" - 완료")