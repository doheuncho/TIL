# https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        num = list(num)
        result = []
        used = []

        counter = defaultdict(deque)
        
        for i, c in enumerate(num):
            counter[int(c)].append(i)
	    
        if k >= n**2:
            return ''.join(sorted(num))
        
        for _ in range(n):
            for i in range(10):
                if counter[i]:
                    index = counter[i][0]
                    offset = bisect.bisect_left(used, index)
                    if index - offset <= k:
                        k -= (index - offset)
                        result.append(i)
                        used.insert(offset, counter[i].popleft())
                        break
                        
        return ''.join(map(str, result))
    