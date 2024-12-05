class Magazine:

    _all = [] 

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all.append(self)

    def name(self):
        return self._name

    def category(self):
        return self._category

    @classmethod
    def all(cls):
        return cls._all

    def contributors(self):
        authors = []
        for article in self._articles:
            author = article.author()
            if author not in authors:
                authors.append(author) #  pre-defined method used to add a single item to certain collection types
        return authors

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all:
            if magazine.name() == name:
                return magazine
        return None

    @classmethod
    def article_titles(cls):
        titles = []
        for magazine in cls._all:
            for article in magazine._articles:
                title = article.title()
                titles.append(title)
        return titles

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author()
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1 # use else statement to execute code when the condition inside the if statement is False
        contributing_authors = []
        for author, count in authors.items():# A for loop is used for iterating over a sequence
            if count > 2:# if is used when the condition is true
                contributing_authors.append(author)
        return contributing_authors