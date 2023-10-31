from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("C:/Users/aadhi/PROJECT/model_dt.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        industrial_risk= request.form.get("industrial_risk")
        management_risk= request.form.get("management_risk")
        financial_flexibility= request.form.get("financial_flexibility")
        credibility = request.form.get("credibility")
        competitiveness= request.form.get("competitiveness")
        operating_risk= request.form.get("operating_risk")
        result=model.predict([[industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk]])
        print(result)
        if result[0] != [1]:
            prediction ='BANKRUPTCY'
        else:
            prediction ='NON BANKRUPTCY'
        return prediction
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)