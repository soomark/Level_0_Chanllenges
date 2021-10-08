# Function prints vowels in a string
def printvowels(word):
    letters = ''
    print(end='Vowels: ')
    for x in word:
        if x in 'aeiou':
            letters += x + ','
        else:
            if x in 'AEOIU':
                            letters += x + ','
    print(letters.lower()[:len(letters) - 1])


input_string = "Ear"
printvowels(input_string)
