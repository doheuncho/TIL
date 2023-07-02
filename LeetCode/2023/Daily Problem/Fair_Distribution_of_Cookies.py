# https://leetcode.com/problems/fair-distribution-of-cookies/


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.result = float("inf")
        cookies.sort(reverse=True)

        def dfs(idx: int, groups: List[int]) -> None:
            if idx == len(cookies):
                self.result = min(self.result, max(groups))
                return
            for i in range(k):
                if groups[i] + cookies[idx] < self.result:
                    groups[i] += cookies[idx]
                    dfs(idx + 1, groups)
                    groups[i] -= cookies[idx]

        dfs(0, [0] * k)

        return self.result
