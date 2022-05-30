# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_NUM = 2147483647
        MIN_NUM = -2147483648
        HALF_MIN = -1073741824
        
        # overflow case
        if dividend == MIN_NUM and divisor == -1:
            return MAX_NUM
        
        negative = False
        
        if dividend > 0:
            dividend = -dividend
            negative = True
        
        if divisor > 0:
            divisor = - divisor
            if negative:
                negative = False
            else:
                negative = True
        
        quotient = 0
        
        while divisor >= dividend:
            power_of_two = -1
            value = divisor
            
            while value >= HALF_MIN and value + value >= dividend:
                value += value
                power_of_two += power_of_two
            
            quotient += power_of_two
            dividend -= value
        
        if negative:
            return quotient
        else:
            return -quotient
