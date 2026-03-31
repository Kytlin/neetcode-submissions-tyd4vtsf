class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # fresh_fruits = set()
        fresh_fruits = 0
        rotten_pile = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                    # fresh_fruits.add((i,j))
                if grid[i][j] == 2:
                    rotten_pile.append((i,j))

        directions = ((-1,0),(0,-1),(1,0),(0,1))
        time = 0
        while rotten_pile and fresh_fruits:
            for _ in range(len(rotten_pile)):
                i, j = rotten_pile.popleft()

                for step_i, step_j in directions:
                    if (0 <= i+step_i < m and 0 <= j+step_j < n 
                            and grid[i+step_i][j+step_j] == 1):
                            # and (i+step_i,j+step_j) in fresh_fruits):
                        # fresh_fruits.remove((i+step_i,j+step_j))
                        fresh_fruits -= 1
                        grid[i+step_i][j+step_j] = 2
                        rotten_pile.append((i+step_i,j+step_j))
            time += 1
            if not fresh_fruits:
                return time

        if not fresh_fruits:
            return time
        return -1