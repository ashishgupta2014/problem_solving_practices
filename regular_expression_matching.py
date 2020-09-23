import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p,s)
        if not match:
            return False
        if match.start()==0 and match.end()==len(s):
            return True
        return False
s = Solution()
print(s.isMatch(s='aab', p='c*a*b'))