# https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damaged = sum(damage) + max(-max(damage), -armor)
        return damaged + 1
