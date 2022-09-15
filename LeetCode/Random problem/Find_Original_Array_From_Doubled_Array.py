# https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        if counter[0] % 2:
            return []
        result = [0 for _ in range(counter[0]//2)]

        for num in sorted(counter.keys()):
            if counter[num] > counter[num*2]:
                return []
            else:
                counter[num*2] -= counter[num]
                for _ in range(counter[num]):
                    result.append(num)
        
        return result
        