from django.shortcuts import render
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
from .forms import HotspotForm
from django.http import HttpResponse

# Load the model and rules
MODEL_PATH = "myproject/unsupervised_autoencoder_model.h5"
model = load_model(MODEL_PATH)

RULES_PATH = "myproject/association_rules.csv"
rules_df = pd.read_csv(RULES_PATH)

def home(request):
    return HttpResponse("Welcome to the homepage!")

def predict_hotspot(request):
    if request.method == "POST":
        form = HotspotForm(request.POST)
        if form.is_valid():
            # Get form data
            county = form.cleaned_data["county"]
            year = form.cleaned_data["year"]
            sex = form.cleaned_data["sex"]
            population = form.cleaned_data["population"]
            count = form.cleaned_data["count"]

            # Prepare input features
            #input_features = np.array([year, 1 if sex == "M" else 0, population, count]).reshape(1, -1)
            # Adjust the number of features to match the model's expected input shape
            input_features = np.array([year, 1 if sex == "M" else 0, population, count] + [0] * 7).reshape(1, -1)

            print(input_features, "+++++++++++++++++++++++++++++++++++++++++")
            # Predict using the model
            prediction = model.predict(input_features)
            print(prediction, "+++++++++++++++++++++++++++++++++++++++++")
            predicted_rate = prediction[0][0]
            print(predicted_rate, "++++++++++++++++++this is the prediction from model+++++++++++++++++++++++++++++++++")
            # Determine if it's a hotspot
            is_hotspot = predicted_rate > 1.5  # Example threshold

            # Fetch associated diseases
            print("Columns in rules_df:", rules_df.columns)

            # Check if county is in 'antecedents' and extract associated diseases from 'consequents'
            if "antecedents" in rules_df.columns and "consequents" in rules_df.columns:
                associated_diseases = rules_df[rules_df["antecedents"].str.contains(county, na=False)]["consequents"].unique()
            else:
                return HttpResponse("Error: Relevant columns ('antecedents' and 'consequents') are missing.")



            # Prepare context for rendering the result page
            context = {
                "form": form,
                "county": county,
                "year": year,
                "predicted_rate": predicted_rate,
                "is_hotspot": is_hotspot,
                 "associated_diseases": associated_diseases,
            }
            return render(request, "result.html", context)
    else:
        # Render form for GET request
        form = HotspotForm()

    return render(request, "predict.html", {"form": form})

# Define the predict_result view (optional if it's unused)
def predict_result(request):
    return render(request, "result.html")
