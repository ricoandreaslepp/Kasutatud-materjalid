from estnltk import Text
from salvestaja import salvestamine
import os

def solve(sheet):
    global text_to_fix
    text = Text(open(text_to_fix, "r", encoding="UTF-8").read())

    i = 1
    for result in text.spellcheck_results:
        sheet.write(i, 0, result['text'])
        sheet.write(i, 1, result['spelling'])
        if (result['suggestions']):
            sheet.write(i, 2, result['suggestions'][0])
            sugges = ""
            for sent in result['suggestions']:
                sugges += (sent + ", ")
            sheet.write(i, 3, sugges)
        i += 1

    return i

# fix texts
os.chdir("../sis_tekst/kasutatud tekstid")
for file in os.listdir():
    global text_to_fix
    text_to_fix = file

    salvestamine("EstNLTK", solve, text_to_fix)
    os.chdir("./sis_tekst/kasutatud tekstid")