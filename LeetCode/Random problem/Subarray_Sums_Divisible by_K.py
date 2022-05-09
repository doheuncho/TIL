# Subarray Sums Divisible by K

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = cur_sum = 0
        remain_dict = collections.defaultdict(int)
        remain_dict[0] = 1
        
        for num in nums:
            cur_sum += num
            result += remain_dict[cur_sum % k]
            remain_dict[cur_sum % k] += 1
        
        return result
        