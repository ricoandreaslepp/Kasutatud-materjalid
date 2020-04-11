import re
import os

from salvestaja import salvestamine
from collections import Counter

probability_dict = {}


def study():
    # algkorpuse fail
    study_text = "tasakaalus_ilu_teadus.txt"

    return Counter(words(open(study_text, encoding="utf-8").read()))


def words(text):
    return re.findall(r'\w+', text.lower())


def P(word):
    "Probability of `word`."
    "check if the üäöõ words count in as well"
    N = sum(WORDS.values())
    return WORDS[word] / N


def init_ngram_probability():
    from ngrammid_mudel import return_probability_dict
    global probability_dict
    probability_dict = return_probability_dict()


def correction_with_ngrams(word, word_before):
    possible_corrections = candidates(word)

    corrections_dict = {}
    for correction in possible_corrections:
        corrections_dict.update({correction: P(correction)})

    for correct in possible_corrections:

        if (word_before, correct) in probability_dict.keys():
            corrections_dict[correct] += probability_dict[(word_before, correct)]

    return sorted(corrections_dict.items(), key=lambda key_value: key_value[1])[len(corrections_dict) - 1][0]


def candidates(word):
    "Generate possible spelling corrections for word."
    return (list(known(edits1(word))) + [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyzõüäö'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def solve(sheet):
    global text_to_fix
    tokens = words(open(text_to_fix, "r", encoding="UTF-8").read())
    fixed = tokens[0] + " "

    sheet.write(1, 0, tokens[0])
    sheet.write(1, 1, "TRUE")

    i = 2
    for index in range(1, len(tokens)):
        word = tokens[index]
        word_before = fixed.split(" ")[index - 1]

        sheet.write(i, 0, word)
        corrected = correction_with_ngrams(word, word_before)
        if word != corrected:
            sheet.write(i, 1, "FALSE")
            sheet.write(i, 2, corrected)
            if candidates(word):
                sugges = ", ".join(candidates(word))
                sheet.write(i, 3, sugges)
        else:
            sheet.write(i, 1, "TRUE")

        i += 1

        fixed += corrected + " "

    return i


os.chdir("../sis_tekst/Algkorpused")
WORDS = study()
os.chdir("../../")

# fix texts
os.chdir("./sis_tekst/kasutatud_tekstid")
for file in os.listdir():
    global text_to_fix
    text_to_fix = file

    salvestamine("Peter Norvig, N-gram", solve, text_to_fix)
    os.chdir("./sis_tekst/kasutatud_tekstid")
