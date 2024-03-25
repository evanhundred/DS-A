import math

def searchLine(nums, target):
    if nums[0] == target:
        return 0
    if len(nums) <= 1:
        return -1

    midpoint = math.floor(len(nums) / 2)
    left = nums[:midpoint]
    right = nums[midpoint:]

    leftResult = self.searchLine(left)
    if leftResult != -1:
        return leftResult
    rightResult = self.searchLine(right)
    if rightResult != -1:
        return rightResult + midpoint
        
        return -1

# prev
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
