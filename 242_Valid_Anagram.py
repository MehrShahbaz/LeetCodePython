class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        result1 = {}
        result2 = {}
        for x in range(len(s)):
            result1[s[x]] = 1 + result1.get(s[x], 0)
            result2[t[x]] = 1 + result2.get(t[x], 0)

        return result1 == result2
