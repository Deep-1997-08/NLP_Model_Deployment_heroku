from flask import Flask, render_template,url_for, request
import pandas as pd 
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import nltk
import os

if 'DYNO' in os.environ:
    nltk.download('stopwords')

filename = 'nlp_model.pkl'
clf = joblib.load(filename)
cv= joblib.load('transform.pkl')
app = Flask(__name__)


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/predict', method=['POST'])
def predict():
  if request.method == 'POST':
    message = request.form['message']
    data = [message]
    vect = cv.transform(data).toarray()
    my_prediction = clf.predict(vect)
  return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
  app.run(debug=True)
