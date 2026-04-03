class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        res = 0

        for i in range(len(nums)):
            count = 1
            curN = nums[i]
            if curN - 1 in nums or curN in seen:
                continue
            seen.add(curN)
            while curN + 1 in nums:
                seen.add(curN + 1)
                count += 1
                curN += 1
            res = max(count, res)


        return res

