class News_Source:

    def __init__(self, name, url, description):

        self.name = name
        self.url = url
        self.description = description
    

class News_Article:

    def __init__(self,title, description, name,  publishedAT, author, urlToImage, url):

        self.title = title
        self.description = description
        self.name = name
        self.publishedAT = publishedAT
        self.author = author
        self.urlToImage = urlToImage
        self.url = url