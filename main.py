from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# Get the current directory to serve the HTML file without needing a "templates" folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    """Serves the main admission portal HTML file."""
    return send_from_directory(BASE_DIR, 'admission_portal_simple.html')

@app.route('/submit', methods=['POST'])
def submit_application():
    """
    An example of a Python backend route that could process the form data.
    Right now, the HTML uses JavaScript to handle the form, but this route
    is ready if you want to switch to Python processing!
    """
    data = request.json
    print("Received new application:", data)
    return jsonify({"status": "success", "message": "Application received by Python backend!"})

if __name__ == '__main__':
    print("🎓 Starting Medicaps University Portal...")
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    app.run(debug=True)
