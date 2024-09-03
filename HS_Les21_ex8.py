# Lesson 21.
"""
8. Dictionaries Exercise:
Create a dictionary of book titles and their authors. Write a function to search for a book
by its title and return the author's name.
"""

books = {"A Time to Love and a Time to Die": "Erich Maria Remarque", "Steppenwolf": "Hermann Hesse",
         "1984": "George Orwell", "Crime and Punishment": "Fyodor Dostoevsky",
         "Critique of Pure Reason": "Immanuel Kant"}

to_search = "Critique of Pure Reason"


def search_for_book(list_of_books: dict, search_title: str) -> str:
    for k, v in list_of_books.items():
        if search_title == k:
            return v


print(search_for_book(books, to_search))

# Output: Immanuel Kant
