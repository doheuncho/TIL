# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 케이스 처리를 위해 정렬한다.
        nums.sort()
        for i in range(len(nums)):
            # 합이 0이 되려면 최소 1개의 원소는 0 이하여야 한다.
            if nums[i] > 0:
                break
            # 중복 케이스 처리
            if i == 0 or nums[i - 1] != nums[i]:
                self.twosum(nums, i, result)
        return result

    # 나머지 두 수의 합을 구해 세 수의 합이 0이면 result에 결과를 추가하는 함수.
    def twosum(self, nums: List[int], i: int, result: List[List[int]]):
        # 이전에 살펴본 nums[j]값들을 저장할 set 을 만든다.
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -(nums[i] + nums[j])
            # 만약 complement가 seen의 원소라면, nums[i] + nums[j] + complement = 0이다.
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                # 중복 케이스 처리
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
