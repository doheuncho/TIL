# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = collections.defaultdict(list)

        for c1, c2 in zip(s1, s2):
            graph[c1].append(c2)
            graph[c2].append(c1)
        
        def dfs(char: str, smallest_char: str) -> str:
            if char < smallest_char:
                smallest_char = char
            
            for neighbor in graph[char]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    smallest_char = dfs(neighbor, smallest_char)
            
            return smallest_char
        
        result = ""
        for char in baseStr:
            visited = set(char)
            result += dfs(char, char)
        
        return result
