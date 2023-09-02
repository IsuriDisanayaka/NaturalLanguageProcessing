from flask import Flask, render_template, request

import pickle
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the fitted TF-IDF vectorizer
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

# Function to preprocess text
def preprocess_text(text):
    # Text cleaning similar to what you did before
    contraction_dict = {"ain't": "is not", "aren't": "are not", "can't": "cannot", "'cause": "because",
                        "could've": "could have", "couldn't": "could not", "didn't": "did not",
                        "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not",
                        "haven't": "have not", "he'd": "he would", "he'll": "he will", "he's": "he is",
                        "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have"}

    def _get_contractions(contraction_dict):
        contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
        return contraction_dict, contraction_re

    def replace_contractions(text):
        contractions, contractions_re = _get_contractions(contraction_dict)

        def replace(match):
            return contractions[match.group(0)]

        return contractions_re.sub(replace, text)

    text = replace_contractions(text)

    # Remove punctuations
    text = "".join([char for char in text if char not in string.punctuation])

    # Convert to lowercase
    text = text.lower()

    # Remove hashtags
    text = re.sub(r"\#", "", text)

    # Remove URL addresses
    text = re.sub(r"http\S+", "URL", text)

    # Remove '@' symbols
    text = re.sub(r"@", "", text)

    # Remove multiple contiguous spaces
    text = re.sub("\s{2,}", " ", text)

    # Tokenize the text
    words = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]

    # Remove leftover punctuations
    words = [word for word in words if word.isalpha()]

    cleaned_text = ' '.join(words)

    # Use the loaded TF-IDF vectorizer to transform the text
    tfidf_text = tfidf_vectorizer.transform([cleaned_text])

    return tfidf_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)
    result = 'Disaster' if prediction[0] == 1 else 'Not a Disaster'
    return render_template('index.html', prediction_result=result, input_text=text)

if __name__ == '__main__':
    app.run(debug=True)
