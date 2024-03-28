# LeetCode 167

def twoSum(numbers, target)
    int]:
        result = []
        if len(numbers) == 0:
            return result
        x = 0
        y = len(numbers) - 1
        num1 = numbers[x]
        num2 = numbers[y]
        if num2 + numbers[y - 1] < target:
            return result
        if num2 + numbers[y- 1] == target:
            return [y, y + 1]
                
        isComplete = False
        while not isComplete:
            if y == 0 and x == 0:
                isComplete = True
            if x == y:
                x -= 1
                y = len(numbers) - 1
            num1 = numbers[x]
            num2 = numbers[y]
            if num1 + num2 == target:
                result = [x + 1, y + 1]
                isComplete = True
                break
            if num1 + num2 < target:
                x += 1
                continue
            if num1 + num2 > target:
                y -= 1
                
        return result