class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                continue
            if i > 0 and nums[i-1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            while r > l:
                tSum = n + nums[l] + nums[r]
                if tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and r > l:
                        l += 1

        return res