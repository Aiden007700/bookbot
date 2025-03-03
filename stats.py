def get_num_words(text: str) -> int:
    return len(text.split())

def count_letter_occurrences(text: str) -> dict:
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def generate_report(text: str) -> None:
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    letter_counts = count_letter_occurrences(text)
    for letter, count in sorted(letter_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{letter}: {count}")
    print("============= END ===============")