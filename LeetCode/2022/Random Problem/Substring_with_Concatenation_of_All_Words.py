# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_map = collections.Counter(words)
        results = []
        word_size = len(words[0])
        num_word = len(words)
        sub_size = word_size * num_word
        
        for i in range(len(s) - sub_size + 1):
            seen = dict(word_map)
            word_used = 0
            for start in range(i, i + sub_size, word_size):
                sub_word = s[start: start + word_size]
                if sub_word in seen and seen[sub_word] > 0:
                    seen[sub_word] -= 1
                    word_used += 1
                else:
                    break
            if word_used == num_word:
                results.append(i)
        
        return results
    