import pandas as pd

def process_data(df):
    """
    Centralized function to clean and encode data.
    Ensures consistency between training and prediction.
    """
    # 1. Clean
    df = df.dropna()
    
    # 2. Encode categorical variables
    df = pd.get_dummies(df, drop_first=True)
    
    return df