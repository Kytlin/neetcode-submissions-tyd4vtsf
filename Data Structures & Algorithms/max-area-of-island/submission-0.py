class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0]) 
        
        def numLands(row,col):
            if not (0 <= row < m and 0 <= col < n) or (row,col) in visited or grid[row][col] == 0:
                return 0
            # else:
            #     return 1

            count = 1
            visited.add((row,col))

            count += numLands(row-1,col)
            count += numLands(row,col-1)
            count += numLands(row+1,col)
            count += numLands(row,col+1)

            return count

        max_area = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, numLands(i,j))

        return max_area