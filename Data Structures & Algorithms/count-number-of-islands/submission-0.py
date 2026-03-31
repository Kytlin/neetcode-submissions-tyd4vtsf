class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = set()
        m, n = len(grid), len(grid[0])

        def traverse_island(row, col):
            if not (0 <= row < m and 0 <= col < n) or (row,col) in visited or grid[row][col] == "0":
                return

            visited.add((row,col))

            traverse_island(row-1,col)
            traverse_island(row,col-1)
            traverse_island(row+1,col)
            traverse_island(row,col+1)

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == "1":
                    island_count += 1
                    traverse_island(i,j)

        return island_count