
def count_words(path):
    with open(path, 'r') as file:
        text = file.read()
        words_count = len(text.split())
        return words_count

path = str(input("Enter path of file : "))
count = count_words(path)
print(f"Number of Words in {path} is {count}")
