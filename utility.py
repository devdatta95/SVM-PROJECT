import numpy as np
from config import *
import pickle
import joblib


def return_prediction(model, scaler, sample_json):
    # For larger data features, you should probably write a for loop
    # That builds out this array for you

    gen = sample_json['Gender']
    mar = sample_json['Married']
    dep = sample_json['Dependents']
    edu = sample_json['Education']
    sle = sample_json['Self_Employed']
    api = sample_json['ApplicantIncome']
    cpi = sample_json['CoapplicantIncome']
    lam = sample_json['LoanAmount']
    lat = sample_json['Loan_Amount_Term']
    crh = sample_json['Credit_History']
    pra = sample_json['Property_Area']

    person = [[gen, mar, dep, edu, sle, api, cpi, lam, lat, crh, pra]]

    person = scaler.transform(person)

    classes = np.array(['Not-Eligible:- 0', 'Eligible:- 1'])

    class_ind = model.predict(person)

    return classes[class_ind]


# REMEMBER TO LOAD THE MODEL AND THE SCALER!

# LOAD THE SVC MODEL
with open(MODEL_OBJECT, 'rb') as file2:
    svc_pickle_model = pickle.load(file2)

# LOAD THE SCLAER OBJECT
svc_scaler = joblib.load(SCALER_OBJECT)
