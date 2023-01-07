# https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        result = cur_gas = total_gas = 0

        for i in range(n):
            cur_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]
            
            if cur_gas < 0:
                result = i + 1
                cur_gas = 0
        
        if total_gas >= 0:
            return result
        
        return -1
