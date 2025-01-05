def main():
    filepath = "/home/cmcm750203/workspace/github.com/mcmanusc/bookbot/books/frankenstein.txt"
    try:
        with open(filepath, 'r') as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return

    # Calculate and print letter counts
    letter_counts = count_letters(file_contents)
    print("Letter Counts:")
    for letter, count in sorted(letter_counts.items()):
        print(f"the '{letter}' character appears {count} times.")

    # Calculate and print word count
    word_count = count_words(file_contents)
    print(f"\nTotal Words: {word_count}")



def count_words(file_contents):
    words = len(file_contents.split())
    return words

def count_letters(file_contents):
    counts = {}
    for char in file_contents.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

    


main()
