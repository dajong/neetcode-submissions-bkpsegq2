class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while r >= l:
            mid = l + (r - l) // 2
            t = 0
            for p in piles:
                t += math.ceil(float(p)/mid)
            if t <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res