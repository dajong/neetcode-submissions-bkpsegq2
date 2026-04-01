class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, v in enumerate(nums):
            if v > 0:
                continue
            
            if i > 0 and nums[i-1] == v:
                continue

            l, r = i + 1, len(nums) - 1

            while r > l:
                tSum = v + nums[l] + nums[r]

                if tSum > 0: 
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and r > l:
                        l += 1

        return res