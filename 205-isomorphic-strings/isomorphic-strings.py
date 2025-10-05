class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
        
            if ch1 in mapST and mapST[ch1] != ch2:
                return False
            if ch2 in mapTS and mapTS[ch2] != ch1:
                return False

            mapST[ch1] = ch2
            mapTS[ch2] = ch1

        return True 