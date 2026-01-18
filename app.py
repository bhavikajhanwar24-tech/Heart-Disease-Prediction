from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained pipeline model
with open("heart_disease_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = {
        'age': int(request.form['age']),
        'sex': request.form['sex'],
        'chest_pain_type': request.form['chest_pain_type'],
        'resting_blood_pressure': int(request.form['bp']),
        'cholesterol': int(request.form['chol']),
        'fasting_blood_sugar': request.form['fbs'],
        'resting_electrocardiogram': request.form['ecg'],
        'max_heart_rate_achieved': int(request.form['thalach']),
        'exercise_induced_angina': request.form['exang'],
        'st_depression': float(request.form['oldpeak']),
        'st_slope': request.form['slope'],
        'num_major_vessels': int(request.form['ca']),
        'thalassemia': request.form['thal']
    }

    df = pd.DataFrame([data])

    prob = model.predict_proba(df)[0][1]
    prediction = 1 if prob >= 0.4 else 0

    return render_template(
        "index.html",
        prediction=prediction,
        probability=round(prob, 3)
    )

if __name__ == "__main__":
    app.run(debug=True)
