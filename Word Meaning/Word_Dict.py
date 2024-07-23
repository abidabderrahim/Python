"""
Simple program for word meaning , and we can use PyDictionary
like package for search about the meaning of the words .
"""

def main():
    word_dictionary = {
        'A' : 'first Upercase of characters',
        'Z' : 'last Upercase of characters',
        '0' : 'first digit in decimal numbers',
        '1' : 'digit one in decimal numbers',
        '9' : 'last digit in decimal numbers'
    }
    while True:
        word = input("Enter a word : ")
        if word == "":
            break
        if word in word_dictionary:
            print(f"{word} : {word_dictionary[word]}")

main()