def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words():
    words = get_book_text().split()
    return len(words)

def count_letters():
    text = get_book_text().lower()
    letters = {}
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters



