class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def dfs(coord_x, coord_y):
            queue = deque()
            queue.append((coord_x, coord_y))
            visited.add((coord_x, coord_y))
            board[coord_x][coord_y] = "-"

            modify = True
            while queue:
                coord_x, coord_y = queue.popleft()
                for step_x, step_y in directions:
                    res_x, res_y = coord_x + step_x, coord_y + step_y
                    out_of_bounds = not (0 <= res_x < rows and 0 <= res_y < cols)
                    if not out_of_bounds and board[res_x][res_y] == "O":
                        queue.append((res_x, res_y))
                        visited.add((res_x, res_y))
                        board[res_x][res_y] = "-"
                    elif out_of_bounds:
                        modify = False

            final_sign = "X" if modify else "O"

            queue.append((coord_x, coord_y))
            board[coord_x][coord_y] = final_sign

            while queue:
                coord_x, coord_y = queue.popleft()
                for step_x, step_y in directions:
                    res_x, res_y = coord_x + step_x, coord_y + step_y
                    out_of_bounds = not (0 <= res_x < rows and 0 <= res_y < cols)
                    if not out_of_bounds and board[res_x][res_y] == "-":
                        queue.append((res_x, res_y))
                        board[res_x][res_y] = final_sign

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j)
        