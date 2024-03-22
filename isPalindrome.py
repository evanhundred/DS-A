def isPalindrome(s):
	x, y = 0, len(s) - 1
	while x < y:
		# filter for alnum
		for ptr, val in dict(x=1,y=-1):
			while not s[ptr].isalnum():
				ptr += val
		if s[x].lower() == s[y].lower():
			y -= 1
			x += 1
		else:
			return False
	return True



# leetcode
# 54 ms / 35.50%
# 17.03 MB / 94.65%
# def first_isPalindrome(s):
# 	x, y = 0, len(s) - 1
# 	for idx, char in enumerate(s):
# 		if not char.isalnum():
# 			continue
# 		while not s[y].isalnum():
# 			y -= 1
# 		if y <= idx:
# 			return True
# 		if char.lower() == s[y].lower():
# 			y -= 1
# 		else:
# 			return False
# 	return True

str = "hello"
str = "heleh"
str = "heleh!"
# str = "A man, a plan, a canal: Panama"
# str = "0P"
print(isPalindrome(str))

# def pointerValues():
# 	pointerValues = dict(x=1,y=-1)
# 	for k,v in pointerValues.items():
# 		print(k,v)

# pointerValues()

# char = "a"
# print(notchar.isalpha())

