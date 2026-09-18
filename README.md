# Sydney Housing Price Prediction and Decision Support System

SIT (Deakin) 8.1D Mini Project. Predicts sale prices for properties in Cabramatta,
Bankstown and Marrickville using 93 sold listings from realestate.com.au (March–September 2026).

## Files
- `sydney_housing.csv` – collected dataset (93 sold properties, 31 per suburb)
- `8.1D.ipynb` – data cleaning, EDA, feature engineering, model training and evaluation
- `app.py` – Streamlit web app for price prediction
- `model.joblib` – trained Linear Regression model used by the app
- `requirements.txt` – Python packages

## How to run
1. Install packages: `pip install -r requirements.txt`
2. Run `8.1D.ipynb` from top to bottom (this recreates `model.joblib`)
3. Start the app: `streamlit run app.py`
4. Open http://localhost:8501, enter the property details and click **Predict price**
