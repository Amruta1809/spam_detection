from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)  # Allow CORS for frontend-backend communication

# Load the trained model
model = joblib.load('spam_detector.pkl')

@app.route('/')
def serve_index():
    """Serve the main HTML file."""
    return send_from_directory('static', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to predict spam."""
    try:
        data = request.get_json()
        if 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        message = data['message']
        prediction = model.predict([message])[0]
        result = 'Spam' if prediction == 1 else 'Ham'
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
