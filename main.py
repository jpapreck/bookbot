def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document \n")
    sorted_report(character_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    text = text.lower()
    char_list = []
    char_dict = {}
    for char in text:
        char_list.append(char)
    for letter in char_list:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict
    
def sorted_report(character_count):
    character_count = list(character_count.items())
    character_count.sort()
    for items in character_count:
        if items[0][0].isalpha():
            print(f"The {items[0]} character was found {items[1]} times")

    
main()
