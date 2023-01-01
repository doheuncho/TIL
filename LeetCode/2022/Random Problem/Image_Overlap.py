# https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        set_1 = set()
        set_2 = set()
        
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    set_1.add((i, j))
                if img2[i][j]:
                    set_2.add((i,j))
                    
        move = {}
        
        for i, j in set_1:
            for x, y in set_2:
                move[(x-i, y-j)] = move.get((x-i, y-j), 0) + 1
        
        if not move:
            return 0
        
        return max(move.values())
