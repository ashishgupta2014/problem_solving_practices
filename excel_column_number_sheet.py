class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0;
        for B in range(len(s)):
            result *= 26;
            result += ord(s[B]) - ord('A') + 1;

        return result
s = Solution()
print(s.titleToNumber('ZY'))