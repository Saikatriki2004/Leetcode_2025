from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def label_to_rc(s: int) -> (int, int):
            """
            Convert a 1-based square label s (1 <= s <= n*n) into (row, col)
            on the n×n board, given that labels start at board[n−1][0] = 1
            and wind back-and-forth across each row.
            """
            s -= 1
            row_from_bottom = s // n
            col_in_row = s % n
            row = n - 1 - row_from_bottom
            # If row_from_bottom is even, we go left→right; if odd, right→left.
            if row_from_bottom % 2 == 0:
                col = col_in_row
            else:
                col = n - 1 - col_in_row
            return row, col

        # BFS queue will store (current_label, moves_so_far).
        q = deque()
        q.append((1, 0))
        visited = [False] * (n * n + 1)
        visited[1] = True

        while q:
            curr_label, moves = q.popleft()
            if curr_label == n * n:
                # Reached the final square.
                return moves

            # Try all possible die rolls from 1 to 6 steps ahead.
            for step in range(1, 7):
                nxt = curr_label + step
                if nxt > n * n:
                    break

                # Map "nxt" into board coordinates.
                r, c = label_to_rc(nxt)
                # If there's a snake or ladder, follow it once.
                if board[r][c] != -1:
                    nxt = board[r][c]

                if nxt == n * n:
                    return moves + 1

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, moves + 1))

        # If BFS completes without reaching n*n, it’s impossible.
        return -1
