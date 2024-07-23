"""
tool for replace word in string .
"""

def replace_word():
    text = str(input("Enter your string : "))
    print(f"this is your string : {text}")
    word_to_replace = str(input("Enter the word to replace: "))
    word_replacement = str(input("Enter the word for replacement: "))
    new_text = text.replace(word_to_replace, word_replacement)
    return new_text

new_v_text = replace_word()
print(new_v_text)
