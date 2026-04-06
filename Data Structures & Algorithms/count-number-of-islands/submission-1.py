class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = ((-1,0),(0,-1),(1,0),(0,1)) # south, west, north, east
        queue = deque()
        visited = set()
        def bfs(start):
            queue.append(start)
            while queue:
                cur_y, cur_x = queue.popleft()
                visited.add((cur_y, cur_x))
                for y, x in directions:
                    next_y, next_x = cur_y + y, cur_x + x
                    bound_check = 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0])
                    if bound_check and grid[next_y][next_x] == "1" and (next_y, next_x) not in visited:
                        queue.append((next_y, next_x))
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs((i,j))
                    num_islands += 1
        return num_islands
        