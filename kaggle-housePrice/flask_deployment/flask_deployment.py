from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

 
# Inisialisasi aplikasi Flask
app = Flask(__name__)
 
# Memuat model yang telah disimpan
joblib_model = joblib.load('kaggle-housePrice/flask_deployment/gbr_model.joblib') # Pastikan path file sesuai dengan penyimpanan Anda
feature_names = joblib.load('kaggle-housePrice/flask_deployment/feature_names.pkl') # Pastikan path file sesuai dengan penyimpanan Anda

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']  # Mengambil data dari request JSON
    # print(f"Type data: {type(data)}")
    # print(f"Length data: {len(data)}")
    # print(f"Isi data: {data[:10]}") #10 pertama

    # # Jika data adalah List of list dengan 1 elemen
    # if len(data) == 1 and isinstance(data[0], list):
    #     features = data[0]
    # else:
    #     features = data

    # print(f"Length features: {len(features)}")


    df_input = pd.DataFrame([data], columns=feature_names)
    # prediction = joblib_model.predict(data)  # Melakukan prediksi (harus dalam bentuk 2D array)
    prediction = joblib_model.predict(df_input)
    return jsonify({'prediction': prediction.tolist()})
 
if __name__ == '__main__':
    app.run(debug=True)
