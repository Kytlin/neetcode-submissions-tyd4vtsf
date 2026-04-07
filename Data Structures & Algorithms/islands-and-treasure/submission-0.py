class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        def bfs():
            while queue:
                cur_y, cur_x = queue.pop()
                for y, x in directions:
                    next_y, next_x = cur_y+y, cur_x+x
                    bound_check = 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0])
                    if (bound_check and grid[next_y][next_x] > grid[cur_y][cur_x]): 
                        grid[next_y][next_x] = grid[cur_y][cur_x] + 1
                        queue.append((next_y,next_x))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        bfs()