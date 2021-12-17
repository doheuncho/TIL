# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums_length = len(nums)
        # 중복 케이스처리를 위해 정렬
        nums.sort()

        for i in range(nums_length - 2):
            # 합이 0이 되려면 최소 1개의 원소는 0 이하여야 한다.
            if nums[i] > 0:
                break
            # i에 대한 중복 케이스 처리
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 투 포인터 생성
            left, right = i + 1, nums_length - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # 각 pointer 에 대한 중복 케이스 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results
