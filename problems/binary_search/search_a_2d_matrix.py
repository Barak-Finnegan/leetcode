# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][0]:
                l = mid + 1
            if target < matrix[mid][0]:
                r = mid - 1
            if target == matrix[mid][0]:
                return True
        
        target_row = l - 1
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            if target < matrix[target_row][mid]:
                r = mid - 1
            if target == matrix[target_row][mid]:
                return True
        return False
