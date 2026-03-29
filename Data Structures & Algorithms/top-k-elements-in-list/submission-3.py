class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        top = []
        for _k, _v in count.items():
            heapq.heappush(top, (_v, _k))
            if len(top) > k:
                heapq.heappop(top)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(top)[1])
        
        return res
