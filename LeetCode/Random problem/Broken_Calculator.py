# https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equivalents = {}
        
        def find(x):
            if x not in equivalents:
                return x
            else:
                return find(equivalents[x])
            
        for equation in equations:
            if equation[1] == "=":
                x = equation[0]
                y = equation[3]
                
                if find(x) != find(y):
                    equivalents[find(y)] = find(x)
                    
        for equation in equations:
            if equation[1] == "!" and find(equation[0]) == find(equation[3]):
                return False
            
        return True
    