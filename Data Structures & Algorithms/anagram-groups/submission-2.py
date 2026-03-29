class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {sorted string, index}
        track = {}
        res = []
        num = 0
        for s in strs:
            sc = sorted(s)
            ss = "".join(sc)
            if ss in track:
                res[track.get(ss)].append(s)
            else:
                track[ss] = num
                num+=1
                res.append([s])
                
        return res
        