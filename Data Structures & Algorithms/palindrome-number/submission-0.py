class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        sx = str(x)
        l, r = 0, len(sx) - 1
        while r > l:
            if sx[l] != sx[r]:
                return False
            l += 1
            r -= 1

        return True