# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate_nums = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }
        
        for i in range(len(num)//2 + 1):
            if num[i] in rotate_nums:
                if rotate_nums[num[i]] != num[len(num)-1-i]:
                    return False
            else:
                return False
        
        return True
                