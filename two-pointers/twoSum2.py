def twoSum(numbers, target)
        result = []
        x = 0
        y = len(numbers) - 1
        num1 = numbers[x]
        num2 = numbers[y]
        if num2 + num1 < target:
                return result
                
        lastItered = "x"
        isComplete = False
        while not isComplete:
            if y <= x:
                isComplete = True
                break
            if num1 + num2 == target:
                result = [x + 1, y + 1]
                isComplete = True
            else:
                if lastItered == "x":
                    y += 1
                    lastItered = "y"
                else: 
                    x += 1
                    lastItered = "x"
        
        return result