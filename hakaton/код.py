
# data processing modules
import pandas as pd
import re
# text pre-procassing modules
import os
from autocorrect import spell
from nltk.corpus import stopwords, words
from nltk.corpus import wordnet as wn
# model modules
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
#Marusya adds
import nltk
from nltk.tokenize import word_tokenize

maxFeatures = 2000  # Change carefully. May decrease quality of predictions
maxVectorLen = 300  # Warning! Dont change it. Model learned with this vector size

# nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('words')
# nltk.download('sentiwordnet')

projectFolder = os.path.dirname(__file__)
stop_words = set(stopwords.words('english'))
tokenizer = Tokenizer(num_words=maxFeatures, split=' ')
sentimentWordsPath = os.path.join(projectFolder, 'SentimentWordsData.csv')
dictPath = os.path.join(projectFolder, 'big_dict 0.5.txt')
with open(dictPath, 'r') as file:
    english_vocab = [word.replace("\n", '') for word in file.readlines() if len(word) > 0]
sentimentWords = pd.read_csv(sentimentWordsPath)
sentiDict = {row['word']: (row['NegScore'], row['PosScore']) for index, row in sentimentWords.iterrows()}

patterns = [
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[\w+]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'\d+',  # numbers (Not sure should we delete it on this stage)
    r"['-]\w+",  # words with - and '
    r"[:;=%x][o0\-^_]?[ds\\\[\]\(\)/i|><]+",  # smiles
]


def ClearFromPatterns(str, patterns):
    result = str
    for pattern in patterns:
        result = re.sub(pattern, '', result)
    return result


def Split(text):
    regex = r'(\w*) '
    list1 = re.findall(regex, text)
    return list1


def DeletePunctuation(text):
    return ' '.join([word for word in Split(text) if len(word) > 0])


def DeleteStopWords(words, stopWords):
    return [word for word in words if word not in stopWords]


def CorrectSpelling(words):
    text = [spell(word).lower() if len(word) > 3 else word for word in words]
    return text


def MorphyCorrection(words):
    res = []
    for word in words:
        newWord = wn.morphy(word)  # Returns None if it cant change word
        if newWord:
            res.append(newWord)
        else:
            res.append(word)
    return res


def GrammarPreProcessing(text):
    text = text.lower()
    text = ClearFromPatterns(text, patterns)
    text = DeletePunctuation(text)
    words = text.split(' ')
    words = DeleteStopWords(words, stop_words)
    words = CorrectSpelling(words)
    words = MorphyCorrection(words)
    return ' '.join(words)


def UppercaseCount(text):
    count = 0
    for letter in text:
        if letter.isupper():
            count += 1
    return count


def SentimentPunctuationCount(text):
    return text.count('!')


def PunctuationCount(text):
    return len(re.findall(r'[!?:;.,"]', text)) - 2 * text.count('...')  # we count '...' as 3 dots in findall


def PrepareSet(set, maxVectorLen):
    tokenizer.fit_on_texts(set)
    X = tokenizer.texts_to_sequences(set)
    X = pad_sequences(X, maxlen=maxVectorLen)
    return X


def SmilesCount(text):
    return len(re.findall(r"[:;=%x][o0\-^_]?[ds\\\[\]\(\)/i|><]+", text))


def MakePreprocessData(texts):
    data = pd.DataFrame()
    data['text'] = texts
    data['len'] = [len(text) for text in texts]
    data['words_count'] = [len(text.split()) for text in texts]
    data['uppercase_count'] = [UppercaseCount(text) for text in texts]
    data['meanWords_count'] = [len([word for word in Split(text) if word not in stop_words]) for text in texts]
    data['sentimentPunctuation_count'] = [SentimentPunctuationCount(text) for text in texts]
    data['totalPunctuation_count'] = [PunctuationCount(text) for text in texts]
    data['smiles_count'] = [SmilesCount(text) for text in texts]

    return data


def RealWordsRatio(text):
    if len(text) == 0:
        return 0
    unusual = [word for word in text.split() if word not in english_vocab and len(word) > 0]
    return 1 - float(len(unusual)) / len(text)


def AvarageEmotionRatio(text):
    count = 0
    posSum = 0
    negSum = 0
    for word in text.split():
        if word in sentiDict:
            count += 1
            negSum = sentiDict[word][0]
            posSum = sentiDict[word][1]
    if count == 0:
        return (0, 0)
    else:
        return (negSum / count, posSum / count)

def Adv_Adj(text):
    text = word_tokenize(text)
    text = list(nltk.bigrams(text))
    text1 = []
    k_emot_adj = 1 # коэф - множитель, повышающий эмоциональность
    for bigram in text:
        pos_tag_bigram = nltk.pos_tag(bigram, tagset='universal')
        if pos_tag_bigram[0][1] != "ADV" and pos_tag_bigram[1][1] != "ADJ":
            text1.append(pos_tag_bigram[0][0])
        elif pos_tag_bigram[0][1] == "ADV" and pos_tag_bigram[1][1] == "ADJ":
            k_emot_adj = k_emot_adj + 0.1 # подобрать значение
            return k_emot_adj
    return text1

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

def main():
    # Just write your data path set will be prepared automatically.
    dataPath = os.path.join(projectFolder, "TestData.csv")
    outputPath = os.path.join(projectFolder, 'DATA.csv')
    data = pd.read_csv(dataPath)
    set = MakePreprocessData(data['text'].values)
    set['processed_text'] = [GrammarPreProcessing(text) for text in set['text'].values]
    set['real_words_ratio'] = [RealWordsRatio(text) for text in set['text'].values]
    set['AvarageEmotionRatio'] = [AvarageEmotionRatio(text) for text in set['text'].values]
    X = PrepareSet(set['processed_text'].values, maxVectorLen)
    model = load_model('model.h5')
    pr = model.predict(X, steps=1)

    # creating output file with our analysis
    output = pd.DataFrame()
    output['text'] = data['text']
    output['applicity'] = [
        '1' if row['real_words_ratio'] > 0.9 and row['AvarageEmotionRatio'][0] + row['AvarageEmotionRatio'][1] > 0.05 else '0' for
        index, row in set.iterrows()]
    output['sentiment'] = ['0' if sentiment[0] > sentiment[1] else '1' for sentiment in pr]
    print(output.head(10))
    output.to_csv(outputPath)


if __name__ == "__main__":
    main()


