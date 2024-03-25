def findDuplicates(nums):
    if len(nums) < 2:
        return []
    frequency = {}
    for el in nums:
        if el not in frequency:
            frequency[el] = 1
        else:
            frequency[el] += 1
    twice = []
    for key in frequency:
        if frequency[key] == 2:
            twice.append(key)
    return twice

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))

nums = [1,1,2]
print(findDuplicates(nums))

nums = [1]
print(findDuplicates(nums))
