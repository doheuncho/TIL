# https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        left, right = 0, len(people) - 1
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            result += 1
        
        return result
