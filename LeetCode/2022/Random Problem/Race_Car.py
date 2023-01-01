# https://leetcode.com/problems/race-car/

class Solution:
    dp = {0: 0}
    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]

        d = target.bit_length()

        if 2 ** d - 1 == target:
            self.dp[target] = d
        else:
            self.dp[target] = self.racecar(2 ** d - 1 - target) + d + 1
            for n in range(d - 1):
                self.dp[target] = min(self.dp[target], self.racecar(target - 2 ** (d - 1) + 2 ** n) + d + n + 1)
        
        return self.dp[target]
    