import urllib.request,json
from .models import News_Source, News_Article

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url 
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

 
def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)
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
            news_object = News_Source(name, url, description)
            news_results.append(news_object)

    return news_results


def get_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=general&language=en&pageSize=10&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result

def get_health_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=health&pageSize=5&language=en&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result

def get_sports_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=sports&language=en&pageSize=5&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result

def get_technology_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=technology&language=en&pageSize=5&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result


def get_entertainment_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=entertainment&language=en&pageSize=5&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result

def get_business_articles():

    get_articles_url = 'https://newsapi.org/v2/top-headlines?category=business&language=en&pageSize=5&apiKey={}'.format(api_key)
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
        description = article_item.get('description')
        publishedAt = article_item.get('publishedAt')
        author = article_item.get('author')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')

        if title:
            articles_object = News_Article(title, description, publishedAt, author, urlToImage, url)
            articles_result.append(articles_object)

    return articles_result





  

