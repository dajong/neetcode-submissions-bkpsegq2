class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while r >= l:
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            
            mid = l + ((r - l) // 2)
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return res