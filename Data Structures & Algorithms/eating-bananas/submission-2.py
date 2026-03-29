class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while r >= l:
            mid = (l + r) // 2

            curTime = 0
            for p in piles:
                curTime += math.ceil(float(p) / mid)
            
            if curTime <= h:
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1

        return res