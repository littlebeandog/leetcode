class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        elif board:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if self.search(board, i, j, word):
                        return True
        return False

    def search(self, board, i, j, word):
        if word == '':
            return True
        elif len(board) > i >= 0 and len(board[0]) > j >= 0 and board[i][j] == word[0]:
            keep = board[i][j]
            board[i][j] = None
            res = \
                self.search(board, i - 1, j, word[1:]) or self.search(board, i + 1, j, word[1:]) or self.search(board, i, j - 1, word[1:]) or self.search(board, i, j + 1, word[1:])

            board[i][j] = keep
            return res
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    r = s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    print(r)