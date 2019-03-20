# data processing modules
import pandas as pd
import os
import re
# text pre-procassing modules
import nltk
import tensorflow
from autocorrect import spell
from nltk.corpus import stopwords, words
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn
from keras.preprocessing.text import Tokenizer
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('words')
nltk.download('sentiwordnet')
maxFeatures = 2000
stop_words = set(stopwords.words('english'))
tokenizer = Tokenizer(num_words=maxFeatures, split=' ')
with open('big_dict 0.5.txt', 'r') as file:
    english_vocab = [word.replace("\n", '') for word in file.readlines() if len(word) > 0]

# patterns = [
#     r'<[^>]+>',  # HTML tags
#     r'(?:@[\w_]+)',  # @-mentions
#     r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
#     r'http[s]?://(?:[\w+]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
#     r'\d+',  # numbers
#     r"['-]\w+",  # words with - and '
#     r"[:;=%x][o0\-^_]?[ds\\\[\]\(\)/i|><]+",  # smiles
# ]
#
#
# def ClearFromPatterns(str, patterns):
#     result = str
#     for pattern in patterns:
#         result = re.sub(pattern, '', result)
#     return result
#
#
# def Split(text):
#     # splitPatter = r"[!@#$%^&*\(\)-+\[\]{}:;\'\"< >?/.,]"
#     # splitPatter = r"[!?.,:\( \) \\/\"\'*;\[\=+&-]"
#     regex = r'(\w*) '
#     list1 = re.findall(regex, text)
#     return list1
#
#
# def DeletePunctuation(text):
#     return ' '.join([word for word in Split(text) if len(word) > 0])
#
#
# def DeleteStopWords(words, stopWords):
#     return [word for word in words if word not in stopWords]
#
#
# def CorrectSpelling(words):
#     text = [spell(word).lower() if len(word) > 3 else word for word in words]
#     return text
#
#
# def MorphyCorrection(words):
#     res = []
#     for word in words:
#         newWord = wn.morphy(word)  # Returns None if it cant change word
#         if newWord:
#             res.append(newWord)
#         else:
#             res.append(word)
#     return res
#
#
# def GrammarPreProcessing(text):
#     text = text.lower()
#     text = ClearFromPatterns(text, patterns)
#     text = DeletePunctuation(text)
#     words = text.split(' ')
#     words = DeleteStopWords(words, stop_words)
#     words = CorrectSpelling(words)
#     words = MorphyCorrection(words)
#     return ' '.join(words)

from nltk.tokenize import word_tokenize

# import itertools
# from nltk.collocations import BigramCollocationFinder
# from nltk.metrics import BigramAssocMeasures
#
# words = """ The next set of methods seem to be based mostly on the idea of assuming a generative model for the data and doing hypothesis testing. I.e., you can have one model that assumes the two words are independent (the null hypothesis), and one that assumes they are not. Typically this is implemented as multinomials over words, and then a classical statistical test is applied to the estimated maximum likelihood parameters of the data. You can use Dice coefficient, t-score, chi-squared, or even something simpler like the log-likelihood ratio."""
# words = word_tokenize(words)
# def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
#     bigram_finder = BigramCollocationFinder.from_words(words)
#     bigrams = bigram_finder.nbest(score_fn, n)
#     return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])



#text = """it was cat. Lemmatization reduces words to their base word, which is  lemmas.
  #It transforms root words with the use of vocabulary and morphological analysis. correct books."""
# text = GrammarPreProcessing(text)
# text = word_tokenize(text)
# print(Adv_Adj(text))
#text = list(nltk.bigrams(text))
#text1 = []
#for bigram in text:
    #pos_tag_bigram = nltk.pos_tag(bigram, tagset='universal')
    #if pos_tag_bigram[0][1] != "ADV" and pos_tag_bigram[1][1] != "ADJ":
        #text1.append(pos_tag_bigram[0][0])
