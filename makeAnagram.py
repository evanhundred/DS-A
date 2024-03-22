def makeAnagram(a, b):
	from collections import Counter
	counter = Counter(a)
	counter.subtract(b)
	deletions = sum(map(abs, counter.values()))

	return deletions

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print(makeAnagram(a, b))

# def makeAnagram(a, b):
# 	charHash = {}
# 	deletions = 0

# 	for char in a:
# 		if char in charHash:
# 			charHash[char] += 1
# 		else:
# 			charHash[char] = 1
# 	for char in b:
# 		if char not in charHash:
# 			deletions += 1
# 			print(char)
# 		else:
# 			if charHash[char] == 0:
# 				deletions += 1
# 				print(f' {char}')
# 			else:
# 				charHash[char] -= 1
# 	for char in charHash:
# 		if charHash[char] % 2 != 0:
# 			deletions += 1
# 	print(charHash)
# 	return deletions