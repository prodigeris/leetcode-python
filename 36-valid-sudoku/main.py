from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkIfListUnique(lis: List[str]) -> bool:
            existing = {}
            for i in lis:
                if i == ".":
                    continue
                if i in existing:
                    return False
                existing[i] = True
            return True

        for i in range(len(board)):
            if not checkIfListUnique(board[i]):
                return False
            col = []
            for j in range(len(board[0])):
                col.append(board[j][i])
            if not checkIfListUnique(col):
                return False

        block = []
        for i in range(3):
            for k in range(3):
                for j in range(3):
                    for z in range(3):
                        block.append(board[i * 3+j][k * 3+z])
                        if len(block) == 9:
                            if not checkIfListUnique(block):
                                return False
                            block = []
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(board))
