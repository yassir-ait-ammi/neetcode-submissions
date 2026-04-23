class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix)
        hight = rows * cols - 1
        low = 0
        while low <= hight:
            mid = low + (hight - low) // 2
            cols = len(matrix[0])
            i = mid // cols
            j = mid % cols
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                low = mid + 1
            else:
                hight = mid - 1
        return False