class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            cur = nums[i]
            if (target - cur) in m:
                return [m.get(target - cur), i]

            m[cur] = i

        return [] 