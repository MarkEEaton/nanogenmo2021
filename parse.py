from collections import Counter, defaultdict
from nltk.corpus import stopwords
import langdetect
import nltk
import re
import string

nato = [
    ("a", "Alfa"),
    ("b", "Bravo"),
    ("c", "Charlie"),
    ("d", "Delta"),
    ("e", "Echo"),
    ("f", "Foxtrot"),
    ("g", "Golf"),
    ("h", "Hotel"),
    ("i", "India"),
    ("j", "Juliett"),
    ("k", "Kilo"),
    ("l", "Lima"),
    ("m", "Mike"),
    ("n", "November"),
    ("o", "Oscar"),
    ("p", "Papa"),
    ("q", "Quebec"),
    ("r", "Romeo"),
    ("s", "Sierra"),
    ("t", "Tango"),
    ("u", "Uniform"),
    ("v", "Victor"),
    ("w", "Whiskey"),
    ("x", "Xray"),
    ("y", "Yankee"),
    ("z", "Zulu"),
]


def novel():
    with open("test.txt", "r", encoding="latin-1") as f1:
        results = defaultdict(list)
        novel_words = 0
        sentences = nltk.tokenize.sent_tokenize(f1.read())
        for sentence in sentences:
            sentence = sentence.replace("\n", " ")
            sentence = sentence.replace("\r", " ")
            try:
                language = langdetect.detect(sentence)
            except langdetect.lang_detect_exception.LangDetectException:
                language = "none"
            sentence = sentence.replace('"', "")
            sentence = sentence.replace("(", "")
            sentence = sentence.replace(")", "")
            sentence = sentence.replace("_", "")
            sentence = sentence.replace("[", "")
            sentence = sentence.replace("]", "")
            sentence = sentence.replace("*", "")
            sentence = sentence.replace("|", "")
            sentence = " ".join(sentence.split())
            sentence = re.sub(r"(\.)\1+", "\\1", sentence)
            if sentence.isupper() or (language != "en"):
                pass
            elif sentence[-8:] == "Brigade.":
                pass
            elif sentence[-3:] == "Cf.":
                pass
            elif sentence[-6:] == "Photo.":
                pass
            elif sentence[:4] == "Time":
                pass
            elif sentence[:11] == "INGREDIENTS":
                pass
            elif sentence[:9] == "Copyright":
                pass
            elif sentence[:7] == "Section":
                pass
            elif isnumber(sentence):
                pass
            else:
                words = nltk.tokenize.word_tokenize(sentence)
                words = [word.lower() for word in words if word.isalpha()]
                sentence_words = len(words)
                words = [
                    word for word in words if word not in stopwords.words("english")
                ]
                first_letters = [word[0] for word in words]
                c = Counter()
                for l in first_letters:
                    c[l] += 1
                try:
                    selected_letter = c.most_common(1)[0][0]
                    if novel_words > 50000:
                        print(results)
                        return results
                    if c.most_common(1)[0][1] / len(words) > 0.6:
                        results[selected_letter].append(sentence)
                        novel_words += sentence_words
                        print(sentence)
                except IndexError:
                    pass
                except:
                    raise


def isnumber(sentence):
    for letter in sentence:
        if letter.isnumeric():
            return True
    return False


def assemble(nov):
    with open("novel.txt", "a", encoding="latin-1") as f2:
        for letter in nato:
            try:
                f2.write("\n\n\n" + letter[1].upper() + "\n\n")
                i = 30
                while i < len(nov[letter[0]]):
                    nov[letter[0]].insert(i, "\n     ")
                    i += 31
                f2.write(" ".join(nov[letter[0]]))
            except IndexError:
                pass


if __name__ == "__main__":
    nov = novel()
    assemble(nov)
