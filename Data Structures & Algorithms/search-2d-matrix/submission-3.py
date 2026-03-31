class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False
        
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(matrix[0])-1
        while left <= right:
            center = left + (right-left) // 2
            if matrix[mid][center] == target:
                return True
            elif target > matrix[mid][center]:
                left = center + 1
            else:
                right = center - 1

        return False