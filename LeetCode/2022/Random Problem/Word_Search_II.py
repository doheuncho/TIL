# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = collections.defaultdict(TrieNode)
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        result = []
        trie = TrieNode()
        
        def helper(row, col, parent):
            character = board[row][col]
            current = parent.children[character]
            if current.word != "":
                result.append(current.word)
                current.word = ""
            board[row][col] = '#'
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for x, y in directions:
                next_row = row + y
                next_col = col + x
                
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    continue
                if board[next_row][next_col] not in current.children:
                    continue
                helper(next_row, next_col, current)
            board[row][col] = character
            if not current.children:
                del parent.children[character]
            return None
        
        for word in words:
            node = trie
            for c in word:
                node = node.children[c]
            node.word = word
        
        for i in range(m):
            for j in range(n):
                character = board[i][j]
                if character in trie.children:
                    helper(i, j, trie)

        return result
