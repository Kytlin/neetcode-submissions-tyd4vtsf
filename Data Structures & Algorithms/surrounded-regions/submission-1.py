class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def dfs(coord_x, coord_y):
            queue = deque()
            queue.append((coord_x, coord_y))
            board[coord_x][coord_y] = "-"

            while queue:
                coord_x, coord_y = queue.popleft()
                for step_x, step_y in directions:
                    res_x, res_y = coord_x + step_x, coord_y + step_y
                    out_of_bounds = not (0 <= res_x < rows and 0 <= res_y < cols)
                    if not out_of_bounds and board[res_x][res_y] == "O":
                        queue.append((res_x, res_y))
                        board[res_x][res_y] = "-"

        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][-1] == "O":
                dfs(i, cols-1)
        
        for i in range(cols):
            if board[0][i] == "O":
                dfs(0, i)
            if board[-1][i] == "O":
                dfs(rows-1, i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "-":
                    board[i][j] = "O"
        