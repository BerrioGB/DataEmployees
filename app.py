from flask import Flask, request, jsonify
#import obtener_TI from querys
import numpy as np

app = Flask(__name__)

# Initialize the API
#estimation_api = url base se datos()

@app.route('/empleados/ti')
def home():
    result = obtener_TI(URL)
    return {'home':'OK', 'model_version':"1.0.0"}

@app.route('/predict', methods=['POST'])
def predict():
    

#if __name__ == '__main__':
    app.run(port=4000, debug=True)