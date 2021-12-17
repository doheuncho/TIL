# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
# Time Limit Exceeded
from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        # 예외 조건
        if not height:
            return 0

        volume = 0
        n = len(height)

        for i in range(n):
            # height[i]기준 좌우 기둥의 높이 최대값
            left_max = 0
            right_max = 0
            # height[0] ~ height[i] 까지 비교하여 가장 높은 높이를 저장
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # height[i] ~ height[n] 까지 비교하여 가장 높은 높이를 저장
            for j in range(i, n):
                right_max = max(right_max, height[j])

            # height[i]에서의 수면의 높이는 left_max, right_max 중 더 낮은 기둥의 높이와 같다.
            volume += min(left_max, right_max) - height[i]

        return volume
