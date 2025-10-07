from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = (Counter(t) - Counter(s)).popitem()[0]
        return result
        