class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
