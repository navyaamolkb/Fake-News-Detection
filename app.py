from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model and vectorizer
loaded_model = pickle.load(open('models/model.pkl', 'rb'))
loaded_tfidfvect = pickle.load(open('models/tfidfvect.pkl', 'rb'))


# -----------------------------
# SIMPLE PREPROCESS (No NLTK)
# -----------------------------
def preprocessText(text):
    text = text.lower()                          # lowercase
    text = re.sub(r'[^a-zA-Z]', ' ', text)       # remove symbols & numbers
    text = text.split()                          # split into words
    return " ".join(text)                        # join back


# -----------------------------
# PREDICTION FUNCTION
# -----------------------------
def fake_news_det(text):
    processed = preprocessText(text)
    vectorized = loaded_tfidfvect.transform([processed])
    prediction = loaded_model.predict(vectorized)[0]

    return "Fake News ❌" if prediction == 0 else "Real News ✅"


# -----------------------------
# ROUTES
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    pred = fake_news_det(message)
    return render_template('result.html', prediction=pred, message=message)


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
