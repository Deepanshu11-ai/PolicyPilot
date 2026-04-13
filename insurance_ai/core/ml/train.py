import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

BASE_DIR = os.path.dirname(__file__)

data_path = os.path.join(BASE_DIR, "data", "claims_dataset.csv")
model_path = os.path.join(BASE_DIR, "models", "claim_model_3.pkl")

df = pd.read_csv(data_path)

X = df[["exclusions", "conditions", "covered", "waiting_period", "claim_type"]]
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

os.makedirs(os.path.dirname(model_path), exist_ok=True)

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained & saved")