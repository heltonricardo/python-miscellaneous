class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __add__(self, other):
        total_pages = self.pages + other.pages
        return f"The combined pages of '{self.title}' and '{other.title}' is {total_pages} pages."

    def __sub__(self, other):
        difference = self.pages - other.pages
        return f"The difference in pages between '{self.title}' and '{other.title}' is {abs(difference)} pages."

    def __mul__(self, scalar):
        return f"The pages of '{self.title}' multiplied by {scalar} is {self.pages * scalar} pages."

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __ge__(self, other):
        return self.pages >= other.pages


book1 = Book("The Catcher in the Rye", "J. D. Salinger", 288)
book2 = Book("Journey to the Center of the Earth", "Jules Verne", 146)

print("Arithmetic dunder methods demonstration:")
print("Sum:", book1 + book2)
print("Difference:", book1 - book2)
print("Multiplication by scalar:", book1 * 2)
print()
print("Relational dunder methods demonstration:")
print("Equal:", book1 == book2)
print("Less than:", book1 < book2)
print("Less than or equal:", book1 <= book2)
print("Greater than:", book1 > book2)
print("Greater than or equal:", book1 >= book2)
