class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        
        for i in range(l):
            length = 1
            while i + length < l and temperatures[i + length] <= temperatures[i]:
                length += 1
            res[i] = length if i + length < l else 0

        return res