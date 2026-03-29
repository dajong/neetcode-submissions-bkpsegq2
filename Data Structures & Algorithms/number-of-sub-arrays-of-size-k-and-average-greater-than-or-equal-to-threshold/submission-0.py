class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        curSum = res = 0

        for R in range(len(arr)):
            curSum += arr[R]
            L = R - k + 1
            if R >= k - 1:
                res += curSum >= threshold 
                curSum -= arr[L]
        return res

