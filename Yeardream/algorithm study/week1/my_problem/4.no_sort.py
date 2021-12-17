# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 결과를 저장할 set과 중복 케이스 처리를 위한 set 생성.
        result, duplicate = set(), set()
        # 합이 0인 케이스를 판단하기 위한 dictionary 생성
        seen = {}
        for i, val1 in enumerate(nums):
            # 중복 케이스 처리
            if val1 not in duplicate:
                duplicate.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    # 만약 complement가 seen의 key값 중 하나고, 그 value가 i라면, nums[i] + nums[j] + complement = 0이다.
                    if complement in seen and seen[complement] == i:
                        result.add(tuple(sorted((val1, val2, complement))))
                    # nums[j] 값을 key로, i값을 value로 가지는 원소 추가.
                    seen[val2] = i
        return result
