from collections import Counter
import nltk
import string

with open("test.txt", "r", encoding="latin-1") as f:
    sentences = nltk.tokenize.sent_tokenize(f.read())
    for sentence in sentences[:5]:
        sentence = sentence.replace("\n", " ")
        words = nltk.tokenize.word_tokenize(sentence)
        words = [word.lower() for word in words if word.isalpha()]
        first_letters = [word[0] for word in words]
        c = Counter()
        for letter in "abcdefghijklmnopqrstuvwxyz":
            for l in first_letters:
                if l == letter:
                    c[l] += 1
        print(c.most_common(1)[0][0], c.most_common(1)[0][1] / len(words))
