from flask import Flask, render_template, request
import pickle, re, nltk
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)

with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    tfidf_vectorizer = pickle.load(vectorizer_file)

def preprocess_text(text):
    # Text cleaning
    contraction_dict = {
        "ain't": "is not", "aren't": "are not", "can't": "cannot", "'cause": "because",
        "could've": "could have", "couldn't": "could not", "didn't": "did not",
        "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not",
        "haven't": "have not", "he'd": "he would", "he'll": "he will", "he's": "he is",
        "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have"
    }

    def _get_contractions(contraction_dict):
        contraction_re = re.compile('(%s)' % '|'.join(contraction_dict.keys()))
        return contraction_dict, contraction_re

    def replace_contractions(text):
        contractions, contractions_re = _get_contractions(contraction_dict)

        def replace(match):
            return contractions[match.group(0)]

        return contractions_re.sub(replace, text)

    text = replace_contractions(text)
    text = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    text = text.lower()
    text = re.sub(r"\#", "", text)
    text = re.sub(r"http\S+", "URL", text)
    text = re.sub(r"@", "", text)
    text = re.sub("\s{2,}", " ", text)

    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    words = [word for word in words if word.isalpha()]
    cleaned_text = ' '.join(words)

    # Use the loaded TF-IDF vectorizer to transform the text
    # tfidf_text = tfidf_vectorizer.transform([cleaned_text])

    temp = [cleaned_text]
    print(cleaned_text)
    temp1 =   tfidf_vectorizer.transform(temp)
    return  temp1

    # return tfidf_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)
    prediction = model.predict(preprocessed_text)

    result = 'Disaster' if prediction[0] == 1 else 'Not a Disaster'
    return render_template('index.html', prediction_result=result, input_text=text)

if __name__ == '__main__':
    app.run(debug=True)
