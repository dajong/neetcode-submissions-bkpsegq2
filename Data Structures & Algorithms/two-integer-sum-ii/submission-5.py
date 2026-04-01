class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            curTar = target - numbers[i]

            while r >= l:
                mid = l + (r - l) // 2
                if numbers[mid] > curTar:
                    r = mid - 1
                elif numbers[mid] < curTar:
                    l = mid + 1
                else:
                    return [i + 1, mid + 1]
            
    