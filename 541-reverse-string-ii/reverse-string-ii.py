class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        for i in range(0, n, 2*k):
            chunk = s[i:i+2*k]
            first_k = chunk[:k][::-1]
            rest = chunk[k:]
            result.append(first_k + rest)
        return ''.join(result)