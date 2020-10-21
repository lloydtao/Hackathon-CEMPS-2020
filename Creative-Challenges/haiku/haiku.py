""" Hackathon - Poetry (Haiku) """

from random import sample, choice
from datetime import datetime
from nltk import ConditionalFreqDist
from nltk.corpus import cmudict
from nltk.util import bigrams


# Read word list from text file
with open("word_list.txt") as f:
    content = f.readlines()
corp = [x.strip() for x in content]
lc_corp = [w.lower() for w in corp]

pro = cmudict.dict()
good_words = [x for x in lc_corp if x in pro]


def generate_starts():
    words = [("1", word) for word in good_words]
    words = sample(words, len(words))
    starts = words[-100:]
    return starts


def count_syllables(word):
    stress = [x for x in pro[word][0] if x[-1].isdigit()]
    return len(stress)


def construct_line(total, previous_word=None):
    starts = generate_starts()
    if total == 0:
        line = []
    else:
        if previous_word:
            next_words = [w for w in good_words if count_syllables(w) <= total]
            if len(next_words) == 0:
                ok_starts = [w for (n, w) in starts if count_syllables(w) <= total]
                next_word = choice(ok_starts)
            else:
                next_word = choice(next_words)
            num_syllables = count_syllables(next_word)
            remaining = total - num_syllables
            line = [next_word] + construct_line(remaining, next_word)
        else:
            ok_starts = [w for (n, w) in starts if count_syllables(w) <= total]
            first_word = choice(ok_starts)
            num_syllables = count_syllables(first_word)
            remaining = total - num_syllables
            line = [first_word] + construct_line(remaining, first_word)
    return line


def haiku():
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print()
    print("    | " + " ".join(construct_line(5)))
    print("    | " + " ".join(construct_line(7)))
    print("    | " + " ".join(construct_line(5)))
    print()
    print(" - Matthew Collison (" + date_created + ")")
    print()


if __name__ == "__main__":
    haiku()
