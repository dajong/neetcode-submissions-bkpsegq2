class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeroCount = 0

        for i in range(len(nums)):
            curN = 1

            if curN == 0:
                zeroCount += 1
                res.append(curN)
                continue
            if zeroCount > 1:
                return [0 * len(nums)]
                
            for j in range(len(nums)):
                if i != j:
                    curN *= nums[j]
            
            res.append(curN)

        return res
                
