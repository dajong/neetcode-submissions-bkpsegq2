class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, v in enumerate(nums):
            need = target - v

            if need in hm:
                return [hm[need], i]
            
            hm[v] = i
        
        return None