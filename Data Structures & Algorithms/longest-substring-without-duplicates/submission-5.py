class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = res = curSum = 0

        for R in range(len(s)):
            if s[R] in window:
                for i in range(L, R):
                    curSum -= 1
                    if s[i] == s[R]:
                        L = i + 1
                        window.remove(s[i])      
                        break
                    window.remove(s[i])
                    
            window.add(s[R])
            curSum += 1
            res = max(curSum, res)

        return res