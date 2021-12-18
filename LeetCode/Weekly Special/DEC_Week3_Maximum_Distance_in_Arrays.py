# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # 각 array들은 정렬이 되어있으므로 각 array의 첫 val(최솟값)와 마지막 val(최댓값)만을 살펴봐도 된다.
        max_val, max_idx = max((array[-1], index) for index, array in enumerate(arrays))
        min_val, min_idx = min((array[0], index) for index, array in enumerate(arrays))
        
        if max_idx != min_idx:
            return max_val - min_val
        # 만약 하나의 array에서 최댓값과 최솟값이 나온경우는 2번째로 큰 수/작은 수를 이용하여 distance를 구해야한다.
        else:
            second_max_val, second_max_idx = max((array[-1], index) for index, array in enumerate(arrays) if index != max_idx)
            second_min_val, second_min_idx = min((array[0], index) for index, array in enumerate(arrays) if index != min_idx)
            
            return max((max_val - second_min_val), (second_max_val - min_val))
