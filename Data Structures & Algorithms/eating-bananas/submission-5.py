class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while r >= l:
            k = l + (r - l)//2

            t = 0
            for p in piles:
               t += math.ceil(float(p) / k)

            if t <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res