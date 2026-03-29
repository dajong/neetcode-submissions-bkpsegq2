class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        maj = len(nums) // 3
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] > maj and n not in res:
                res.append(n)
        
        return res