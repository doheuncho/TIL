# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_length = len(nums)
        # 중복 케이스처리를 위해 정렬
        nums.sort()

        # 반복문을 통한 완전탐색, i <= j <= k 순으로 선택한다.
        for i in range(nums_length - 2):
            # 합이 0이 되려면 최소 1개의 원소는 0 이하여야 한다.
            if nums[i] > 0:
                break
            # i 에 대한 중복 케이스 처리
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, nums_length - 1):
                # j 에 대한 중복 케이스 처리
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j + 1, nums_length):
                    # k 에 대한 중복 케이스 처리
                    if k > j + 1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
        return result
