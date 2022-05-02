from flask import render_template
from app import app
from app.requests import get_news
from .models import news

@app.route('/')
def index():
    sources = get_news()
    return render_template('index.html', news_sources= sources)

    