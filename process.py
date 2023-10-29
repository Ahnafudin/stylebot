import json
import random
import string
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

class ChatBot:
    def __init__(self):
        self.input_shape = 8
        self.responses = {}
        self.lemmatizer = WordNetLemmatizer()
        self.tokenizer, self.le, self.model = None, None, None
        self.load_resources()
        self.prepare_model()

    def load_resources(self):
        with open('dataset/chatbot.json') as content:
            data = json.load(content)
        for intent in data['intents']:
            self.responses[intent['tag']] = intent['responses']

        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)

    def prepare_model(self):
        self.tokenizer = pickle.load(open('model/tokenizers.pkl', 'rb'))
        self.le = pickle.load(open('model/le.pkl', 'rb'))
        self.model = keras.models.load_model('model/chat_model.h5')

    def remove_punctuation(self, text):
        text = ''.join([letters.lower() for letters in text if letters not in string.punctuation])
        return [text]

    def vectorize_text(self, text):
        texts_p = self.remove_punctuation(text)
        vector = self.tokenizer.texts_to_sequences(texts_p)
        vector = np.array(vector).reshape(-1)
        vector = pad_sequences([vector], self.input_shape)
        return vector

    def predict(self, text):
        vector = self.vectorize_text(text)
        output = self.model.predict(vector)
        response_tag = self.le.inverse_transform([output.argmax()])[0]
        return random.choice(self.responses[response_tag])

    def generate_response(self, text):
        return self.predict(text)