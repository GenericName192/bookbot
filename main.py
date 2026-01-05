from stats import number_of_words_in_book, number_of_each_character


def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # print(get_book_text("books/frankenstein.txt"))
    book = get_book_text("books/frankenstein.txt")
    num_words = number_of_words_in_book(book)
    print(f"Found {num_words} total words")
    print(number_of_each_character(book))


main()
