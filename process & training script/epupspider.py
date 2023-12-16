import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as soup


def parse_epub(file_path,output):
    book = epub.read_epub(file_path)

    text_content = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text_content.append(item.get_content().decode("utf-8"))

    wt = "\n".join(text_content)
    sp = soup(wt, "html.parser")
    text = sp.get_text()
    #text_content.append(text)

    ft = open(output, "w", encoding="utf-8")
    ft.write(text)

epub_file = "hitler_text/Mein Kampf.epub"

output = "./hitler_text/Mein Kampf.txt"

parse_epub(epub_file, output)