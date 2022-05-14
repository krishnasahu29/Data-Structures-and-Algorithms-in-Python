from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        # find the next position in the state to populate
        position = len(state)
        candidates = set(range(n))

        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if its occupied
            candidates.discard(col)
            dist = position - row

            # discard diagonals
            candidates.discard(col + dist)
            candidates.discard(col - dist)

        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_str = self.state_to_str(state, n)
            solutions.append(state_str)
            return

        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_str(self, state, n):

        # eg. [1, 3, 0, 2]
        # output: ".Q..","...Q","Q...","..Q."

        ret = []
        for i in state:
            s = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(s)

        return ret
