def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()


def number_of_words_in_book(book):
    return len(book.split())


def main():
    # print(get_book_text("books/frankenstein.txt"))
    book = get_book_text("books/frankenstein.txt")
    num_words = number_of_words_in_book(book)
    print(f"Found {num_words} total words")


main()
