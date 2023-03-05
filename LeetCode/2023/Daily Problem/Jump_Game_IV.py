# https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        iloc = collections.defaultdict(list)
        for i , n in enumerate(arr):
            iloc[n].append(i)

        n = len(arr)
        visited, start, end = {0},{0}, {n - 1}
        step = 1

        while start:
            next_steps = set()
            while start:
                i = start.pop()
                for next_step in [i - 1, i + 1] + iloc[arr[i]]:
                    if next_step in end:
                        return step
                    if next_step in visited:
                        continue
                    if not 0 <= next_step < n:
                        continue
                    visited.add(next_step)
                    next_steps.add(next_step)
                del iloc[arr[i]]

            start = next_steps
            if start:
                step = step + 1

        return -1
    