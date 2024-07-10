from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
jwt = JWTManager(app)

# Importing routes
from resources import member, trainer, fitness_class, schedule, attendance, payment, user

app.register_namespace(user.ns)
app.register_namespace(trainer.ns)
app.register_namespace(fitness_class.ns)
app.register_namespace(schedule.ns)
app.register_namespace(attendance.ns)
app.register_namespace(payment.ns)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Gym Management System API"})

if __name__ == '__main__':
    app.run(debug=True)
