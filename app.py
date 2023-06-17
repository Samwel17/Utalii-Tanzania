from flask import Flask, render_template, request
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier
from sklearn.preprocessing import OneHotEncoder


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Load the trained model
    model = joblib.load("models/lightgbm_model_all.pkl")


    # Preprocessing function
    def preprocess_data(data):

    # Load the necessary preprocessing components
        onehotencoder = joblib.load("models/one-hot-encoder_all.pkl")
        scaler = joblib.load("models/scaler_all.pkl")
    
    # Separate continuous and categorical features
        continuous_features = data[["Tzmainland", "Zanzibar", "total_number", "int_transport", "accomodation", "food", "local_transport", "sightseeing", "tour_guide", "insurance", "first_trip"]]
        categorical_features = data[['country','age_group','tour_arrangement','travel_with','purpose','main_activity','payment_mode']]

    # Preprocess categorical 
        categorical_data = onehotencoder.transform(categorical_features)
        
        continuous_features = continuous_features.to_numpy()

    # Combine the preprocessed features
        preprocessed_data = np.concatenate((continuous_features, categorical_data), axis=1)

        preprocessed_data = scaler.transform(preprocessed_data)
  
        return preprocessed_data

    # extract the input
    country = request.form.get("country")
    age_group = request.form.get("age_group")
    travel_with = request.form.get("travel_with")
    purpose = request.form.get("purpose")
    total_number = request.form.get("total_number")
    main_activity = request.form.get("main_activity")
    tour_arrangement = request.form.get("tour_arrangement")
    payment_mode = request.form.get("payment_mode")
    Tzmainland = request.form.get("Tzmainland")
    Zanzibar = request.form.get("Zanzibar")
    int_transport = request.form.get("int_transport")
    accomodation = request.form.get("accomodation")
    food = request.form.get("food")
    local_transport = request.form.get("local_transport")
    sightseeing = request.form.get("sightseeing")
    tour_guide = request.form.get("tour_guide")
    insurance = request.form.get("insurance")
    first_trip = request.form.get("first_trip")

    # process the input
    data = pd.DataFrame({
        "country": [country],
        "age_group": [age_group],
        "travel_with": [travel_with],
        "purpose": [purpose],
        "total_number": [total_number],
        "main_activity": [main_activity],
        "tour_arrangement": [tour_arrangement],
        "payment_mode": [payment_mode],
        "Tzmainland": [Tzmainland],
        "Zanzibar": [Zanzibar],
        "int_transport": [int_transport],
        "accomodation": [accomodation],
        "food": [food],
        "local_transport": [local_transport],
        "sightseeing": [sightseeing],
        "tour_guide": [tour_guide],
        "insurance": [insurance],
        "first_trip": [first_trip]
    })

    # result dictionary
    result_dic = {
    1: " from Tsh 0 to Tsh 500,000",
    2: "from Tsh 500,000 to Tsh 1,000,000",
    3: "from Tsh 1,000,000 to Tsh 5,000,000",
    4: "from Tsh 5,000,000 to Tsh 10,000,000",
    5: "from Tsh 10,000,000 and above",
}

    # Preprocess the input data
    preprocessed_data = preprocess_data(data)

  
    # Make the prediction
    prediction = model.predict(preprocessed_data)
    
    prediction = int(prediction)

    return render_template("result.html", prediction=result_dic[prediction])


if __name__ == "__main__":
    app.run(debug=True)
