def twoSum(numbers, target)
        result = []
        x = 0
        y = len(numbers) - 1
        num1 = numbers[x]
        num2 = numbers[y]
        if num2 + num1 < target:
            return result
                
        isComplete = False
        while not isComplete:
            if y <= x:
                if x + y < target or x >= len(numbers) - 2:
                    isComplete = True
                    break
                x += 1
                y = len(numbers - 1)
            num1 = numbers[x]
            num2 = numbers[y]
            if num1 + num2 == target:
                result = [x + 1, y + 1]
                isComplete = True
                break
            else:
                y -= 1
        
        return result