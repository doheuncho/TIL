# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for directory in path:
            if not directory:
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            elif directory != '.':
                stack.append(directory)

        return '/' + '/'.join(stack)
        