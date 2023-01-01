# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        
        for i in range(len(self.vector)):
            result += self.vector[i] * vec.vector[i]
            
        return result
