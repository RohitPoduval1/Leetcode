class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = defaultdict(set)  # map the row number to the numbers we have seen in the row 
        cols_seen = defaultdict(set)  # map the column number to the numbers we have seen in the column 
        squares_seen = defaultdict(set)  

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue
                if (
                    val in rows_seen[r]
                    or val in cols_seen[c]
                    or val in squares_seen[(r // 3, c // 3)]
                ):
                    return False

                cols_seen[c].add(val)
                rows_seen[r].add(val)
                squares_seen[(r // 3, c // 3)].add(val)

        return True