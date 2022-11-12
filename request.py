import requests
import json

url = "http://127.0.0.1:5000/prediction"

payload = json.dumps({
  "Gender": 6.546546546546547e+26,
  "Married": 0,
  "Dependents": 0,
  "Education": 0,
  "Self_Employed": 0,
  "ApplicantIncome": 5849,
  "CoapplicantIncome": 0,
  "LoanAmount": 146,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
