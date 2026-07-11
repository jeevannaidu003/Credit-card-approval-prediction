import pandas as pd
import joblib
from pathlib import Path

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "dataset" / "final_credit_card_dataset.csv")

X = df.drop("TARGET", axis=1)
y = df["TARGET"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("="*60)
print("DECISION TREE")
print("="*60)

print("Accuracy :", accuracy_score(y_test, pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred))
print("\nClassification Report")
print(classification_report(y_test, pred))

joblib.dump(model, BASE_DIR / "saved_models" / "decision_tree.pkl")

print("\nModel Saved Successfully!")