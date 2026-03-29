class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tmp_set = []
        
        for i in nums:
            if i in tmp_set:
                return True
            tmp_set.append(i)
        return False