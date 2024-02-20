class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        result = {}
        for x in strs:
            s = ''.join(sorted(x))
            if s in result:
                result[s].append(x)
            else:
                result[s] = [x]
               
        return list(result.values())