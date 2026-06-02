import pandas as pd
import re
import string
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("spam.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Keep required columns
df = df[['email', 'label']]

# Remove null values
df.dropna(inplace=True)

# Convert to string
df['email'] = df['email'].astype(str)

# ==========================
# TEXT CLEANING
# ==========================

def clean_text(text):
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    # Remove extra spaces
    text = " ".join(text.split())

    return text

df['email'] = df['email'].apply(clean_text)

# ==========================
# FEATURES AND LABELS
# ==========================

X = df['email']
y = df['label']

# ==========================
# TF-IDF VECTORIZER
# ==========================

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)

X = vectorizer.fit_transform(X)

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# LOGISTIC REGRESSION
# ==========================

print("\nTraining Logistic Regression...")

logistic_model = LogisticRegression(
    max_iter=1000
)

logistic_model.fit(
    X_train,
    y_train
)

logistic_pred = logistic_model.predict(
    X_test
)

logistic_accuracy = accuracy_score(
    y_test,
    logistic_pred
)

print(
    "Logistic Regression Accuracy:",
    round(logistic_accuracy * 100, 2),
    "%"
)

# ==========================
# RANDOM FOREST
# ==========================

print("\nTraining Random Forest...")

random_forest_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

random_forest_model.fit(
    X_train,
    y_train
)

rf_pred = random_forest_model.predict(
    X_test
)

rf_accuracy = accuracy_score(
    y_test,
    rf_pred
)

print(
    "Random Forest Accuracy:",
    round(rf_accuracy * 100, 2),
    "%"
)

# ==========================
# BEST MODEL
# ==========================

if logistic_accuracy > rf_accuracy:
    best_model = logistic_model
    best_name = "Logistic Regression"
else:
    best_model = random_forest_model
    best_name = "Random Forest"

print("\nBest Model:", best_name)

# ==========================
# SAVE FILES
# ==========================

joblib.dump(
    vectorizer,
    "vectorizer.pkl"
)

joblib.dump(
    logistic_model,
    "logistic_regression.pkl"
)

joblib.dump(
    random_forest_model,
    "random_forest.pkl"
)

joblib.dump(
    best_model,
    "best_model.pkl"
)

print("\nFiles Saved Successfully!")

print("vectorizer.pkl")
print("logistic_regression.pkl")
print("random_forest.pkl")
print("best_model.pkl")

# ==========================
# TEST PREDICTION
# ==========================

sample_email = [
    "Congratulations! You have won a free iPhone. Click here now."
]

sample_vector = vectorizer.transform(
    sample_email
)

prediction = best_model.predict(
    sample_vector
)

probability = best_model.predict_proba(
    sample_vector
)

print("\nSample Email Test")

print(
    "Prediction:",
    "Spam" if prediction[0] == 1 else "Not Spam"
)

print(
    "Spam Probability:",
    round(probability[0][1] * 100, 2),
    "%"
)