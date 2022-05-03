from app import app
import urllib.request,json
from .models import news

News_Sources= news.News_Source

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = 'https://newsapi.org/v2/top-headlines/sources?language=en&apiKey=8bcc39f4104646c09fdd3c037f85a7ca'
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        name =news_item.get('name')
        url = news_item.get('url')
        description = news_item.get('description')

        if name:
            news_object = News_Sources(name, url, description)
            news_results.append(news_object)

    return news_results

News_Articles = news.News_Article
def get_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=8bcc39f4104646c09fdd3c037f85a7ca'
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_result = None

        if get_articles_response['articles']:
            articles_result_list = get_articles_response['articles']
            articles_result = process_articles(articles_result_list)

# title, description, name,  publishedAT, author, urlToImage, url
    return articles_result

def process_articles(articles_list):
    articles_result = []
    for article_item in articles_list:
        title = article_item.get('title')
        name = article_item.get('name')
        description = article_item.get('description')
        publishedAT = article_item.get('publishedAT')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Articles(title, description, name,  publishedAT, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result




  

