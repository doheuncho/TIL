# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
# 메모리 : 14.1 MB
# 시간 : 31 ms
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = map(list, zip(*matrix[::-1]))
