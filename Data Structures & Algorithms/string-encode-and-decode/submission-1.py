class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        l = 0
        while len(s) > l:
            r = l

            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            
            l = r + 1
            r = l + length
            ans.append(s[l:r])

            l = r
        
        return ans


        