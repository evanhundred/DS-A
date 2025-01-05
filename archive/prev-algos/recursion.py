def powerOf(num, power):
	if power <= 1:
		return num

	return num * powerOf(num, power - 1)




# print(powerOf(3,5))
# def loopIt(nums):
# 	for idx,num in enumerate(nums):
# 		print(idx,num)
# loopIt([2,5,7])