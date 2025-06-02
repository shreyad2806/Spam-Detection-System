# spam_detector.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load and prepare data
df = pd.read_csv("spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

X_train, _, y_train, _ = train_test_split(
    df['message'], df['label_num'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Function to predict
def predict_spam(msg):
    msg_counts = vectorizer.transform([msg])
    return model.predict(msg_counts)[0]

