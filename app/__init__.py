from flask import Flask

app = Flask(__name__)

# Avoid circular dependency
from app import views