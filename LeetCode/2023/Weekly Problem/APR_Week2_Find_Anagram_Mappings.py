# https://leetcode.com/problems/find-anagram-mappings/

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = collections.defaultdict(list)        
        
        for i, num in enumerate(nums2):
            dic[num].append(i)
        
        return [dic[num].pop() for num in nums1]
    