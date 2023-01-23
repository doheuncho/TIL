# https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = set(range(1, n+1))
        trust_count = [0] * (n+1)

        for a, b in trust:
            candidates.discard(a)
            trust_count[b] += 1
        
        for candidate in candidates:
            if max(candidate) == n - 1:
                return candidate
               
        return -1
        