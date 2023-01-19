# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, n: int) -> bool:
        n = str(n)
        rotate_dic = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        rotated = ""

        for num in n:
            if num not in rotate_dic:
                return False
            rotated += rotate_dic[num]

        return rotated[::-1] != n
