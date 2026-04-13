import pickle
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "models", "claim_model_3.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def normalize(x, max_val=10):
    return min(x / max_val, 1)


def predict_claim(exclusions, conditions, covered, waiting_period, claim_type):
    # ✅ Proper DataFrame with feature names
    data = pd.DataFrame([{
        "exclusions": normalize(exclusions),
        "conditions": normalize(conditions),
        "covered": covered,
        "waiting_period": waiting_period,
        "claim_type": claim_type
    }])

    prob = model.predict_proba(data)[0][1]
    percentage = int(prob * 100)

    if percentage > 75:
        decision = "Likely Approved"
    elif percentage > 45:
        decision = "Uncertain"
    else:
        decision = "Likely Rejected"

    return percentage, decision


def explain_factors(exclusions, conditions, covered, waiting_period):
    reasons = []

    if exclusions > 3:
        reasons.append("High number of exclusions")
    if conditions > 2:
        reasons.append("Many conditions applied")
    if waiting_period:
        reasons.append("Waiting period restriction")
    if covered:
        reasons.append("Scenario matches policy coverage")

    return reasons