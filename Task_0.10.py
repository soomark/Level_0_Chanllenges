# Function to find common elements present in 2 words
def common_letters(word1, word2):
	s1 = word1
	s2 = word2
	# List output
	result = ''
	# Function process
	if len(s1) < len(s2):
		for i in s1:
			if i.lower() in s2.lower():
				result += i + ', '
	else:
		for i in s2:
			if i.lower() in s1.lower():
				result += i + ', '
	
	print("Common letters:", result.lower()[:len(result) - 2])


wordA = "CompuTers"
wordB = "HouSe"
result = common_letters(wordA, wordB)
