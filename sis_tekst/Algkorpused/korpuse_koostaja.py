import os
import re
from time import time
from bs4 import BeautifulSoup

# kõik kaustad, milles olevaid .tei faile soovite ühendada tekstifailiks, formaat "./kausta nimi"
folders = ["./tasakaalus_ilukirjandus_lausestatud", "./tasakaalus_teadus_lausestatud"]
# -----------------------
# koostatava korpuse nimi, formaat "nimi.txt"
korpuse_nimi = "nimi.txt"
# -----------------------
korpus = open(korpuse_nimi, "w", encoding="utf-8")
total_words = 0
for fold in folders:
    
    os.chdir(fold)

    temp = "[],'"
    total_str = ""
    for tei_doc in os.listdir(os.curdir):

        with open(tei_doc, "r", encoding="LATIN-1") as tei:
            soup = BeautifulSoup(tei, "html5lib")

        first = list(filter(None, re.split(' |, |\n|\t', str(soup.text).strip())))
        total_words += len(first)
        tx = str(first).translate({ord(i): None for i in temp})
        total_str += tx

    os.getcwd()
    os.chdir("../")
    korpus.write(total_str)

korpus.close()
# mitu sõna saadi tekstifaili
print(total_words)
# --------------------------
