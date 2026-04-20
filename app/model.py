import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .processor import process_data  
import os

MODEL_PATH = "models/model.pkl"

def train_and_save_model(data_path):
    raw_df = pd.read_csv(data_path)
    
    # USE THE PROCESSOR HERE
    processed_df = process_data(raw_df)
    
    X = processed_df.drop('price', axis=1)
    y = processed_df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Save the model AND the column names to ensure input alignment later
    os.makedirs("models", exist_ok=True)
    joblib.dump((model, X.columns.tolist()), MODEL_PATH)
    return {"r2": model.score(X_test, y_test)}

def predict(input_dict: dict):
    # Load model and the feature list it expects
    model, model_columns = joblib.load(MODEL_PATH)
    
    # Convert input to DataFrame and USE THE PROCESSOR HERE
    input_df = pd.DataFrame([input_dict])
    processed_input = process_data(input_df)
    
    # Align columns: Ensure the input has all columns the model was trained on
    # (Important for categorical variables like 'furnishingstatus')
    for col in model_columns:
        if col not in processed_input.columns:
            processed_input[col] = 0
            
    final_input = processed_input[model_columns] # Reorder to match training
    return model.predict(final_input)[0]