# leetcode는 아래 모듈들을 미리 import함
# 메모리 : 15.8 MB
# 시간 : 87 ms
from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 스택에 값이 있을 때, 이전 위치(stack[-1])의 높이가 현재의 높이(height[i])를 비교
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                # 만약 pop한 후의 stack이 비어있다면 distance가 0이므로 바로 반복문을 탈출한다.
                if not len(stack):
                    break
                # water는 수면의 높이와 top의 높이의 차를 나타낸다.,
                water = min(height[i], height[stack[-1]]) - height[top]
                # water높이만큼의 물이 얼마나 넓게 고여있는지를 확인한다.
                distance = i - stack[-1] - 1
                # 결과값에 앞에서 구한 물의 부피를 더해준다.
                volume += distance * water
            # 스택에 i값 저장
            stack.append(i)

        return volume
