class BookNotFoundError(Exception):
    message = "The book you specified does not exist."
    i18n = "errors.book_not_found"

    def __str__(self):
        return BookNotFoundError.message


class BooksNotFoundError(Exception):
    message = "No books were found."
    i18n = "errors.books_not_found"

    def __str__(self):
        return BooksNotFoundError.message
