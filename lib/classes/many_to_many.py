class Article:

    
    articles=[]
    all = []

    def __init__(self, author, magazine, title):
        self.author = author        
        self.magazine = magazine
        self.title = title
        Article.articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise AttributeError("Cannot change the title of an existing Article object")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be of type string and between 5 and 50 characters, inclusive")
        self._title = title
 
    #author property
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception
        
    #magazine property
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise Exception
        
class Author:

    #attribute to store all author instances/ authors

    all = []

    #Author constructor/initializer
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        #code to ensure, author name property Should not be able to change after the author is instantiated hint: hasattr()
        if hasattr(self, "name"):
            raise AttributeError("Cannot change the name of an existing Author object")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name = name
    #return articles associated with an author
    def articles(self):
        return [article for article in Article.articles if article.author == self]
    
    #returns the number of articles written by the author
    def count(self):
        return len(self.articles())
    
    #return magazines associated with an author
    def magazines(self):
        mag_set=set([article.magazine for article in self.articles()])
        return list(mag_set)

        #return [article.magazine for article in self.articles()]

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazines= self.magazines()
        if magazines:
            magazines_set=set([magazine.category for magazine in magazines])
            return list(magazines_set)
        else:
            return None

class Magazine:

    
   #these two lines do the same thing, wrote for my on understanding, variable all is similar to magazines
    magazines= []
    all = []

    @classmethod 
    def top_publisher(cls):
        #starts by checking if there are any magazines and articles in the database,
        if Article.all and Magazine.all:
            #make sure that all the magazines in the database are actually Magazine objects.
            if all(isinstance(mag, Magazine) for mag in Magazine.all):
                #creates a dictionary where the keys are the magazines and the values are the number of articles for each magazine.
                mag_articles = {mag:len(mag.articles()) for mag in Magazine.all}
                top_mag = max(mag_articles, key=lambda mag:mag_articles[mag])
            
                return top_mag
        
        #If there are no magazines or articles in the database, the method returns None.
        return None
   

    def __init__(self, name, category):
        self.name = name
        self.category = category

        #these two lines do the same thing, wrote for my on understanding, variable all is similar to magazines
        Magazine.all.append(self)
        Magazine.magazines.append(self)

    #magazine name getter and setter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (2 <= len(name)) or not (len(name)<= 16):
            raise Exception
        self._name = name

    #magazine category property setter and getter
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if not isinstance(category, str) or not (0<len(category)):
            raise Exception
        self._category = category

    #return articles associated with a magazine
    def articles(self):
        
        return [article for article in Article.articles if article.magazine == self]
    #return authors associated with a magazine
    def contributors(self): 

        authorsSet =  set([article.author for article in self.articles()])
        authors = list(authorsSet)

        return authors
        


    def article_titles(self):
        articles = self.articles()

        if articles:
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
        contributing_authors = []
        authorsSet= self.contributors()
        authors = list(authorsSet)  # Get the set of authors for this magazine
        
        for author in authors:
            if isinstance(author, Author) and author.count() > 2:  # Check if the author is an Author instance and has written more than 2 articles
                contributing_authors.append(author)
            else:
                return None
        if contributing_authors:
            return contributing_authors
        
        