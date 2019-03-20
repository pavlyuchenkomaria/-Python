#import SpellChecker as SpellChecker
import nltk
nltk.download()
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.probability import FreqDist

#tokenized_text_words2 = word_tokenize(text2)
#freq = FreqDist(tokenized_text_words2)
#print(freq.most_common())
#print(freq)

import matplotlib.pyplot as plt
#freq.plot(30,cumulative=False)
#plt.show()

#print("after stemming:",stemmed_words_text2)

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()
import re

from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))

from spellchecker import SpellChecker
spell = SpellChecker()
import urbandict as ud

def IsExist(word):
    try:
        define = ud.define(word)
    except:
        return False
    return True

text_for_all_tests_except_bigrams = """ Lemmatization reduces words to their base word, which is linguistically correct lemmas.
 It transforms root words with the use of vocabulary and morphological analysis. 
 Lemmaaaaatization is usually more 3645 sophisticated than stemming. Stemmer works on 
 an individual word without knowledge of the context!!! For example, The word "better" 
 has "good" as its lemma. This thing will miss by stemming because it 
 requires a dictionary look-up."""

text = """it was awfully beautiful."""
# убрали заглавные
text = text.lower()
# убрали цифры
text = re.sub(r"\d+", " ", text)
# токенизировали
text = word_tokenize(text)
# убрали все знаки кроме точки
# почистили стоп-слова
# проверили на существование
# лемматизировали
text3 = []
#text = spell.known(text)
#and IsExist(w) еще одно условие в иф
for w in text:
    if w.isalpha() and w not in stop_words:
        w = lem.lemmatize(w)
        w = lem.lemmatize(w, pos="v")
        text3.append(w)
    elif w == '.':
        text3.append(w)
text = text3
text = list(nltk.bigrams(text))
for bigram in text:
    pos_tag_bigram = nltk.pos_tag(bigram, tagset='universal')
    # if pos_tag_bigram[0][1] == "ADV" and pos_tag_bigram[1][1] == "ADJ":
        #здесь я придумаю, как простроить, чтобы менялась не биграмма, а удалялось слово из текста
    print(bigram)
# от того, что я меняю биграммы - текст не меняется

print(text)

"""https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk
https://www.nltk.org/book/ch01.html
"""

#for word in text if word.isalpha() - только для слов

