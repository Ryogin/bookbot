from stats import count_words, count_char, sort_char

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    chars_dict = count_char(text)
    chars_sorted = sort_char(chars_dict)
    report(book_path, total_words, chars_sorted)
    
def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def report(book_path, count_words, sort_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for i in sort_char:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")


main()