import numpy as np
import pandas as pd
from sklearn import svm


#https://scikit-learn.org/stable/supervised_learning.html#supervised-learning
#https://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf
#http://qaru.site/questions/349557/very-simple-text-classification-by-machine-learning
#http://zabaykin.ru/?p=558
#http://mechanoid.kiev.ua/ml-text-proc.html
#https://www.kaggle.com/vamsi1251/bag-of-words-model
#https://www.kaggle.com/c/word2vec-nlp-tutorial#evaluation

# example scikit-learm

#def main():
    #X = [[0, 0], [1, 1]]
    #y = [0, 1]
    #clf = svm.SVC(gamma='scale')
    #clf.fit(X, y)
    #print(clf)

#if __name__ == '__main__':
   # main()

# example spacy

""" import spacy

 Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

 The text we want to examine
text = London is the capital and most populous city of England and 
the United Kingdom.  Standing on the River Thames in the south east 
of the island of Great Britain, London has been a major settlement 
for two millennia. It was founded by the Romans, who named it Londinium.


# Parse the text with spaCy. This runs the entire pipeline.
doc = nlp(text)

# 'doc' now contains a parsed version of text. We can use it to do anything we want!
# For example, this will print out all the named entities that were detected:
for entity in doc.ents:
    print(f"{entity.text} ({entity.label_})")

# example pymorphy2
#https://github.com/kmike/pymorphy2/blob/master/docs/user/guide.rst

# import pymorphy2 - нужно импортировать
# morph = pymorphy2.MorphAnalyzer()
# morph.parse('стали')
"""

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[ : , : -1].values
Y = dataset.iloc[ : , 3].values
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[:, 1:3])
    # взяли данные из места, с ними поработали и туда же вернули
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
 # создали объект в классе
label_encoder = LabelEncoder()
 # заменили во всех строках первый столбец
 # с названием страны на цифру для этой страны
X[ : , 0] = label_encoder.fit_transform(X[ : , 0])

onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

print(X_train)