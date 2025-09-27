class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        while stack:
            prev = stack.pop()
            next_greater[prev] = -1
        result = [next_greater[num] for num in nums1]
        return result