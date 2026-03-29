class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                prod *= n
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i, c in enumerate(nums):
            if zero_count: res[i] = 0 if c else prod
            
            else:
                res[i] = int(prod / c)
        
        return res