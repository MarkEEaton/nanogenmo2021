from collections import Counter
from nltk.corpus import stopwords
import langdetect
import nltk
import string


with open("test.txt", "r", encoding="latin-1") as f1:
    sentences = nltk.tokenize.sent_tokenize(f1.read())
    for sentence in sentences:
        sentence = sentence.replace("\n", " ")
        try:
            language = langdetect.detect(sentence)
        except langdetect.lang_detect_exception.LangDetectException:
            language = "none"
        sentence = sentence.replace('"', '')
        sentence = sentence.replace("(", "")
        sentence = sentence.replace(")", "")
        sentence = sentence.replace("_", "")
        if sentence.isupper() or (language != 'en'):
            pass
        else:
            words = nltk.tokenize.word_tokenize(sentence)
            words = [word.lower() for word in words if word.isalpha()]
            words = [word for word in words if word not in stopwords.words("english")]
            first_letters = [word[0] for word in words]
            c = Counter()
            for letter in "a":
                for l in first_letters:
                    if l == letter:
                        c[l] += 1
            try:
                if c.most_common(1)[0][1] / len(words) > 0.6:
                    with open("novel.txt", "a", encoding="latin-1") as f2:
                        print(sentence)
                        f2.write(sentence + " ")
            except IndexError:
                pass
            except:
                raise
