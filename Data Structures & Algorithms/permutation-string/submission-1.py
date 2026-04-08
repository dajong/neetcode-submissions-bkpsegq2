class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l = 0
        target = "".join(sorted(s1))

        while len(s2) >= l + window:
            if "".join(sorted(s2[l:l + window])) == target:
                return True
            l += 1
        return False
