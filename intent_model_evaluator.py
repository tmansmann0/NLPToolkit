import pickle
import nltk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

model = load_model('intent_model.h5')

def preprocess_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    return " ".join(words)

def predict_intent(text):
    preprocessed_text = preprocess_text(text)
    tokenizer = pickle.load(open('submodules/NLP/tokenizer.pkl', 'rb'))
    label_encoder = pickle.load(open('submodules/NLP/label_encoder.pkl', 'rb'))
    sequence = tokenizer.texts_to_sequences([preprocessed_text])
    X_pred = pad_sequences(sequence, maxlen=10)
    y_pred = model.predict(X_pred)
    intent = label_encoder.inverse_transform(np.argmax(y_pred, axis=1))[0]
    return intent

while True:
    text = input("Enter a text (or type 'quit' to exit): ")
    if text == "quit":
        break
    intent = predict_intent(text)
    print("Predicted Intent:", intent)
