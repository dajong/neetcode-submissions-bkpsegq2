class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # positive needs negative anyway, we can skip positive numbers
            if a > 0:
                break
            
            # remove duplicates
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums) - 1

            while r > l:
                s3 = nums[l] + nums[r] + a
                if s3 > 0:
                    r -= 1
                elif s3 < 0:
                    l += 1
                else: 
                    res.append([nums[l], nums[r], a])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res