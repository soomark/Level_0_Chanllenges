# Function prints vowels in a string
def printvowels(word):
    # to print the vowels
    for char in word:
        if char in "aeiouAEIOU":
            print(char, end=', ')


word = input("Entre the string: ")
printvowels(word)