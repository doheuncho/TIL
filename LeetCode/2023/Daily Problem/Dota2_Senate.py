# https://leetcode.com/problems/dota2-senate/

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiants = collections.deque()
        dires = collections.deque()
        
        for i, c in enumerate(senate):
            if c == "R":
                radiants.append(i)
            else:
                dires.append(i)

        while dires and radiants:
            d, r = dires.popleft(), radiants.popleft()
            
            if d < r:
                dires.append(d+len(senate))
            else:
                radiants.append(r+len(senate))
        
        if radiants:
            return "Radiant"

        return "Dire"
