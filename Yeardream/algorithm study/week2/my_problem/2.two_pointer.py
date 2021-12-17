# leetcode는 아래 모듈들을 미리 import함
# 메모리 : 15.8 MB
# 시간 : 107 ms
from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        # 예외 조건
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽으로 포인터 이동
            if left_max <= right_max:
                # 완전 탐색 풀이에서의 volume += min(left_max, right_max) - height[i]와 같다.
                volume += left_max - height[left]
                left += 1
            else:
                # 반대의 경우도 같은 매커니즘을 반복한다.
                volume += right_max - height[right]
                right -= 1

        return volume
