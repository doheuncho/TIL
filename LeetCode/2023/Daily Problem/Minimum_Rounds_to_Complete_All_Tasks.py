# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        result = 0
        counter = collections.Counter(tasks)
        
        for task in counter.values():
            if task == 1:
                return -1
            else:
                result += (task + 2) // 3
        
        return result
