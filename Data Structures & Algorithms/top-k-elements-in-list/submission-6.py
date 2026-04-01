class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1
        
        tmp = []
        for key, value in mp.items():
            tmp.append((value, key))
        tmp = sorted(tmp)

        for i in range(k):
            res.append(tmp.pop()[1])

        return res
