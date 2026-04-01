class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        tmp = []
        for key, value in count.items():
            heapq.heappush(tmp, (value, key))
            if len(tmp) > k:
                heapq.heappop(tmp)

        for i in range(k):
            res.append(heapq.heappop(tmp)[1])

        
        return res