# Fake-News-Detection

This project identifies whether a news article is real or fake using machine learning.

# Model Training

After feature engineering, three algorithms were tested: Logistic Regression, Decision Tree Classifier, and PassiveAggressiveClassifier. The PassiveAggressiveClassifier performed the best and was selected as the final model. Hyperparameter tuning was applied to improve results.

# Model Evaluation

The model was evaluated using accuracy. After evaluation, it is used to predict labels for new and unseen articles.

# Getting Started

1. Clone the repository.
2. Open CMD in the project directory.
3. Run:
pip install -r requirements.txt
4. Open the project in any IDE (VS Code or PyCharm).
5. Run Fake_News_Detector.py.
6. Open the browser and go to:
http://127.0.0.1:5000/

The web app will start, and you can test predictions. Sometimes predictions may be incorrect.
