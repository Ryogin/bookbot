def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_char(count_char):
    sort_list = []
    for char, num in count_char.items():
        sort_list.append({"char":char, "num":num})
    sort_list.sort(reverse=True, key=lambda x: x["num"])
    return sort_list








