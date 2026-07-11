# ==========================================================
# CREDITWISE AI
# Credit Card Approval Prediction System
# Flask Backend
# ==========================================================

from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path

# ==========================================================
# INITIALIZE FLASK
# ==========================================================

app = Flask(__name__)

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "saved_models" / "best_model.pkl"

FEATURE_PATH = BASE_DIR / "saved_models" / "feature_columns.pkl"

ENCODER_FOLDER = BASE_DIR / "saved_models" / "encoders"

# ==========================================================
# LOAD MODEL
# ==========================================================

print("=" * 60)
print("Loading Machine Learning Model...")
print("=" * 60)

model = joblib.load(MODEL_PATH)

print("✓ Model Loaded Successfully")

# ==========================================================
# LOAD FEATURE ORDER
# ==========================================================

feature_columns = joblib.load(FEATURE_PATH)

print("✓ Feature Columns Loaded")

# ==========================================================
# LOAD ALL LABEL ENCODERS
# ==========================================================

encoders = {}

encoder_names = [

    "CODE_GENDER",

    "FLAG_OWN_CAR",

    "FLAG_OWN_REALTY",

    "NAME_INCOME_TYPE",

    "NAME_EDUCATION_TYPE",

    "NAME_FAMILY_STATUS",

    "NAME_HOUSING_TYPE",

    "OCCUPATION_TYPE"

]

for encoder in encoder_names:

    encoders[encoder] = joblib.load(

        ENCODER_FOLDER / f"{encoder}_encoder.pkl"

    )

print("✓ Label Encoders Loaded")

print("=" * 60)

# ==========================================================
# HOME PAGE
# ==========================================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================================
# HELPER FUNCTION
# Convert Form Data into DataFrame
# ==========================================================

def prepare_input(form_data):

    data = {}

    # -------------------------------
    # Encode Categorical Variables
    # -------------------------------

    data["CODE_GENDER"] = encoders["CODE_GENDER"].transform(

        [form_data["CODE_GENDER"]]

    )[0]

    data["FLAG_OWN_CAR"] = encoders["FLAG_OWN_CAR"].transform(

        [form_data["FLAG_OWN_CAR"]]

    )[0]

    data["FLAG_OWN_REALTY"] = encoders["FLAG_OWN_REALTY"].transform(

        [form_data["FLAG_OWN_REALTY"]]

    )[0]

    data["NAME_INCOME_TYPE"] = encoders["NAME_INCOME_TYPE"].transform(

        [form_data["NAME_INCOME_TYPE"]]

    )[0]

    data["NAME_EDUCATION_TYPE"] = encoders["NAME_EDUCATION_TYPE"].transform(

        [form_data["NAME_EDUCATION_TYPE"]]

    )[0]

    data["NAME_FAMILY_STATUS"] = encoders["NAME_FAMILY_STATUS"].transform(

        [form_data["NAME_FAMILY_STATUS"]]

    )[0]

    data["NAME_HOUSING_TYPE"] = encoders["NAME_HOUSING_TYPE"].transform(

        [form_data["NAME_HOUSING_TYPE"]]

    )[0]

    data["OCCUPATION_TYPE"] = encoders["OCCUPATION_TYPE"].transform(

        [form_data["OCCUPATION_TYPE"]]

    )[0]

    # -------------------------------
    # Numerical Variables
    # -------------------------------

    data["CNT_CHILDREN"] = int(form_data["CNT_CHILDREN"])

    data["AMT_INCOME_TOTAL"] = float(form_data["AMT_INCOME_TOTAL"])

    data["FLAG_MOBIL"] = 1

    data["FLAG_WORK_PHONE"] = int(form_data["FLAG_WORK_PHONE"])

    data["FLAG_PHONE"] = int(form_data["FLAG_PHONE"])

    data["FLAG_EMAIL"] = int(form_data["FLAG_EMAIL"])

    data["CNT_FAM_MEMBERS"] = float(form_data["CNT_FAM_MEMBERS"])

    data["AGE"] = int(form_data["AGE"])

    data["EMPLOYMENT_YEARS"] = int(form_data["EMPLOYMENT_YEARS"])

    # -------------------------------
    # DataFrame
    # -------------------------------

    input_df = pd.DataFrame([data])

    input_df = input_df[feature_columns]

    return input_df
# ==========================================================
# PREDICTION ROUTE
# ==========================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # ---------------------------------------
        # Convert HTML Form Data
        # ---------------------------------------

        input_df = prepare_input(request.form)

        # ---------------------------------------
        # Predict
        # ---------------------------------------

        prediction = model.predict(input_df)[0]

        probability = model.predict_proba(input_df)[0]

        confidence = round(max(probability) * 100, 2)

        # ---------------------------------------
        # Prediction Result
        # ---------------------------------------

        if prediction == 0:

            prediction_text = "Credit Approved"

            result_color = "#16a34a"

            result_icon = "✅"

            risk = "Low Risk"

            recommendation = (
                "The applicant has a strong financial profile. "
                "Based on the information provided, the model predicts "
                "a high likelihood of credit card approval."
            )

        else:

            prediction_text = "Credit Rejected"

            result_color = "#dc2626"

            result_icon = "❌"

            risk = "High Risk"

            recommendation = (
                "The model predicts a higher credit risk based on "
                "the submitted information. Improving financial "
                "stability and credit history may increase the "
                "likelihood of approval."
            )

        # ---------------------------------------
        # Render Result Page
        # ---------------------------------------

        return render_template(

            "result.html",

            prediction=prediction_text,

            confidence=confidence,

            color=result_color,

            icon=result_icon,

            risk=risk,

            recommendation=recommendation

        )

    except Exception as e:

        return render_template(

            "result.html",

            prediction="Prediction Failed",

            confidence=0,

            color="#dc2626",

            icon="⚠️",

            risk="Unknown",

            recommendation=str(e)

        )


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("CreditWise AI Server Started")
    print("Open Browser : http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )