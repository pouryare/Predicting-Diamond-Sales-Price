from flask import Flask, render_template, request, jsonify
from model.model import predict_price, model_features, numeric_features

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = {}
        for feature in model_features:
            if feature in numeric_features:
                input_data[feature] = float(request.form.get(feature, 0))
            else:
                input_data[feature] = request.form.get(feature, "Unknown")

        predicted_price = predict_price(input_data)
        return jsonify({'predicted_price': float(predicted_price)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)