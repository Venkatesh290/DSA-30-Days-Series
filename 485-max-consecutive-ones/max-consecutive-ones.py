class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
            else:
                current_count = 0
            max_count = max(max_count, current_count)
        return max_count