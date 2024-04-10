from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load Configuration of application. Check configuration.py for more details
app.config.from_object('app.configuration.DevConfig')


from app import routes
