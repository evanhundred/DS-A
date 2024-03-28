def twoSum(numbers, target)
        x = 0
        y = len(numbers) - 1
        result = []
        isComplete = False
        while not isComplete:
            if y <= x:
                if x == 
                isComplete = True
                break
            num1 = numbers[x]
            num2 = numbers[y]
            if num1 + num2 == target:
                result = [x + 1, y + 1]
                isComplete = True
            else:
                y += 1
        
        return result