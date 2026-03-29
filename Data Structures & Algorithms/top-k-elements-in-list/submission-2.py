class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        topCount = []
        ans = []

        for n in nums:
            count[n] += 1

        for key,v in count.items():
            topCount.append((v, key))
        topCount.sort()

        while len(ans) < k:
                ans.append(topCount.pop()[1])
        return ans
