from stats import calc_num_of_words
from stats import count_characters
from stats import sort_dict
import sys

def get_book_text(f):
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        output = get_book_text(f)
        num_word = f"Found {calc_num_of_words(output)} total words"
        raw_dict = count_characters(output)
        sorted_list = sort_dict(raw_dict)
    print("============BOOKBOT============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("-----------Word Count----------")
    print(num_word)
    print("---------Character Count-------")
    for i in sorted_list:
        if i["key"].isalpha():
            print(i["key"] + ":", i["value"])
    print("=============END===============")

main()