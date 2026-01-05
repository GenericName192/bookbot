def number_of_words_in_book(book):
    return len(book.split())


def number_of_each_character(book):
    book = book.lower()
    char_count = {}
    for character in book:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count
