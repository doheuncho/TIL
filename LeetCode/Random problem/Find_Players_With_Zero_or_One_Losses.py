# https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        result = [[], []]
        dic = collections.defaultdict(int)
                
        for winner, loser in matches:
            dic[winner]
            dic[loser] += 1
            
        for player in dic:
            if dic[player] == 0:
                result[0].append(player)
            elif dic[player] == 1:
                result[1].append(player)
        
        result[0].sort()
        result[1].sort()
        
        return result
