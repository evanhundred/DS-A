def containsDuplicate(nums) -> bool:
        returnVal = False
        numberHash = {}
        for idx, num in enumerate(nums):
            try:
                if numberHash[num] == True:
                    returnVal = True
                    break
            except:
                numberHash[num] = True
    
        return returnVal
        
nums = [1,2,3,1]
print(containsDuplicate(nums))