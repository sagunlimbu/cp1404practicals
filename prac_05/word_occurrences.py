"""
CP1404 - Practical 5
Name: <SAGUN LIMBU>
"""
"""
Word Occurrences
Estimate: 20 minutes
Actual:   [to be filled out after completion]
"""

def main():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()

    for word in words:
        frequency = word_to_count.get(word, 0)
        word_to_count[word] = frequency + 1

    words = list(word_to_count.keys())
    words.sort()

    max_length = max(len(word) for word in words)
    for word in words:
        print(f"{word:{max_length}} : {word_to_count[word]}")

if __name__ == "__main__":
    main()
