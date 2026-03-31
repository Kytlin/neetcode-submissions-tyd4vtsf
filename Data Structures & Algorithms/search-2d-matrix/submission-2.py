class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        left, mid, right = 0, 0, len(matrix)-1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[mid][0] > target:
                right = mid - 1
            elif mid < len(matrix) and matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            else:
                break

        left, right = 0, len(matrix[0])-1
        while left <= right:
            row_mid = left + (right-left)//2
            if matrix[mid][row_mid] > target:
                right = row_mid - 1
            elif matrix[mid][row_mid] < target:
                left = row_mid + 1
            else:
                return True
        return False