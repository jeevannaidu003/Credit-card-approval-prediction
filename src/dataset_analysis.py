# ============================================================
# CREDIT CARD APPROVAL PREDICTION
# Epic 2 : Data Analysis
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

print("=" * 70)
print("CREDIT CARD APPROVAL PREDICTION")
print("DATASET ANALYSIS")
print("=" * 70)

# ============================================================
# LOAD FINAL DATASET
# ============================================================

df = pd.read_csv("dataset/final_credit_card_dataset.csv")

print("\nDataset Loaded Successfully!")

# ============================================================
# STORY 2 : DATASET EXPLORATION
# ============================================================

print("\nFirst 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nInformation")
print(df.info())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

# ============================================================
# STORY 5 : DESCRIPTIVE ANALYSIS
# ============================================================

print("\nStatistical Summary")

print(df.describe())

print("\nTarget Distribution")

print(df["TARGET"].value_counts())

# ============================================================
# STORY 3 : UNIVARIATE ANALYSIS
# ============================================================

# Target Variable

plt.figure(figsize=(6,4))

sns.countplot(data=df,x="TARGET")

plt.title("Target Distribution")

plt.show()

# Gender

plt.figure(figsize=(6,4))

sns.countplot(data=df,x="CODE_GENDER")

plt.title("Gender Distribution")

plt.show()

# Car Ownership

plt.figure(figsize=(6,4))

sns.countplot(data=df,x="FLAG_OWN_CAR")

plt.title("Car Ownership")

plt.show()

# House Ownership

plt.figure(figsize=(6,4))

sns.countplot(data=df,x="FLAG_OWN_REALTY")

plt.title("House Ownership")

plt.show()

# Income

plt.figure(figsize=(10,5))

sns.histplot(df["AMT_INCOME_TOTAL"],bins=50,kde=True)

plt.title("Annual Income Distribution")

plt.show()

# Age

plt.figure(figsize=(10,5))

sns.histplot(df["AGE"],bins=40,kde=True)

plt.title("Age Distribution")

plt.show()

# Employment

plt.figure(figsize=(10,5))

sns.histplot(df["EMPLOYMENT_YEARS"],bins=40,kde=True)

plt.title("Employment Years")

plt.show()

# Family Members

plt.figure(figsize=(8,5))

sns.countplot(data=df,x="CNT_FAM_MEMBERS")

plt.title("Family Members")

plt.show()

# Children

plt.figure(figsize=(8,5))

sns.countplot(data=df,x="CNT_CHILDREN")

plt.title("Children Count")

plt.show()

# ============================================================
# STORY 4 : MULTIVARIATE ANALYSIS
# ============================================================

# Correlation Heatmap

plt.figure(figsize=(16,12))

sns.heatmap(
    df.corr(),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# Income vs Target

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="TARGET",
    y="AMT_INCOME_TOTAL"
)

plt.title("Income vs Target")

plt.show()

# Age vs Target

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="TARGET",
    y="AGE"
)

plt.title("Age vs Target")

plt.show()

# Employment vs Target

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x="TARGET",
    y="EMPLOYMENT_YEARS"
)

plt.title("Employment vs Target")

plt.show()

# Family Members vs Income

plt.figure(figsize=(8,5))

sns.scatterplot(
    data=df,
    x="CNT_FAM_MEMBERS",
    y="AMT_INCOME_TOTAL",
    hue="TARGET"
)

plt.title("Family Members vs Income")

plt.show()

# ============================================================
# END
# ============================================================

print("\n" + "="*70)
print("EPIC 2 COMPLETED SUCCESSFULLY")
print("="*70)