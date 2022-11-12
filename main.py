from flask import Flask, request, jsonify
from utility import return_prediction, svc_scaler, svc_pickle_model

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'


@app.route('/prediction', methods=['POST'])
def predict_flower():
    # RECEIVE THE REQUEST
    content = request.json

    # PRINT THE DATA PRESENT IN THE REQUEST
    print("[INFO] Request: ", content)

    # PREDICT THE CLASS USING HELPER FUNCTION
    results = return_prediction(model=svc_pickle_model, scaler=svc_scaler, sample_json=content)

    # PRINT THE RESULT
    print("[INFO] Responce: ", results)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(results[0])


if __name__ == '__main__':
    app.run()
