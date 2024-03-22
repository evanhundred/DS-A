def permute(nums):
    print(nums)
    if len(nums) <= 1:
        return nums
    
    allPerms = []

    for idx, num in enumerate(nums):
        # print(idx,num)
        after1 = nums[idx + 1::]
        # print(nums[after1])
        permutedSlice = permute(after1)
        # print(permutedSlice)
        for array in permutedSlice:
            allPerms.append([array].insert(0,num))

        # allPerms.append(permute(nums).insert(0,firstNum))

    print(allPerms)
    return allPerms

print(permute([1,2,3]))