class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter
        count = {}
        
        # buckets
        freq = [[] for i in range(len(nums) + 1)]

        # count each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # put them into buckets
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res

