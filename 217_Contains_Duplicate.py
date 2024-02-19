class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for x in nums:
            if x in result:
                return True
            else:
                result[x] = 1
        return False
