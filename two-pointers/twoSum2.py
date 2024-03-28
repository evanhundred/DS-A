def twoSum(numbers, target)
    x = 0
    y = 1
    result = []
    isComplete = False
    while not isComplete:
        if y == len(numbers):
            if x == len(numbers) - 2:
                isComplete = true
                break
            else:
                x += 1
                y = x + 1
                continue
        num1 = numbers[x]
        num2 = numbers[y]
        elif x + y = target:
            result = [num1, num2]
            isComplete = True
        else:
            y += 1
        
    return result