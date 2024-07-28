def main():
    book_path = "books/frankenstein.txt"
    abc = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z")

    with open(book_path) as f:
        text = f.read()
    
    def split_text(text):
        new = text.split()
        return len(new)

    def number_of_char(text):
        chars = {}
        for c in text:
            c = c.lower()
            if c in abc:
                if c in chars:
                    chars[c] += 1
                else:
                    chars[c] = 1
        return chars

    def print_to_screen(dict):
        char_list = list(dict.items())
        char_list.sort(key=lambda item: item[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document")
        for item in char_list:
            print(f"The {item[0]} character was found {item[1]} times")
        print("--- End report ---")

    num_words = split_text(text)
    chars_dict = number_of_char(text)
    print_to_screen(chars_dict)
main()