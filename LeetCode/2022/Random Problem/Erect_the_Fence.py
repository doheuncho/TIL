# https://leetcode.com/problems/erect-the-fence/

class Solution:
    # Monotone Chain
    def orientation(self, a: Tuple[int], b: Tuple[int], c: Tuple[int]) -> int:
        return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        stack = []
        
        for point in trees:
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(tuple(point))
        
        for point in trees[::-1]:
            while len(stack) > 1 and self.orientation(stack[-2], stack[-1], point) > 0:
                stack.pop()
            stack.append(tuple(point))
        
        return list(set(stack))
    