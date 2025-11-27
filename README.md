# Fake-News-Detection

# Problem Definition
This project focuses on building a system that can distinguish genuine news articles from misleading or fabricated ones. The goal is to create a model capable of analysing text and predicting whether a news item is real or fake.

# Approach
Fake-news detection works best when the model learns from labelled examples. Here, supervised learning is used so that the algorithm studies previously tagged articles and learns the patterns that separate truth from deception. Logistic Regression, Decision Tree Classifier, and PassiveAggressiveClassifier were explored, and the final model is based on the PassiveAggressiveClassifier due to its stronger performance.

# Data Collection
The dataset consists of news items gathered from different sources. It may include content scraped from websites, collected from archives, or downloaded from the dataset folder included within the project repository.

# Data Exploration
Before training, the data is examined to understand the nature of the text. Visual libraries such as matplotlib, seaborn, and wordcloud are used to make sense of the distribution of information and highlight patterns within titles and article bodies.

# Data Preparation
The collected data is cleaned and refined. Duplicate entries are removed, missing details are handled, and any inconsistencies are corrected so that the model receives reliable input.

# Feature Engineering
Only the title and content of each news article are used as meaningful inputs to the model. Irrelevant fields, such as the author column, are excluded to maintain focus on the actual text.

# Model Training
Several algorithms are trained and tested to understand how well they classify the articles. After comparing their accuracy, the PassiveAggressiveClassifier is selected as the final choice.

# Model Evaluation
The trained model is assessed using accuracy as the metric. Once its performance is verified, it becomes ready to classify unseen articles.

# Prediction
The finished system can analyse any new text and estimate whether it belongs to real news or fake news.

# Getting Started

To run this project in VS Code, clone the repository and set up your environment as follows:

- Open your terminal inside the project folder and create a virtual environment:
python -m venv venv
- Activate it:
venv\Scripts\activate
- Install the required packages:
pip install -r requirements.txt
- Then start the application:
python app.py
- Once it runs, open the browser and visit:
http://127.0.0.1:5000/

The web app will load and you can test the predictions directly.

<img width="1920" height="909" alt="Screenshot (275)" src="https://github.com/user-attachments/assets/5660f37f-648f-4fe4-bd51-5926b903bf7f" />
