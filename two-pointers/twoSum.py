leetcode: 
	49ms / 98.81%
	18.47 MB / 22.38%
def twoSum(nums, target):
	addendHash = {}
	for idx, num in enumerate(nums):
		compliment = target - num
		if compliment in addendHash:
			return [addendHash[compliment], idx]
		else:
			addendHash[num] = idx
	print(addendHash)
	return False


nums = [2,7,11,15]
target = 9
print(twoSum(nums,target)) # [0,1]
nums = [3,2,4]
target = 6
print(twoSum(nums,target)) # [1,2]
nums = [3,3]
target = 6
print(twoSum(nums,target)) # [0,1]

# leetcode 3193 ms / 10.69%
def twoSum(nums, target):
	x = 0
	y = 1
	loopIsOver = False
	while not loopIsOver:
		if nums[x] + nums[y] == target:
			return [x,y]
		if y == len(nums) - 1:
			if x < len(nums) - 2:
				x += 1
				y = x + 1
			else:
				loopIsOver = True
		else:
			y += 1
	return False