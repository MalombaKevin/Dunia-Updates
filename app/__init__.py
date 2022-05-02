from flask import Flask

from app.config import DevConfig, ProdConfig

app = Flask(__name__)

app.config.from_object(DevConfig)

from app import views