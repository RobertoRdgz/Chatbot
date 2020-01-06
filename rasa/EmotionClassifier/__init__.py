from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, KFold, train_test_split

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import base64
import string
import pandas as pd
import numpy as np

EmotionOrder = {'anger':0 ,'disgust':1, 'fear':2 ,'guilt':3, 'joy':4 ,'sadness':5 , 'shame':6}

def clean_text(text):
    remove_punc = [char for char in text if char not in string.punctuation]
    remove_punc = ''.join(remove_punc)
    clean_words = [word for word in remove_punc.split() if word.lower() not in stopwords.words('english')]
    #return ' '.join(clean_words)
    return clean_words


def clean_data(messages):
    """Delete some rows of the dataset"""

    messages = messages.loc[messages['text'] != " No response."]
    messages = messages.loc[messages['text'] != "no response."]
    messages = messages.loc[messages['text'] != "NO RESPONSE."]
    messages = messages.loc[messages['text'] != " I have never felt this emotion."]
    messages = messages.loc[messages['text'] != "Not applicable."]
    messages = messages.loc[messages['text'] != "None."]
    messages = messages.loc[messages['text'] != "Nothing."]

    return messages

def most_frequent(List):
    """return the most frequent emotion in the List"""

    List = List.tolist()
    return max(set(List), key = List.count)


class CLF:
    def __init__(self):
        self.train_model()

    def train_model(self):
        messages = pd.read_csv("ISEAR_4.csv", encoding='latin-1')
        messages = clean_data(messages)

        #messages["text"] = messages['text'].apply(clean_text)

        X = messages['text']
        Y = messages['class']

        self.pipeline = Pipeline([
            ('bow',CountVectorizer()), # converts strings to integer counts
            ('tfidf',TfidfTransformer()), # converts integer counts to weighted TF-IDF scores
            ('Multinomial_classifier',MultinomialNB()) # train on TF-IDF vectors with Naive Bayes classifier
        ])
        self.pipeline.fit(X, Y)

    def predict(self, message):
        """This fuction returns the most repeated emotion in the prediction
        and its maximum probability """

        #Clean the input:
        input_ = clean_text(message)

        if input_ == []:
            return None, None 

        #Make the prediction to obtain the list of emotion:
        prueba = self.pipeline.predict(input_)

        #Get the most repeated emotion:
        most_frequentEmotion = most_frequent(prueba)

        #Find the index of the most frequent emotion from Emotion order:
        emotion_idx = EmotionOrder[most_frequentEmotion]

        #Make the prediction to obtain the probabilities array:
        probs_approach = self.pipeline.predict_proba(input_)

        Probas = []
        for prob in probs_approach:
            #Get the prob for the most frequent emotion in every sublist:

            prob_ = prob[emotion_idx]
            Probas.append(prob_)

        #Obtain the maximum probability of the most frequent emotion:
        most_frequentEmotion_prob = max(Probas)

        return most_frequentEmotion, most_frequentEmotion_prob
