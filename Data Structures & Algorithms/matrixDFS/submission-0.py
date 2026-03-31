class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            land_visited = (row, col) in visited
            if not (0 <= row < m and 0 <= col < n) or land_visited or grid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1

            visited.add((row, col))

            count = 0
            count += dfs(row-1,col)
            count += dfs(row,col-1)
            count += dfs(row+1,col)
            count += dfs(row,col+1)
            
            visited.remove((row, col))

            return count
    
        return dfs(0,0)