class News_Source:

    def __init__(self, name, url, description):

        self.name = name
        self.url = url
        self.description = description
    

class News_Article:

    def __init__(self,title, description, publishedAt, author, urlToImage, url):

        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.author = author
        self.urlToImage = urlToImage
        self.url = url