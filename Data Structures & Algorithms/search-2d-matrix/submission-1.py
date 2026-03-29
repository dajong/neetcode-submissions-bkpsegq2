class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml, mr = 0, len(matrix) - 1
        nl, nr = 0, len(matrix[0]) - 1

        while mr >= ml:
            midM = ml + ((mr - ml) // 2)
            if target < matrix[midM][0]:
                mr = midM - 1
            elif target > matrix[midM][len(matrix[0]) - 1]:
                ml = midM + 1
            else:
                while nr >= nl:
                    midN = nl + ((nr - nl) // 2)

                    if target < matrix[midM][midN]:
                        nr = midN - 1
                    elif target > matrix[midM][midN]:
                        nl = midN + 1
                    else:
                        return True
                break
        return False