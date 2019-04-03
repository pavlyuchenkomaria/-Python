import collections
import json
import newspaper

from newspaper import Article
from collections import Counter

# text pre-procassing modules
from nltk import FreqDist
from nltk.corpus import stopwords, words
# model modules
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize

import csv

def DeletePunctuation(text):
    return [word for word in text if len(word) > 1]

def DeleteStopWords(words, stopWords):
    return [word for word in words if word not in stopWords]

def GrammarPreProcessing1(text):
    text = text.lower()
    text = word_tokenize(text)
    text = DeletePunctuation(text)
    text = DeleteStopWords(text, stop_words)

    return text

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# функция дает dictionary пар "частота слова в тексте - слово" из текстового файла (файл очищен
# пунктуации и стоп-слов)
def Count_freq_of_words():
    file1 = open("articles_CRIME.txt", "r", encoding="utf-8")
    data_set = file1.read()
    data_set = GrammarPreProcessing1(data_set)
    freqdict = wordListToFreqDict(data_set)
    return sortFreqDict(freqdict)

# функция дает dictionary пар "частота слова в тексте - слово" из текстового файла (файл очищен
# пунктуации и стоп-слов)
def Count_most_common_words():
    file1 = open("articles_CRIME.txt", "r", encoding="utf-8")
    data_set = file1.read()
    data_set = GrammarPreProcessing1(data_set)

    #график распределения частот слов
    fdist1 = FreqDist(data_set)
    fdist1.plot(150, cumulative=False)

    #считает частоты самых популярных
    counter = Counter(data_set)
    most_occur = counter.most_common(50)
    return most_occur


print(type(Count_most_common_words()))
print(type(Count_freq_of_words()))

# функция берет из json файла, где есть размеченные по тегам новости и ссылки на них
# и по выбранной в if категории закидывает тексты новостей с этих ссылок в соответствующий файл
# требует:
# import collections
# import json
# import newspaper
# from newspaper import Article

# file1 = open("articles_CRIME.txt", "a+", encoding="utf-8")
# with open('C:\\Users\\Masha\\PycharmProjects\\ff\\-Python\\perfect ART\\News_Category_Dataset_v2.json') as f:
#     i = 0
#     for line in f: # берем одну строку, так как это отдельный джейсонфайл
#         if (i == 10):
#             break
#         json_row = json.loads(line) # парсим ее
#         if json_row['category'] == "CRIME":
#             i = i+1
#             url = json_row['link']
#             article = Article(url)
#             article.download()
#             article.parse()
#             file1.write(article.text)
#
# file1.close()





