from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')  # Load your pre-trained model here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['time'],
        data['acc_front'],
        data['acc_vert'],
        data['acc_lat'],
        data['sensor_id'],
        data['rssi'],
        data['phase'],
        data['frequency']
    ]
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    activity_map = {1: "sit on bed", 2: "sit on chair", 3: "lying", 4: "ambulating"}
    result = {"activity": activity_map[prediction]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
