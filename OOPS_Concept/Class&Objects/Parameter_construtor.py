# Parameterized Constructor:

# Create a class Book with attributes title and author. Use a constructor
# to initialize these attributes and add a method to print the book details.

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def info(self):
        print(f"Title={self.title}")
        print(f"Author={self.author}")


b1=Book("Python","Sandeep")
b1.info()
b2=Book("Java","Rahul")
b2.info()
b3=Book("C++","Ramesh")
b3.info()