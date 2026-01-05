from stats import number_of_words_in_book, number_of_each_character
from stats import sorted_character_numbers


def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # print(get_book_text("books/frankenstein.txt"))
    book = get_book_text("books/frankenstein.txt")
    num_words = number_of_words_in_book(book)
    number_of_chars = number_of_each_character(book)
    sorted_list = sorted_character_numbers(number_of_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()
