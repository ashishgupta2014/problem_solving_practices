"""
https://app.glider.ai/practice/problem/algorithms/all-palindrome-substrings-/problem

https://www.techiedelight.com/find-possible-palindromic-substrings-string/



For a given string, find all the palindromic sub-strings.

Input
The input contains a string S.

Output
An array of all the palindromic sub-strings.

Constraints
( 1 <= length of S <= 105)

Example #1
Input
abccbaabccba
Output
a b c cc bccb abccba c b a aa baab cbaabc ccbaabcc bccbaabccb abccbaabccba a b c cc bccb abccba c b a
Explanation: For example "abccba" is "abccba[abccba]" this part of S. Consider that single character strings are also palindromes
Example #2
Input
WOWO
Output
W O WOW W OWO O
Explanation: As single character strings are palindromes first W, first O, second W, second O will be different palindromes +
"[WOW]O" this part and "W[OWO]" this part are also palindromes.
"""


# expand in both directions of low and high to find all palindromes
def expand(str, low, high, s):
    # run till str[low.high] is a palindrome
    while low >= 0 and high < len(str) and str[low] == str[high]:
        # push all palindromes into the set
        s.add(str[low: high + 1])

        # expand in both directions
        low = low - 1
        high = high + 1


# Function to find all unique palindromic substrings of given String
def allPalindromicSubStrings(str):
    # create an empty set to store all unique palindromic substrings
    s = set()

    for i in range(len(str)):
        # find all odd length palindrome with str[i] as mid point
        expand(str, i, i, s)

        # find all even length palindrome with str[i] and str[i+1]
        # as its mid points
        expand(str, i, i + 1, s)

    # print all unique palindromic substrings
    print(s)


#######################################################################
"""
https://www.educative.io/m/find-all-palindrome-substrings

Given a string find all non-single letter substrings that are palindromes. For instance:

Solution Explanation
Runtime complexity
The runtime complexity of this solution is polynomial, O(n^{2})O(n
​2
​​ )

Memory complexity
The memory complexity of this solution is constant, O(1).


Solution Breakdown
For each letter in the input string, start expanding to the left and right while checking for even and odd length palindromes. Move to the next letter if we know a palindrome doesn’t exist.

We expand one character to the left and right and compare them. If both of them are equal, we print out the palindrome substring.
"""

######################################################################

def find_palindromes_in_sub_string(input, j, k):
  count = 0
  while j >= 0 and k < len(input):
    if input[j] != input[k]:
      break
    print(input[j: k + 1])
    count += 1

    j -= 1
    k += 1

  return count


def find_all_palindrome_substrings(input):
  count = 0
  for i in range(0, len(input)):
    count += find_palindromes_in_sub_string(input, i - 1, i + 1)
    count += find_palindromes_in_sub_string(input, i, i + 1)

  return count




if __name__ == '__main__':
    str = "google"
    allPalindromicSubStrings(str)
    print("Same problem with little variation")
    s = "aabbbaa";
    print("Total palindrome substrings: ", find_all_palindrome_substrings(s))