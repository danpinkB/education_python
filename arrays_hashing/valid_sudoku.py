class Solution(object):
    def isValidSudoku(self, board):
        cols = [set() for x in range(9)]
        rows = [set() for x in range(9)]
        squares = [[set() for x in range(3)] for y in range(3)]
        element = '.'
        for x in range(9):
            for y in range(9):
                element = board[x][y]
                if element == '.': continue
                if element in cols[x] or element in rows[y] or element in squares[x//3][y//3]:return False
                cols[x].add(element)
                rows[y].add(element)
                squares[x//3][y//3].add(element)
        return False


if __name__ == "__main__":
    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
