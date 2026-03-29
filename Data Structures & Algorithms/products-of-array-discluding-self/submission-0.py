class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot, zero = 1, 0

        for n in nums:
            if n:
                tot *= n
            else:
                zero += 1

        res = [0] * len(nums)

        if zero > 1:
            return res
        
        
        for i, v in enumerate(nums):
            if zero:
                res[i] = 0 if v else tot
            else:
                res[i] = tot // v
        return res