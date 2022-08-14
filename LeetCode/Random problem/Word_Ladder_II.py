# https://leetcode.com/problems/word-ladder-ii/

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        queue = [beginWord]
        parents = collections.defaultdict(list)
        
        while queue:
            child = set()
            for word in queue:
                for i in range(len(beginWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            child.add(next_word)
                            parents[next_word].append(word)
            if endWord in child:
                break
            wordList -= child
            queue = child
        result = []
        
        def dfs(node, path):
            if node == beginWord:
                result.append(path[::-1])
                return None
            for parent in parents[node]:
                dfs(parent, path + [parent])
            return None
                
        dfs(endWord, [endWord])     
        
        return result
