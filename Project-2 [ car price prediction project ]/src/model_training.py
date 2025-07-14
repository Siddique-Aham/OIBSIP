import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt
from data_processing import load_data, preprocess_data
import os

def train_model():
    # Define correct file path (relative to src folder)
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'car_data.csv')
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        print(f"Current working directory: {os.getcwd()}")
        print("Please ensure the 'car_data.csv' file is in the 'data' folder at the project root.")
        return
    
    # Load data
    try:
        data = load_data(file_path)
        print("Data loaded successfully. First 5 rows:")
        print(data.head())
    except Exception as e:
        print(f"Error loading data: {e}")
        return
    
    # Preprocess with consistent column order
    try:
        # Define and maintain consistent feature columns based on actual data
        feature_cols = ['Car_Name', 'Year', 'Driven_kms', 'Fuel_Type', 'Selling_type', 'Transmission', 'Owner']
        target_col = 'price'
        
        # Verify all required columns exist
        missing_cols = [col for col in feature_cols + [target_col] if col not in data.columns]
        if missing_cols:
            raise ValueError(f"Missing columns in data: {missing_cols}\nAvailable columns: {data.columns.tolist()}")
        
        # Create feature matrix and target vector
        X = data[feature_cols]
        y = data[target_col]
        
        # Combine features and target for preprocessing
        data_for_preprocessing = pd.concat([X, y], axis=1)
        
        # Preprocess data
        X_processed, y, preprocessor = preprocess_data(data_for_preprocessing, is_training=True)
        
        print(f"\nPreprocessing completed. Features shape: {X_processed.shape}")
    except Exception as e:
        print(f"\nError preprocessing data: {e}")
        print("Available columns in data:", data.columns.tolist())
        return
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_processed, y, test_size=0.2, random_state=42
    )
    print(f"\nData split into train/test: {X_train.shape[0]}/{X_test.shape[0]} samples")
    
    # Train model
    print("\nTraining Random Forest model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'\nModel Evaluation:')
    print(f'Mean Squared Error: {mse:.2f}')
    print(f'R2 Score: {r2:.2f}')
    
    # Visualize
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Price')
    plt.ylabel('Predicted Price')
    plt.title('Actual vs Predicted Car Prices')
    plt.show()
    
    # Save model and preprocessor
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    model_path = os.path.join(models_dir, 'rf_model.pkl')
    preprocessor_path = os.path.join(models_dir, 'preprocessor.pkl')
    
    joblib.dump(model, model_path)
    joblib.dump(preprocessor, preprocessor_path)
    print(f"\nModel and preprocessor saved to:")
    print(f"- Model: {model_path}")
    print(f"- Preprocessor: {preprocessor_path}")

if __name__ == '__main__':
    train_model()