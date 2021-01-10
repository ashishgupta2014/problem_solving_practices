"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

https://app.glider.ai/practice/problem/algorithms/anagram-substring/problem


Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""



from collections import Counter


def anagram(S, P):
    """

    :param S:
    :param P:
    :return:
    """
    d = Counter(P)
    result = []
    for i, e in enumerate(S):
        x = Counter(S[i:len(P)+i])
        if not (d-x):
            result.append(i)
        #print(i, x, '<==>', d-x)
    return result
print(anagram('BACDGABCDA', 'ABCD'))

class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return
        first = dict()
        second = dict()
        for i in range(len(p)):
            if p[i] not in first:
                first[p[i]] = 1
            else:
                first[p[i]] += 1
        for i in range(len(p)):
            if s[i] not in second:
                second[s[i]] = 1
            else:
                second[s[i]] += 1
        l = []
        if first == second:
            l.append(0)
        for i in range(len(p),len(s)):
            j = i - len(p)
            second[s[j]] -= 1
            if second[s[j]] == 0:
                del second[s[j]]
            if s[i] not in second:
                second[s[i]] = 1
            elif s[i] in second:
                second[s[i]] += 1
            if first == second:
                l.append(j + 1)
        return l
obj = Solution()
print(obj.findAnagrams('BACDGABCDA', 'ABCD'))

