# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for directory in path:
            if not directory:
                continue
            elif directory != '.':
                stack.append(directory)
            elif directory == '..':
                if stack:
                    stack.pop()

        return '/' + '/'.join(stack)
        