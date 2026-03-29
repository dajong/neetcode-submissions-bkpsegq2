class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i, n in enumerate(nums):
            want = target - n

            if want in track:
                return [track[want], i]
            
            track[n] = i

        return null