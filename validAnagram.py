def isAnagram(s: str, t: str):
	letters = {}
	returnVal = False
	for char in s:
		if char in letters:
			letters[char] += 1
		else:
			letters[char] = 1
	for char in t:
		if char in letters:
			if letters[char] == 0:
				break
			letters[char] -= 1
		else:
			return False
			# break
	if all(letters[letter] == 0 for letter in letters):
		returnVal = True
	return returnVal

	
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
s = "rat"
t = "car"
print(isAnagram(s,t))
s="a"
t="ab"
print(isAnagram(s,t))