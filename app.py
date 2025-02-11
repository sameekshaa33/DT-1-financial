from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        msg = request.form.get("message")  
        print("Received message:", msg)  
    else:
        return render_template("predict.html") # Ensure it returns a response#till now we can get the data from frontend to the backend 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)  # Added debug mode for better error tracking

