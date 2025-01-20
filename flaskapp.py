from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

app = Flask(__name__,template_folder='templates')

# Home route
@app.route('/')
def home():
    return render_template('index.html', companies=df['Company'].unique(),
                           types=df['TypeName'].unique(),
                           cpus=df['Cpu brand'].unique(),
                           gpus=df['Gpu brand'].unique(),
                           oss=df['os'].unique())

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get user input
    company = request.form['company']
    type = request.form['type']
    ram = int(request.form['ram'])
    weight = float(request.form['weight'])
    touchscreen = 1 if request.form['touchscreen'] == 'Yes' else 0
    ips = 1 if request.form['ips'] == 'Yes' else 0
    screen_size = float(request.form['screen_size'])
    resolution = request.form['resolution']
    cpu = request.form['cpu']
    hdd = int(request.form['hdd'])
    ssd = int(request.form['ssd'])
    gpu = request.form['gpu']
    os = request.form['os']

    # Process resolution and calculate PPI
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Convert all string inputs to ASCII to avoid Unicode issues
    company = company.encode('ascii', 'ignore').decode()
    type = type.encode('ascii', 'ignore').decode()
    cpu = cpu.encode('ascii', 'ignore').decode()
    gpu = gpu.encode('ascii', 'ignore').decode()
    os = os.encode('ascii', 'ignore').decode()

    # Create query array
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]).reshape(1, 12)

    # Make prediction
    predicted_price = round(np.exp(pipe.predict(query)[0]),2)

    return render_template('result.html', price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
