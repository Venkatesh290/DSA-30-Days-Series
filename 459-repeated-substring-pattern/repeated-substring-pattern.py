class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub = s[0:i]
            repeated = sub * (len(s) // len(sub))
            if repeated == s:
                return True
        return False