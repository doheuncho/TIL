# https://leetcode.com/problems/word-abbreviation/

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviation(word, i=0):
            if len(word) - i <= 3:
                return word
            else:
                return word[:i + 1] + str(len(word) - i - 2) + word[-1]
        
        n = len(words)
        result = [abbreviation(word) for word in words]
        prefix = [0] * n

        for i in range(n):
            while True:
                dupes = set()
                for j in range(i + 1, n):
                    if result[i] == result[j]:
                        dupes.add(j)

                if not dupes:
                    break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    result[k] = abbreviation(words[k], prefix[k])

        return result
