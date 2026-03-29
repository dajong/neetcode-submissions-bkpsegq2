class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) // 2

        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] > maj:
                return n