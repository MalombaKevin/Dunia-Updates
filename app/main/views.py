from flask import render_template
from . import main
from ..requests import get_articles, get_entertainment_articles, get_news, get_health_articles, get_sports_articles, get_technology_articles, get_business_articles


@main.route('/')
def index():
    sources = get_news()
    articles = get_articles()
    return render_template('index.html', news_sources= sources, news_articles = articles)

@main.route('/health')
def health():
    articles = get_health_articles()
    return render_template('health.html', news_articles=articles )

@main.route('/enta')
def enta():
    articles = get_entertainment_articles()
    return render_template('enta.html', news_articles=articles )

@main.route('/sports')
def sports():
    articles = get_sports_articles()
    return render_template('sports.html', news_articles=articles )

@main.route('/tech')
def technology():
    articles = get_technology_articles()
    return render_template('tech.html', news_articles=articles )

@main.route('/biz')
def business():
    articles = get_business_articles()
    return render_template('biz.html', news_articles=articles )

    