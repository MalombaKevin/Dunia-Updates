from flask import Flask

from app.config import DevConfig, ProdConfig

app = Flask(__name__, instance_relative_config = True)

app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'


from app import views