from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

encoder_path = BASE_DIR / "saved_models" / "encoders"

encoders = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "NAME_INCOME_TYPE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_HOUSING_TYPE",
    "OCCUPATION_TYPE"
]

print("=" * 70)
print("ENCODER VALUES")
print("=" * 70)

for name in encoders:

    encoder = joblib.load(
        encoder_path / f"{name}_encoder.pkl"
    )

    print(f"\n{name}")

    print("-" * 50)

    print(list(encoder.classes_))