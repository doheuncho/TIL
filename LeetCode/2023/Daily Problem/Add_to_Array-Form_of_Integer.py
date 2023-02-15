# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = "".join(str(digit) for digit in num)
        added = int(num) + k
        return [int(digit) for digit in str(added)]
