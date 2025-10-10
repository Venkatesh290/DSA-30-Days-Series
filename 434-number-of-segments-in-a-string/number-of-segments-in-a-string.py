class Solution:
    def countSegments(self, s: str) -> int:
        words = s.split()
        count = 0 
        for word in words:
            count += 1
        return count
