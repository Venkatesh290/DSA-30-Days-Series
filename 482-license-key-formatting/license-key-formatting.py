class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        group = []
        i = len(s)
        while i > 0:
            start = max(0, i - k)
            group.append(s[start:i])
            i -= k
        result = "-".join(reversed(group))
        return result