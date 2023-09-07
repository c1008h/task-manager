from flask import Flask

from routes import api_blueprint  
from models.task import Base
from config.connection import Session


app = Flask(__name__)


# Create a SQLAlchemy session
session = Session()
print("Flask app is starting...")

app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)