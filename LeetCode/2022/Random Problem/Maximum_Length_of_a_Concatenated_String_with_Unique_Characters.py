# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        concatenated = [""]
        result = 0
        
        for word in arr:
            for concatenation in concatenated:
                cur = concatenation + word
                
                if len(cur) > len(set(cur)):
                    continue
                else:
                    concatenated.append(cur)
                    result = max(result, len(cur))
                    
        return result
    