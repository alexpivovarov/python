

def vow_counter(word):
    counter = 0
    vowels = 'aeiouAEIOU' # Including uppercase vowels for case insensitivity
    for char in word:
        if char in vowels:
            counter += 1
    return counter



word = input("Enter a word: ")
print(f"The number of vowels in '{word}' is {vow_counter(word)}")