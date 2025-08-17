class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    def contracts(self):
        return [c for c in Contract.all if c.author is self]
    
    def books(self):
        return [c.book for c in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    def contracts(self):
        return [c for c in Contract.all if c.book is self]
    
    def authors(self):
        return [ c.author for c in self.contracts()]
    
    


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @property
    def book(self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [c for c in cls.all if c.date == date]
    
    

    
author = Author("Name") 
book1 = Book("Title1")
book2 = Book("Title2")
book3 = Book("Title3")


Contract(author, book1, "01/01/2001", 10)
Contract(author, book2, "01/01/2001", 20)
Contract(author, book3, "01/01/2001", 30)

total = author.total_royalties()
print(total)




