from nltk import ngrams
from collections import Counter
from failid import study_text

def make_n_gramlist(text, n=2):
    nngramlist = []
    for s in ngrams(text.split(), n=n):
        nngramlist.append(s)
    return nngramlist


def return_probability_dict():
    text = open(study_text, "r", encoding="UTF-8").readline()

    probability_dict = {}
    n_grammide_korpus = make_n_gramlist(text)
    sõnad = Counter(text.split(" "))
    fraasid = Counter(n_grammide_korpus)

    for ph in fraasid:
        probability_dict.update({ph: fraasid[ph] / sõnad[ph[0]]})


    return probability_dict

