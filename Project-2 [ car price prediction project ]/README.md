
##  Car Price Prediction App

A machine learning web application built with **Flask** to predict the price of a used car in Indian Rupees (₹).  
Enter car details like name, year, mileage, fuel type, etc., and get an instant price prediction!

---

##  Table of Contents

* [About](#about)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [How it Works](#how-it-works)
* [Folder Structure](#folder-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Example Prediction](#example-prediction)
* [Future Improvements](#future-improvements)
* [License](#license)
* [Author](#author)

---

##  About

This project demonstrates:

✅ End-to-end machine learning pipeline  
✅ Data preprocessing & feature engineering  
✅ Model training & saving with `joblib`  
✅ Deployment as a Flask web application

It predicts the selling price (in lakhs) based on car attributes like:

* Car Name
* Year of manufacture
* Total kilometers driven
* Fuel type

---

##  Features

* Simple and clean HTML frontend (`index.html`)
* Takes car details as input
* Uses a trained **Random Forest model** (`rf_model.pkl`)
* Reuses the **same preprocessor** (`preprocessor.pkl`) used during training
* Displays predicted price instantly in rupees (₹)

---

##  Tech Stack

* Python 
* Flask 
* Pandas, NumPy
* Scikit-learn (Random Forest)
* joblib
* HTML & CSS

---

##  How it Works

1. User enters car details in the form
2. Data converted into a DataFrame
3. Loaded `preprocessor.pkl` transforms the data
4. Transformed data passed to `rf_model.pkl`
5. Model predicts the price
6. Predicted price displayed instantly on the web page

All of this happens in real-time when the user clicks **Predict**!

---

##  Folder Structure

```

car-price-predictor/
├── .venv/                    # Virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
├── data/
│   └── car_data.csv          # Dataset
├── models/
│   ├── preprocessor.pkl      # Saved preprocessor
│   └── rf_model.pkl         # Trained Random Forest model
├── src/                      # Source code
│   ├── init.py
│   ├── app.py               # Flask app
│   ├── data_processing.py   # Data preprocessing
│   └── model_training.py    # Model training script
├── templates/
│   └── index.html           # Frontend HTML page
├── image.png                # Example prediction image or visualization
├── README.md
└── requirements.txt

````

## 💻 Installation

Follow these steps to set up the project locally:


**Create a virtual environment (recommended)**

```bash
python -m venv .venv
```

Activate it:

* On Windows:

  ```bash
  .venv\Scripts\activate
  ```
* On macOS/Linux:

  ```bash
  source .venv/bin/activate
  ```

**Install the dependencies**

```bash
pip install -r requirements.txt
```

**Ensure required model files are present:**

* `models/rf_model.pkl`
* `models/preprocessor.pkl`

> *If these files are missing, train the model first and save them.*

---

## Usage

Run the Flask app (from inside `src` folder if needed):

```bash
python src/app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000/
```

Fill in the car details → click **Predict** → see the predicted price!

---

##  Example Prediction

* Car Name: `Honda City`
* Year: `2016`
* Mileage (kms): `50000`
* Fuel Type: `Petrol`

**Predicted Price:** `₹8.75 Lakhs`
*(Actual result may vary depending on your model)*

---

## License

This project is open source under the **MIT License**.

---

##  Author

Built with ❤️ by **Siddique Mohammad Aham**

---

```
