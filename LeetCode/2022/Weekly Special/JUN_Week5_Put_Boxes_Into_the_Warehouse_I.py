# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        result = 0
        boxes.sort()
        
        for i in range(1, len(warehouse)):
            if warehouse[i-1] < warehouse[i]:
                warehouse[i] = warehouse[i-1]
        
        for i in range(len(warehouse)-1, -1, -1):
            if result < len(boxes) and boxes[result] <= warehouse[i]:
                result += 1
        
        return result
    