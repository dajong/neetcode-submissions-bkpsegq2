class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target < nums[l]:
            return 0
        elif target > nums[r]:
            return r + 1

        while r >= l:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

        return l

