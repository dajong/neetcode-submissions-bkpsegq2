class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(1, len(strs)):
            if strs[i] == "":
                return ""
            for c in range(min(len(res), len(strs[i]))):
                if res[c] != strs[i][c]:
                    if c == 0:
                        return ""
                    res = res[0:c]
                    break
                if c == min(len(res), len(strs[i])) - 1:
                    res = res[0:c+1]
                continue
        return res
