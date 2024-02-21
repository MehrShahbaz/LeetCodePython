class Solution:
    def isPalindrome(self, s: str) -> bool:
        def convertSmall(s):
            return [x.lower() for x in s if x.isalpha() or x.isnumeric()]
        
        res = convertSmall(s)
    
        start = 0
        end = len(res) - 1
        
        while (start < end):
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        
        return True