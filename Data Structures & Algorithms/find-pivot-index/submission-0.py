class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cur = 0
        prefix = []
        for n in nums:
            cur += n
            prefix.append(cur)
        
        if prefix[len(prefix) - 1] - prefix[0] == 0:
            return 0

        for i in range(1, len(prefix)):
            if prefix[i-1] == (prefix[len(prefix) - 1] - prefix[i]):
                return i
        return -1
