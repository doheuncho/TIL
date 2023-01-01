# https://leetcode.com/problems/shortest-distance-to-target-color/

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        result = []
        
        for i, color in enumerate(colors):
            dic[color].append(i)
        
        for i, color in queries:
            if color not in dic:
                result.append(-1)
            else:
                index = bisect.bisect(dic[color], i)
                left = min(index-1, len(dic[color]) - 1)
                right = min(index, len(dic[color]) - 1)
                
                result.append(min(abs(i - dic[color][left]), abs(i - dic[color][right])))
        
        return result
    