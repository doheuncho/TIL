# https://leetcode.com/problems/push-dominoes/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        status = [0 for _ in range(n)]
        result = ''
        force_to_left = force_to_right = 0

        for i in range(n):
            if dominoes[i] == 'R':
                force_to_right = n
            elif dominoes[i] == 'L':
                force_to_right = 0
            else:
                if force_to_right == 0:
                    force_to_right = 0
                else:
                    force_to_right -= 1
            status[i] += force_to_right
        
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'R':
                force_to_left = 0
            elif dominoes[i] == 'L':
                force_to_left = n
            else:
                if force_to_left == 0:
                    force_to_left = 0
                else:
                    force_to_left -= 1
            status[i] -= force_to_left
        
        for stat in status:
            if stat > 0:
                result += "R"
            elif stat < 0:
                result += "L"
            else:
                result += "."
        
        return result
    