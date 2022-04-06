# https://leetcode.com/problems/brace-expansion/

class Solution:
    def expand(self, s: str) -> List[str]:
        result = ['']
        
        while s:
            if s[0] == '{':
                end = s.index('}')
                brace = s[1:end].split(',')
                result = [r + b for b in brace for r in result]
                
                s = s[end+1:]
            else:
                result = [r + s[0] for r in result]
                s = s[1:]
        
        return sorted(result)
    