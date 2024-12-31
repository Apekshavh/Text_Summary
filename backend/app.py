from flask import Flask
from flask_cors import CORS
from routes import create_api_routes

app = Flask(__name__)
# Enable CORS for all routes with a simpler configuration
CORS(app, resources={r"/*": {"origins": "*"}})

# Register routes
api = create_api_routes()
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=5012)