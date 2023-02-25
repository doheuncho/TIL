# https://leetcode.com/problems/handshakes-that-dont-cross/

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        result = 1
        for i in range(numPeople // 2):
            result *= numPeople - i
            result //= (i + 1)
        return result // (numPeople // 2 + 1) % (10**9 + 7)
    