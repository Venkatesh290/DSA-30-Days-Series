class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo <= hi:
            mid = (lo + hi) // 2
            need = mid * (mid + 1) // 2
            if need == n:
                return mid
            if need <= n:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi