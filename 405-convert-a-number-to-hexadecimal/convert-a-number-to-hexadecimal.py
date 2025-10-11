class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        res = ""
        num &= 0xFFFFFFFF
        while num > 0:
            digit = num % 16
            res = hex_chars[digit] + res
            num //= 16
        return res