# backend/app.py
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend/backend communication

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["service_aggregator_db"]

# Test route
@app.route("/")
def home():
    return {"message": "API is running!"}

# Import and register blueprints (will build these next)
# from routes.auth_routes import auth_bp
# from routes.service_routes import service_bp
# from routes.ai_routes import ai_bp
# app.register_blueprint(auth_bp)
# app.register_blueprint(service_bp)
# app.register_blueprint(ai_bp)

if __name__ == "__main__":
    app.run(debug=True)
