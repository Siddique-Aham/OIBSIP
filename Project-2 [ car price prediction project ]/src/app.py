from flask import Flask, request, render_template
import pandas as pd
import joblib
import os
from data_processing import preprocess_data

app = Flask(__name__, template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates')))

# Load model and preprocessor
try:
    model = joblib.load(os.path.join(os.path.dirname(__file__), '../models/rf_model.pkl'))
    preprocessor = joblib.load(os.path.join(os.path.dirname(__file__), '../models/preprocessor.pkl'))
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    preprocessor = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or preprocessor is None:
        return render_template('index.html', prediction='Model not loaded. Train model first.')
    
    try:
        # Get form data - updated to match Excel columns
        features = {
            'Car_Name': request.form['CarName'],
            'Year': float(request.form['year']),
            'Driven_kms': float(request.form['mileage']),
            'Fuel_Type': request.form['fueltype'],
            'Selling_type': 'Dealer',  # Default value or get from form
            'Transmission': 'Manual',   # Default value or get from form
            'Owner': 0                  # Default value or get from form
        }
        
        # Convert to DataFrame (ensure same column order as training)
        input_data = pd.DataFrame([features], columns=[
            'Car_Name', 'Year', 'Driven_kms', 'Fuel_Type', 
            'Selling_type', 'Transmission', 'Owner'
        ])
        
        # Preprocess using the SAME preprocessor used in training
        input_processed, _ = preprocess_data(input_data, is_training=False, preprocessor=preprocessor)
        
        # Make prediction
        prediction = model.predict(input_processed)[0]
        return render_template('index.html', prediction=f'Predicted Price: ₹{prediction:.2f} Lakhs')  # Changed to ₹ for Indian rupees
    
    except Exception as e:
        return render_template('index.html', prediction=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)