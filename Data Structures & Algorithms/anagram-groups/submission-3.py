class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            ss = sorted(s)
            ss = "".join(ss)
            if ss not in count:
                count[ss] = []

            count[ss].append(s)

        return list(count.values())



        