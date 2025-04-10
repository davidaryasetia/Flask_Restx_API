from flask import Flask
from flask_restx import Api

# Initialize Flask application and wraps it with a Flask-Restx API 
app = Flask(__name__)
api = Api(
    app, 
    version = 1.0, 
    title = 'Miniproject Flask API', 
    description='Sample API Using Flask-RestX'
)

if __name__ == '__main__': 
    app.run(debug=True)

# In flask-restx we can use namespace endpoint api to prevent collision. 