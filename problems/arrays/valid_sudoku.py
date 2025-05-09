# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate rows and columns
        for i in range(len(board)):
            valid_i, valid_j = set(), set()
            for j in range(len(board[0])):
                if board[i][j] in valid_i or board[j][i] in valid_j:
                    return False
                if board[i][j] != '.':
                    valid_i.add(board[i][j])
                if board[j][i] != '.':
                    valid_j.add(board[j][i])

        # validate squares
        square_size = 3
        for i in range(0, len(board), square_size):
            for j in range(0, len(board[0]), square_size):
                valid_square = set()
                for sub_i in range(0, square_size):
                    for sub_j in range(0, square_size):
                        target_val = board[i + sub_i][j + sub_j]
                        if target_val == '.':
                            continue
                        if target_val in valid_square:
                            return False
                        valid_square.add(target_val)

        return True
