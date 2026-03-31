class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        has_seen = set()

        # check rows
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and board[i][j] in has_seen:
                    return False
                has_seen.add(board[i][j])
            has_seen.clear()

        # check cols
        for j in range(9):
            for i in range(9):
                if board[i][j] != "." and board[i][j] in has_seen:
                    return False
                has_seen.add(board[i][j])
            has_seen.clear()

        # check squares
        for i in range(3):
            for j in range(3):
                for k in range(9):
                    x, y = 3*i+(k//3), 3*j+(k%3)
                    if board[x][y] != "." and board[x][y] in has_seen:
                        return False
                    has_seen.add(board[x][y])
                has_seen.clear()

        return True