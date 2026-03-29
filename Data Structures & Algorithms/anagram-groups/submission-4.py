class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for s in strs:
            ss = "".join(sorted(s))
            count[ss].append(s)

        return list(count.values())