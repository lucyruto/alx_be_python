class Book:
    count = 0
    def __init__(self, title):
        self.title = title
        Book.count +=1


    @classmethod
    def display_count(cls):
        print(f"Total books added: {cls.count}")

book1 = Book("Sarafina")
book2 = Book("Sarafina2")
book2 = Book("Sarafina3")

Book.display_count()