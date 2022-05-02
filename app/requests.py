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



  

