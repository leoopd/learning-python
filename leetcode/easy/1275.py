# 1275. Find Winner on a Tic Tac Toe Game

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for i, move in enumerate(moves):
            if i%2 == 0:
                board[move[0]][move[1]] = "A"
            else:
                board[move[0]][move[1]] = "B"

        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return board[0][0]
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return board[0][2]

        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                return board[0][i]
            elif board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                return board[i][0]
        if len(moves) < 9:
            return "Pending"
        return "Draw"
