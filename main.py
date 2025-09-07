import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {count_words(book_text)} total words
--------- Character Count -------""")
    sorted_chars = sorted(count_characters(book_text).items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")
    
if __name__ == "__main__":
    main()