class Article:

    #Variable to store all the articles inside a list
    all = []


    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
       
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long.")
        self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if not isinstance(author,Author):
            raise Exception
        self._author = author

        
class Author:

    #List to store the authors
    all = []

    def __init__(self, name):
        self._name = None
        self.name = name
        Author.all.append(self)
        self.author_articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique_magazines = set([article.magazine for article in self.articles()])
        return list(unique_magazines)

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            #Error handling to avoid the program crashing
            raise Exception
        self.author_articles.append(magazine)
        return Article(self,magazine,title)

    def topic_areas(self):
        if[magazine.category for magazine in self.author_articles] == []:
            return None
        category_set = set([magazine.category for magazine in self.author_articles])
        #Returning the category set as a list
        return list(category_set)

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and  2 <= len(name) <=16:
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category) > 0:
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_contributors = set([article.author for article in self.articles()])
        return list(unique_contributors)

    def article_titles(self):
        if [article.title for article in self.articles()] == []:
            return None
        return [article.title for article in self.articles()]
    

    def contributing_authors(self):
        if len([article.author for article in self.articles()]) <= 2:
            return None
        return [article.author for article in self.articles()]

