from stats import generate_report
import sys

def get_book_text(file_path: str) -> str:
    print(f"Reading book from {file_path}")
    with open(file_path, 'r') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    generate_report(book_text)

main()

