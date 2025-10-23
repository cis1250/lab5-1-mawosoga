#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True



import string

def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if (len(sentence) > 0 and
            sentence[0].isupper() and
            sentence[-1] in ".?!"):
            return sentence
        else:
            print("Invalid input sentence must start with a capital letter and end with '.', '?' or '!'.")

def calculate_frequencies(sentence):
    translator = str.maketrans('', '', string.punctuation.replace("'", ""))
    cleaned_sentence = sentence.translate(translator).lower()
    words = cleaned_sentence.split()
    word_list = []
    frequency_list = []

    for word in words:
        if word in word_list:
            index = word_list.index(word)
            frequency_list[index] += 1
        else:
            word_list.append(word)
            frequency_list.append(1)

    return word_list, frequency_list

def print_frequencies(words, frequencies):
    print("Word Frequencies:")
    for word, freq in zip(words, frequencies):
        print(f"{word}: {freq}")

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

if __name__ == "__main__":
    main()
