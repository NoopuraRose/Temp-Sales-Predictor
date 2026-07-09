import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = joblib.load("temp_sales_predictor_linreg.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    temp = float(data["temp"])

    prediction = model.predict([[temp]])

    return jsonify({
        "sales": round(float(prediction[0][0]),2)
    })


if __name__ == "__main__":
    app.run(debug=True)