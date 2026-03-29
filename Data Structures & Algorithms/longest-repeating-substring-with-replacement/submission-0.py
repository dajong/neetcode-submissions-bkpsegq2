class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = L = 0
        maxC = L

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            maxC = max(maxC, count[s[R]])

            while R - L + 1 - maxC > k:
                count[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)

        return res