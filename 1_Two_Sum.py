class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
    
        result = {}
        for index, num in enumerate(nums):
            if (target - num) in result:
                return [result[target - num], index]
            else:
                result[num] = index