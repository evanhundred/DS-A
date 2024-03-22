import math

def search(nums, target):
    if len(nums) == 1:
        if nums[0] != target:
            return -1
        else:
            return 0

    midpoint  = math.floor(len(nums) / 2)
    left = nums[:midpoint]
    right = nums[midpoint:]

    print((len(nums) / 2) // 1)

    # print(search(left, target))
    resultLeft = search(left, target)
    if resultLeft == -1:
        result = search(right, target)
        if result != -1:
            return result + midpoint
        else:
            return -1
    else:
        return resultLeft

print(search([-1,0,3,5,9,12],9))
