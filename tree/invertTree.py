def invertTree(root):
	result = []
	idx = 0
	countForRow = 1
	maxForRow = 1

	while idx < len(root):
		if count > maxForRow:
			maxForRow *= 2
		if idx + maxForRow >= len(root):
			maxForRow = len(root) - idx
		while countForRow < maxForRow:
			result.append
			
		
		
		idx += 1
			
	return result

root = [4,2,7,1,3,6,9]
print(invertTree(root))
root = [2,1,3]
print(invertTree(root))
root = []
print(invertTree(root))