# https://leetcode.com/problems/prefix-and-suffix-search/

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
class WordFilter:
    def __init__(self, words):
        self.dic = {}
        for i, word in enumerate(words):
            for pre, suf in product(range(len(word) + 1), repeat=2):
                self.dic[(word[:pre], word[suf:])] = i

    def f(self, prefix, suffix):
        return self.dic.get((prefix, suffix), -1)
