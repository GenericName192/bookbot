def number_of_words_in_book(book):
    return len(book.split())


def number_of_each_character(book):
    book = book.lower()
    char_count_dict = {}
    for character in book:
        if character in char_count_dict:
            char_count_dict[character] += 1
        else:
            char_count_dict[character] = 1

    return char_count_dict


def sort_on(items):
    return items["num"]


def sorted_character_numbers(char_count_dict):
    char_numbers_list = []
    for character in char_count_dict:
        char_numbers_list.append({"char": character,
                                  "num": char_count_dict[character]})
    char_numbers_list.sort(key=sort_on, reverse=True)
    return char_numbers_list
