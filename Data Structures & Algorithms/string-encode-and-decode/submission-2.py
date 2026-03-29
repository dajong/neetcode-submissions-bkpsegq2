class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0

        while len(s) > l:
            r = l

            while s[r] != '#':
                r += 1
            
            length = int(s[l:r])
            
            l = r + 1
            r = l + length

            curS = s[l:r]
            res.append(curS)

            l = r

        return res