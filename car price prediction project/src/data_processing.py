import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
import os

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def preprocess_data(data, is_training=True, preprocessor=None):
    """
    Preprocess data: handle missing values and encode features.
    Returns preprocessed data, target (if training), and preprocessor.
    """
    data = data.dropna()
    
    if is_training:
        X = data.drop('price', axis=1)
        y = data['price']
        
        # Identify feature types
        categorical_cols = X.select_dtypes(include=['object']).columns
        numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
        
        # Create preprocessor
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_cols),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
            ])
        
        # Fit and transform
        X_processed = preprocessor.fit_transform(X)
        return X_processed, y, preprocessor
    else:
        if preprocessor is None:
            raise ValueError("Preprocessor must be provided for prediction")
        
        # Transform using the existing preprocessor
        data_processed = preprocessor.transform(data)
        return data_processed, None