# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, result, partition = len(s), [], []

        def dfs(start: int) -> None:
            if start == n:
                result.append(partition.copy())
                return
            for end in range(start, n):
                substring = s[start: end+1]
                if substring == substring[::-1]:
                    partition.append(substring)
                    dfs(end+1)
                    partition.pop()
        dfs(0)

        return result
        