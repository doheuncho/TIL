# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cur = ''
        i = 0
        result = [[] for _ in range(len(searchWord))]
        
        for char in searchWord:
            cur += char
            i += 1
            for product in products:
                if cur == product[:i]:
                    result[i-1].append(product)
                if len(result[i-1]) == 3:
                    break
        
        return result
        