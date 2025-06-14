from flask import Flask, render_template, request
import numpy as np
import pickle


model = pickle.load(open('model.pkl', 'rb'))
X_columns = pickle.load(open('X_columns.pkl', 'rb'))

app = Flask(__name__)


locations = [col for col in X_columns if col not in ['bath', 'balcony', 'bhk', 'new_total_sqft']]

@app.route('/')
def home():
    return render_template('index.html', columns=X_columns, locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    sqft = float(request.form['sqft'])
    area_type = request.form['area_type']
    availability = request.form['availability']


    x = np.zeros(len(X_columns))


    if 'bath' in X_columns:
        x[X_columns.get_loc('bath')] = bath
    if 'balcony' in X_columns:
        x[X_columns.get_loc('balcony')] = balcony
    if 'bhk' in X_columns:
        x[X_columns.get_loc('bhk')] = bhk
    if 'new_total_sqft' in X_columns:
        x[X_columns.get_loc('new_total_sqft')] = sqft


    if location in X_columns:
        x[X_columns.get_loc(location)] = 1
    if area_type in X_columns:
        x[X_columns.get_loc(area_type)] = 1
    if availability in X_columns:
        x[X_columns.get_loc(availability)] = 1

    predicted_price = model.predict([x])[0]
    predicted_price_lakhs = predicted_price / 1e5

    return render_template(
        'index.html',
        prediction_text=f"Estimated Price: ₹{predicted_price:,.2f} Lakhs",
        locations=[col for col in X_columns if col not in ['bath', 'balcony', 'bhk', 'new_total_sqft']]
    )


if __name__ == "__main__":
    app.run(debug=True)
