class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        result = {}
        for x in nums:
            if x in result:
                result[x] += 1
            else:
                result[x] = 1

        result = dict(sorted((result.items()), key=lambda item: item[1]))
        return list(result.keys())[-k:]
