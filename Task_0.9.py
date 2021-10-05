# Function prints vowels in a string
def printvowels(word):
    # to print the vowels
    for char in word:
        if char in "aeiou":
            print(char, end=', ')
    return char


w1 = "Umuzi"
printvowels(w1)
