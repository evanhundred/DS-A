def containsDuplicate(nums):
	numHash = {}
	returnVal = False
	for num in nums:
		try:
			if numHash[num] == True:
				returnVal = True
		except:
			numHash[num] = True
	return returnVal		
	
nums = [1,2,3,4,2]
print(containsDuplicate(nums));