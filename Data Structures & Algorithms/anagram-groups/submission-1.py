class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # set to check
        check = {}
        res = []
        counter = 0

        # if its not in the set, create new list and add sorted item to set
        for item in strs:
            sortedItem = sorted(item)
            sortedItem = ''.join(sortedItem)
            if sortedItem not in check.keys():
                cur = [item]
                res.append(cur)
                check[sortedItem] = counter
                counter += 1

        # if its in the set, then add it
            elif sortedItem in check:
                index = check.get(sortedItem)
                res[index].append(item)
        
        return res