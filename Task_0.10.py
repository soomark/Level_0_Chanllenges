#Function to find common elements present in 2 words
def common_letters(word1, word2):
	s1 = word1
	s2 = word2

#List output
	result = []

#Function process
	if len(s1) < len(s2):
		for i in s1:
			if i in s2:
				result.append(i)
	else:
		for i in s2:
			if i in s1:
				result.append(i)

	print("Common letters:", *result)


wordA = input("Enter the first string: ")
wordB = input("Enter the second string: ")
common_letters(wordA, wordB)
