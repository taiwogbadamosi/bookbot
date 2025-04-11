import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    string = get_book_text(book_path)
    num_words = get_num_words(string)
    dictionary = get_num_chars(string)
    arr = sort_dict(dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for d in arr:
        for k in d:
            if k.isalpha():
                print(f"{k}: {d[k]}")
        
def get_book_text(path):
    with open(path) as f:
        file_string = f.read()
        return file_string
main()
