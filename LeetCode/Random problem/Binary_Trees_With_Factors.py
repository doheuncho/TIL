# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dic = collections.defaultdict(int)
        modulo = 10 ** 9 + 7
        arr.sort()

        for i, num in enumerate(arr):
            dic[num]= 1
            for child1 in arr[:i]:
                if num % child1 == 0:
                    child2 = num//child1
                    dic[num] += dic[child1] * dic[child2]

        return sum(dic.values()) % modulo
    