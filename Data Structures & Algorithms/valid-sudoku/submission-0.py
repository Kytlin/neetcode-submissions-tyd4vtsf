from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        has_seen = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                in_cur_row = board[i][j] in has_seen[f'r{i}']
                in_cur_col = board[i][j] in has_seen[f'c{j}']
                in_cur_box = board[i][j] in has_seen[f'box{(i // 3) * 3 + (j // 3)}']
                
                if in_cur_row or in_cur_col or in_cur_box:
                    return False
                has_seen[f'r{i}'].append(board[i][j])
                has_seen[f'c{j}'].append(board[i][j])
                has_seen[f'box{(i // 3) * 3 + (j // 3)}'].append(board[i][j])
        return True