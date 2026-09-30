class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            half = int((right + left) /  2)
            if matrix[half][0] <= target and matrix[half][len(matrix[half]) - 1] >= target:
                sub_left = 0
                sub_right = len(matrix[half]) - 1
                while sub_left <= sub_right:
                    sub_half = int((sub_left + sub_right) / 2)
                    if matrix[half][sub_half] == target:
                        return True
                    elif matrix[half][sub_half] > target:
                        sub_right = sub_half - 1
                    else:
                        sub_left = sub_half + 1
                return False

            elif matrix[half][0] > target:
                right = half - 1
            else:
                left = half + 1
        return False