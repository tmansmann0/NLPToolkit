import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
import pickle
import os

nltk.download('punkt')
nltk.download('stopwords')
model_path = 'advanced_ner_model'

def preprocess_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)
#Include 15-25 minimum examples for each route. More if there is more neuance and overlap.
#Traning data should be loads of different ways of asking/saying the same thing
#The more the better.
#Once done, hit train and take note of what epoch your model reaches 98-100% accuracy at
#and tune the # of epochs to that number to prevent overfiting

#set epochs here. I use 65 epochs for 300 examples with 5 different intents
epochs=65

training_data = [
    ("your first type of action", "action_descripton"),
    ("your first type of action", "action_2_description"),
]

X = [preprocess_text(example) for example, _ in training_data]
y = [intent for _, intent in training_data]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
sequences = tokenizer.texts_to_sequences(X)
X = pad_sequences(sequences, maxlen=10)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = Sequential()
model.add(Embedding(len(tokenizer.word_index) + 1, 32, input_length=10))
model.add(LSTM(32))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#set epochs here
model.fit(X_train, y_train, batch_size=64, epochs=epochs, validation_data=(X_test, y_test))

model.save('intent_model.h5')

with open('../tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

with open('../label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
