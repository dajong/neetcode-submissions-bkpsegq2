class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while r > l:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        def bs(l, r):
            while r >= l:
                mid = l + (r - l) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1

        p1 = bs(0, pivot - 1)
        return bs(pivot, len(nums) - 1) if p1 == -1 else p1
        