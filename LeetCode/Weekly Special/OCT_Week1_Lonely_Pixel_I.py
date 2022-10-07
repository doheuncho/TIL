# https://leetcode.com/problems/lonely-pixel-i/

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        n, m = len(picture), len(picture[0])
        result = 0
        
        for j in range(m):
            found=False
            for i in range(n):
                if picture[i][j]=='B':
                    if found or picture[i].count('B')!=1:
                        found=False
                        break
                    found=True
            if found:
                result += 1
        
        return result
        