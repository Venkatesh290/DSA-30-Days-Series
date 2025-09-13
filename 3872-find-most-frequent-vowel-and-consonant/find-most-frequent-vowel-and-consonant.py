class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        vowels_count = {}
        consonants_count = {}
        for char in s:
            if char in vowel_set:
                vowels_count[char] = vowels_count.get(char, 0) + 1
            else:
                consonants_count[char] = consonants_count.get(char, 0) + 1
        max_vowel = max(vowels_count.values()) if vowels_count else 0
        max_consonant = max(consonants_count.values()) if consonants_count else 0
        count = max_vowel + max_consonant
        return count
