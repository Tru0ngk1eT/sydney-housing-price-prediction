import streamlit as st, pandas as pd, numpy as np, joblib
from pathlib import Path

b = joblib.load(Path(__file__).parent / "model.joblib")

st.title("Sydney Housing Price Estimator")
st.caption("Cabramatta, Bankstown, Marrickville — trained on 93 sales (2026)")

suburb = st.selectbox("Suburb", ["Cabramatta", "Bankstown", "Marrickville"])
ptype = st.selectbox("Property type", ["house", "duplex", "townhouse", "unit"])
bed = st.number_input("Bedrooms", 1, 6, 2)
bath = st.number_input("Bathrooms", 1, 5, 1)
car = st.number_input("Car spaces", 0, 6, 1)
strata = ptype in ["unit", "townhouse"]
land = 0 if strata else st.number_input("Land size (m²)", 100, 1300, int(b["house_land"]))

if st.button("Predict price"):
    row = pd.DataFrame([dict.fromkeys(b["columns"], 0)])
    row[["bedrooms", "bathrooms", "car_spaces", "land", "is_strata"]] = [bed, bath, car, land, int(strata)]
    if "suburb_" + suburb in row:
        row["suburb_" + suburb] = 1
    price = np.exp(b["model"].predict(row)[0])
    st.metric("Estimated sale price", f"${price:,.0f}")
    st.caption("Indicative only: condition, renovation and views are not included.")