# parsed: 76 ms / 5.49%
def isPalindrome(s):
        parsed = ""

        for char in s:
            if char.isalnum():
                parsed += char
        if len(parsed) == 0:
            return True

        start = 0
        end = len(parsed) - 1
        while start < end:
            print(start,end)
            if parsed[start].lower() == parsed[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
print()
s = ".," # True
print(isPalindrome(s))

# continue solotion:
#     81ms / 5.11%
 # 75ms outer if/else
 # while not check
    # 65ms


    # old

        #     print(start,end)
        #     while not s[start].isalnum() & s[end].isalnum():
        #         if start < end:
        #             if not s[start].isalnum():
        #                 start += 1
        #             if not s[end].isalnum():
        #                 end -= 1
        #         else:
        #             return False
        #     if s[start].lower() == s[end].lower():
        #         start += 1
        #         end -= 1
        #     else:
        #         return False
        # return True