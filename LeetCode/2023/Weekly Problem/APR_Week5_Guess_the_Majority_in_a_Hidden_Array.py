# https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/

# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        query1, query2 = reader.query(0, 1, 2, 3), reader.query(0, 1, 2, 4)
        i = 5

        if query1 == query2:
            diff_with_3, same_with_3 = 0, 2
        else:
            diff_with_3, same_with_3 = 1, 1
            diff_idx = 4

        while i < n:
                if query1 == reader.query(0, 1, 2, i):
                    same_with_3 += 1
                else:
                    diff_with_3 += 1
                    diff_idx = i
                i += 1
        
        if query1 == 4:
            same_with_3 += 3
        elif query1 == 0:
            same_with_3 += 1
            diff_with_3 += 2
        else:
            if query1 == query2:
                query3 = reader.query(1, 2, 3, 4)
                if query3 == query1:
                    same_with_3 += 2
                    diff_with_3 += 1
                else:
                    diff_idx = 0
                    if query3 == 4:
                        same_with_3 += 2
                        diff_with_3 += 1
                    else:
                        diff_with_3 += 3
            else:
                if query2 == 4:
                    diff_with_3 += 3
                    diff_idx = 0
                elif query2 == 0:
                    diff_with_3 += 1
                    same_with_3 += 2
        
        if diff_with_3 == same_with_3:
            return -1
        elif diff_with_3 < same_with_3:
            return 3
        else:
            return diff_idx
        