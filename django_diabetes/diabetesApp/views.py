from django.shortcuts import render
from joblib import load

# Load model once at the start
model = load('./simpan_model/model_pipeline.joblib')

# Create your views here.

def index(request):
    return render(request, 'main.html')

def forminfo(request):
    # Ambil data dari request GET
    a = float(request.GET['Pregnancies'])
    b = float(request.GET['Glucose'])
    c = float(request.GET['BloodPressure'])
    d = float(request.GET['SkinThickness'])
    e = float(request.GET['Insulin'])
    f = float(request.GET['BMI'])
    g = float(request.GET['DiabetesPedigreeFunction'])
    h = float(request.GET['Age'])

    # Prediksi menggunakan model
    y_pred = model.predict([[a, b, c, d, e, f, g, h]])

    # Kirim hasil prediksi ke template
    return render(request, 'result.html', {'prediction': y_pred[0]})
