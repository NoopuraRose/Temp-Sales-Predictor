import joblib
from flask import Flask,request

app = Flask(__name__)
model = joblib.load("temp_sales_predictor_linreg.pkl")

@app.route("/test", methods = ["GET"])
def test():
    return "hello"

@app.route("/user", methods = ["POST"])
def user():
    input = request.get_json()
    print(input)
    temp = input.get("temp")
    print(temp)
    new_sales = model.predict([[temp]])
    print("Predicted sales = ", new_sales[0][0])
    return {"sales": new_sales[0][0]}
    
if __name__ == "__main__":
    app.run()