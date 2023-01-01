# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []

        for query in queries:
            maximum_size = 0
            for num in nums:
                if query >= num:
                    query -= num
                    maximum_size += 1
                else:
                    break
            result.append(maximum_size)
        
        return result
