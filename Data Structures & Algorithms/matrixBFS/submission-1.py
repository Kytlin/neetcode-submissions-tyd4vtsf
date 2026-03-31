from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))

        directions = ((-1,0),(0,-1),(1,0),(0,1))

        length = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == m-1 and j == n-1:
                    return length

                for step_i, step_j in directions:
                    if (0 <= i+step_i < m and 0 <= j+step_j < n 
                            and (i+step_i,j+step_j) not in visited  
                            and grid[i+step_i][j+step_j] == 0):
                        queue.append((i+step_i,j+step_j))
                        visited.add((i,j))
            length += 1
        return -1