# https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_neighbor(bomb1: List[int], bomb2: List[int]) -> Tuple[bool]:
            dist = (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2
            
            return dist <= bomb1[2] ** 2, dist <= bomb2[2] ** 2

        n = len(bombs)
        result = 0        
        neighbors = collections.defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                bomb_i, bomb_j = bombs[i], bombs[j]
                j_in_i, i_in_j = is_neighbor(bomb_i, bomb_j)

                if j_in_i:
                    neighbors[i].append(j)
                if i_in_j:
                    neighbors[j].append(i)

        for i in range(n):
            visited = set()
            queue = [i]
            detonated = 0
            while queue:
                cur = queue.pop()
                if cur not in visited:
                    visited.add(cur)
                    detonated += 1
                    for neighbor in neighbors[cur]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                
            result = max(detonated, result)
        
        return result
    