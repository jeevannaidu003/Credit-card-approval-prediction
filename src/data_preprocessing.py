# ============================================================
# CREDIT CARD APPROVAL PREDICTION
# DATA PREPROCESSING
# ============================================================

import pandas as pd
import numpy as np
import joblib
from pathlib import Path

from sklearn.preprocessing import LabelEncoder

print("=" * 70)
print("CREDIT CARD APPROVAL PREDICTION")
print("DATA PREPROCESSING")
print("=" * 70)

# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# LOAD DATASETS
# ============================================================

application = pd.read_csv(BASE_DIR / "dataset" / "application_record.csv")
credit = pd.read_csv(BASE_DIR / "dataset" / "credit_record.csv")

print("\nDatasets Loaded Successfully!")

# ============================================================
# REMOVE DUPLICATES
# ============================================================

application.drop_duplicates(inplace=True)
credit.drop_duplicates(inplace=True)

print("\nDuplicates Removed")

# ============================================================
# HANDLE MISSING VALUES
# ============================================================

application["OCCUPATION_TYPE"] = application["OCCUPATION_TYPE"].fillna("Unknown")

print("\nMissing Values Handled")

# ============================================================
# CREATE TARGET VARIABLE
# ============================================================

status_map = {
    "X": 0,
    "C": 0,
    "0": 0,
    "1": 1,
    "2": 1,
    "3": 1,
    "4": 1,
    "5": 1
}

credit["STATUS"] = credit["STATUS"].replace(status_map)
credit["STATUS"] = credit["STATUS"].astype(int)

credit = (
    credit
    .groupby("ID")["STATUS"]
    .max()
    .reset_index()
)

credit.rename(columns={"STATUS": "TARGET"}, inplace=True)

print("\nTarget Variable Created")

# ============================================================
# MERGE DATASETS
# ============================================================

df = application.merge(credit, on="ID", how="inner")

print("\nDatasets Merged")

# ============================================================
# FEATURE ENGINEERING
# ============================================================

df["AGE"] = (-df["DAYS_BIRTH"]) // 365

df["EMPLOYMENT_YEARS"] = np.where(
    df["DAYS_EMPLOYED"] < 0,
    (-df["DAYS_EMPLOYED"]) // 365,
    0
)

# ============================================================
# DROP UNUSED COLUMNS
# ============================================================

df.drop(
    columns=[
        "ID",
        "DAYS_BIRTH",
        "DAYS_EMPLOYED"
    ],
    inplace=True
)

# ============================================================
# LABEL ENCODING
# ============================================================

print("\nEncoding Categorical Columns...")

encoder_folder = BASE_DIR / "saved_models" / "encoders"
encoder_folder.mkdir(parents=True, exist_ok=True)

categorical_columns = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "OCCUPATION_TYPE"
]

encoders = {}

for column in categorical_columns:

    le = LabelEncoder()

    df[column] = le.fit_transform(df[column])

    encoders[column] = le

    joblib.dump(
        le,
        encoder_folder / f"{column}_encoder.pkl"
    )

print("Encoders Saved Successfully!")

# ============================================================
# SAVE FEATURE ORDER
# ============================================================

feature_columns = df.drop(columns=["TARGET"]).columns.tolist()

joblib.dump(
    feature_columns,
    BASE_DIR / "saved_models" / "feature_columns.pkl"
)

print("Feature Order Saved!")

# ============================================================
# SAVE FINAL DATASET
# ============================================================

df.to_csv(
    BASE_DIR / "dataset" / "final_credit_card_dataset.csv",
    index=False
)

print("\nFinal Dataset Saved!")

# ============================================================
# DATASET INFO
# ============================================================

print("\nShape :", df.shape)

print("\nTarget Distribution")

print(df["TARGET"].value_counts())

print("\nColumns")

print(df.columns.tolist())

# ============================================================
# COMPLETED
# ============================================================

print("\n" + "=" * 70)
print("EPIC 3 COMPLETED SUCCESSFULLY")
print("=" * 70)