#print(text) #[('awfully', 'polite'), ('polite', 'lemmatization'), ('lemmatization', 'reduce'),
# ('reduce', 'words'), ('words', 'base'), ('base', 'linguistically'), ('linguistically', 'correct'),
# ('correct', 'transform'), ('transform', 'root'), ('root', 'words'), ('words', 'use'),
# ('use', 'vocabulary'), ('vocabulary', 'morphological'), ('morphological', 'correct')]
#print(text) #['polite', 'lemmatization', 'reduce', 'words', 'base', 'correct',
#  'transform', 'root', 'words', 'use', 'vocabulary', 'morphological']
# убрал awfully из awfully polite, linguistically из linguistically correct.
text = """Boss doesn't want to use a car. I do not prefer apple. He is hardly happy"""
# def Negation(text):
#     text_not = word_tokenize(text)
#     result = []
#     negation_list = ["no", "not", "rather", "hardly"]
#     #k_emot_neg = 0
#     k_emot_of_word = 0
#     # n't to not
#     for word in text_not:
#         if word == "n't":
#             result.append("not")
#         else:
#             result.append(word)
#     text_not = result
#     # for word in text_not:
#     #     word = nltk.pos_tag(word, tagset='universal')
#     # text_not = list(nltk.bigrams(text))
#     text1 = []
#     list_of_after_neg_word = []
#     text_not = list(nltk.bigrams(text_not))
#     print(text_not)
#     for bigram in text_not:
#         pos_tag_bigram = nltk.pos_tag(bigram, tagset='universal')
#         if pos_tag_bigram[0][0] in negation_list and (pos_tag_bigram[1][1] == "VERB" or pos_tag_bigram[1][1] == "ADJ"):
#             list_of_after_neg_word.append(pos_tag_bigram[1][0])
#             #k_emot_of_word = 1
#             #list_of_k_emot_of_word.append(k_emot_of_word)
#             #print(pos_tag_bigram)
#         # else:
#         #     k_emot_of_word = 0
#         #     list_of_k_emot_of_word.append(k_emot_of_word)
#     # for word in text_not:
#     #     if word[0] in negation_list:
#     #         k_emot_neg = 1 # рандомная цифра
#     #     elif (word[1] == "VERB" or word[1] == "ADJ") and k_emot_neg == 1:
#     #         k_emot_of_word = 1
#     #print(list_of_k_emot_of_word)
#     return list_of_after_neg_word
#
# возвращает лист слов, у которых тональность должна стать противоположной
def Negation(text):
    text_not = word_tokenize(text)
    result = []
    negation_list = ["no", "not", "rather", "hardly"] #слова-отрицатели
    # n't to not
    for word in text_not:
        if word == "n't":
            result.append("not")
        else:
            result.append(word)
    text_not = result
    list_of_after_neg_word = []
    text_not = list(nltk.bigrams(text_not))
    print(text_not)
    for bigram in text_not:
        pos_tag_bigram = nltk.pos_tag(bigram, tagset='universal')
        if pos_tag_bigram[0][0] in negation_list and (pos_tag_bigram[1][1] == "VERB" or pos_tag_bigram[1][1] == "ADJ"):
            list_of_after_neg_word.append(pos_tag_bigram[1][0])
    return list_of_after_neg_word
print(Negation(text))
#text_not = list(nltk.bigrams(text_not))
# text_not1 = []
# for bigram_not in text_not:
#     pos_tag_bigram_not = nltk.pos_tag(bigram_not, tagset='universal')
#     print(pos_tag_bigram_not)
    # проблема: как часть речи не выловим. а на препроцессинге они просто удаляются.
    # то есть надо как-то перевести в коэф для следующего слова
    # а тут уже вопрос к вам: можно ли при определении сентимента учитывать какие-то коэфы?
    #[('Boss', 'NOUN'), ('does', 'VERB')]
    #[('does', 'VERB'), ('not', 'ADV')]
    #[('not', 'ADV'), ('want', 'VERB')]
#text_not = GrammarPreProcessing(text_not)
#print(text_not) # boss want use like - only GrammarPreProcessing(text_not)

# d = {"i": [0,1,2,3],"lang_label":['__label__eng','__label__eng','__label__eng1','__label__eng'],"if_eng":[0,0,0,0]}
# test_results = pd.DataFrame(data=d)
# #test_result=test_results.loc[ : , "lang_label":"if_eng"]
# j=0
# english_1 = []
# for lang in test_results.loc[ : , "lang_label"]:
#     if lang == '__label__eng':
#         english_1.append(1)
#     else:
#         english_1.append(0)
#     j = j + 1

# print(test_results)
#result: lang_label  if_eng
#0   __label__eng       1
#1   __label__eng       1
#2  __label__eng1       0
#3   __label__eng       1
#доп:
#if test_results.isin(['__label__eng']) - по идее чекает наличие
#test_results.replace({'if_eng': 0}, 1) - заменяет

