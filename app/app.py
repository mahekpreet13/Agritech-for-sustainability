from flask import Flask, request, jsonify, render_template
from PIL import Image
import io

# Import your dummy predictor function
from ml_model.predictor import predict_disease

# Initialize the Flask application
app = Flask(__name__)

# --- HTML Rendering Route ---
@app.route('/')
def home():
    """Renders the main HTML page."""
    return render_template('index.html')

# --- API Endpoints ---
@app.route('/api/predict', methods=['POST'])
def api_predict():
    """Receives an image and returns a disease prediction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # You can process the image here if needed
        # For now, we'll just pass a placeholder to our dummy function
        # In the future, you'd do: image = Image.open(file.stream)
        
        prediction = predict_disease(image_data=file) # Passing the file object for now
        return jsonify(prediction)

@app.route('/api/weather', methods=['GET'])
def api_weather():
    """Returns mock weather data for the user's location."""
    # In a real app, you would use the location from the request to call a weather API
    # Using Jamshedpur's approximate location for the mock data
    lat = request.args.get('lat', '22.80') 
    lon = request.args.get('lon', '86.20')

    mock_weather = {
        'location': 'Jamshedpur',
        'temperature': '31°C',
        'condition': 'Partly Cloudy',
        'alert': 'High humidity expected. Monitor crops for fungal growth.'
    }
    return jsonify(mock_weather)

@app.route('/api/prices', methods=['GET'])
def api_prices():
    """Returns mock market price data for a given crop."""
    crop = request.args.get('crop', 'default').lower()
    
    # Mock data for demonstration
    market_prices = {
        'tomato': {'price': '₹ 25/kg', 'trend': 'up'},
        'potato': {'price': '₹ 18/kg', 'trend': 'stable'},
        'default': {'price': 'N/A', 'trend': 'N/A'}
    }
    
    price_data = market_prices.get(crop, market_prices['default'])
    return jsonify(price_data)