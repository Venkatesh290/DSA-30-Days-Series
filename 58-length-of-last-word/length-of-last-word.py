class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        count = 0
        for char in reversed(s):
            if char == " ":
                break
            count += 1
        return count
