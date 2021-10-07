# Function prints vowels in a string
def printvowels(word):
    letters = ''
    print(end='Vowels: ')
    for x in word:
        if x in 'aeiou':
            letters += x + ','
    print(letters[:len(letters) - 1])


w1 = "Umuzi"
printvowels(w1)
