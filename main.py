import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)
    sorted_counts = sort_character_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['character']}: {entry['count']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()


from stats import get_num_words

from stats import count_characters

from stats import sort_character_counts

main()