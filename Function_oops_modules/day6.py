
# OOP part 2: inheritance, dunder methods (__str__/__repr__)

# Build a small Library Management CLI (Book, Library classes) with JSON persistence


# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} makes a sound!")

# animal1 = Animal("dog")
# animal1.speak()

# class Dog(Animal):
#  # pass
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed
#     def speak(self):
#         print(f"{self.name} barks")
# d = Dog("Rex","labra")
# d.speak()
# print(d.name)
# print(d.breed)

# class Cat(Animal):
#     def __init__(self,name,color):
#         super().__init__(name)
#         self.color = color
#     def speak(self):
#         print(f"{self.name}, meows!!")
#     def __repr__(self):
#         print("yo! its a white cat!!")
# c = Cat("Ritzz","White")
# c.speak()
# print(c.color)
# print(c.name)
# my_cat = c
# print(my_cat)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age}"
#     def __repr__(self):
#         return f"{self.name},{self.age}"
# p = Person("rad","34")
# print(p)
# print([p])

import json

class Book:
    def __init__(self,title,author):
        self.borrowed = False
        self.title = title
        self.author = author
    def __str__(self):
        if(self.borrowed == False):
            return f"{self.title}, {self.author} is Available."
        else:
            return f"{self.title}, {self.author} is borrowed."
    def to_dict(self):
        return {"title": self.title, "author": self.author, "borrowed": self.borrowed}

    @classmethod
    def from_dict(cls, data):
        print(data)
        book = cls(data["title"], data["author"])
        book.borrowed = data["borrowed"]
        return book
        
class BooksNotFoundError(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(book)
    def borrow_book(self,title):

        for book in self.books:
            if book.title == title:
                if book.borrowed:
                    print(f"{title} is already borrowed")
                    return
                else:
                    book.borrowed = True
                    print(f"You borrowed {title}")
                return
        raise BooksNotFoundError(f"No book titled '{title}' found in the library.")   
    
    def return_book(self,title):
        try:
            for book in self.books:
                        if book.title == title:
                            if book.borrowed:
                                book.borrowed = False
                                print (f"Yo have returned {title}")
                                return
                            else :
                                print(f"Book is not borrowed")
                            return
            raise BooksNotFoundError(f"No book titled '{title}' found in the library.")
        except BooksNotFoundError as e:
            print(e)

    def save_to_file(self, filename):
        data = [book.to_dict() for book in self.books]
        with open(filename, "w") as f:
            json.dump(data,f)

    def load_from_file(self,filename):
        with open(filename,"r") as f:
            data= json.load(f)
        self.books = [Book.from_dict(item) for item in data]


lib = Library()
lib.add_book(Book("Book A","Author A"))
lib.add_book(Book("Book B","Author B"))
lib.add_book(Book("Book C","Author C"))

lib.list_books()

lib.borrow_book("Book B")
lib.list_books()

lib.return_book("Book x")
lib.list_books()

lib.save_to_file("Library_management")
lib.load_from_file("Library_management")