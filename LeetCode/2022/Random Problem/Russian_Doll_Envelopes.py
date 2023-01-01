# https://leetcode.com/problems/russian-doll-envelopes/

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        result = 0
        top = []
        
        for i in range(len(envelopes)):
            cur = envelopes[i][1]
            left, right = 0, result
            
            while left < right :
                mid = (left + right) // 2
                if top[mid] >= cur:
                    right = mid
                else:
                    left = mid + 1
            
            if left >= result:
                result += 1
                top.append(cur)
            else:
                top[left] = cur
        
        return result
