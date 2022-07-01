# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        result = 0
        
        for box_count, box_type in boxTypes:
            box_count = min(truckSize, box_count)
            result += box_count * box_type
            truckSize -= box_count
            
            if truckSize == 0:
                break
        
        return result
    