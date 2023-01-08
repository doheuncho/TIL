# https://leetcode.com/problems/max-points-on-a-line/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        
        result = 2
        
        def find_gcd(x, y):
            return find_gcd(y, x%y) if y != 0 else x
        
        for i in range(n):
            dic = collections.defaultdict(int)
            for j in range(i+1, n):
                dx = points[i][0]-points[j][0]
                dy = points[i][1]-points[j][1]
                gcd = find_gcd(dx, dy)
                gradient = (dx//gcd, dy//gcd)
                dic[gradient] += 1
                
            for v in dic.values():
                result = max(result, 1+v)

        return result
