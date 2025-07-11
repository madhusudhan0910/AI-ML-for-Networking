import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import os
df = pd.read_csv("data/sqlxss_mixed_dataset.csv", usecols=["payload", "label"])
df.dropna(inplace=True)
X = df["payload"]
y = df["label"]  
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_vec, y)
os.makedirs("app", exist_ok=True)
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("app/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
print("✅ Multiclass model trained and saved.")
