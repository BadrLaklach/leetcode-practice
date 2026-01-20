"""
===========================================================
    VALID PALINDROME — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward.

Example:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

This file includes TWO methods:
    1. Reverse String Method (O(n) Time, O(n) Space)
    2. Two Pointers Method (O(n) Time, O(1) Space - Optimal)
"""

from typing import List

# ===========================================================
# 1. REVERSE STRING METHOD
# ===========================================================
class SolutionReverse:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — CLEAN AND REVERSE
    ----------------------------------------------------------
    Intuition:
    Build a new string containing only the valid characters (letters 
    and digits) in lowercase. A string is a palindrome if it is 
    identical to its reversed version.

    Algorithm:
        1. Iterate through every character.
        2. If c.isalnum(), append c.lower() to a list/string.
        3. Compare the result with result[::-1].

    Time Complexity:  O(n)
    Space Complexity: O(n) - stores a cleaned version of the string
    """
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


# ===========================================================
# 2. TWO POINTERS METHOD (OPTIMIZED)
# ===========================================================
class SolutionTwoPointers:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — TWO POINTERS (IN-PLACE)
    ----------------------------------------------------------
    Intuition:
    Avoid extra space by using two pointers (left and right). 
    Skip non-alphanumeric characters on both ends and compare 
    the valid characters directly.

    

    Algorithm:
        1. Initialize l = 0, r = len(s) - 1.
        2. While l < r:
            - Skip non-alphanumeric chars at l.
            - Skip non-alphanumeric chars at r.
            - Compare s[l].lower() and s[r].lower().
            - If match, move both pointers inward.
        3. Return True if the loop completes.

    Time Complexity:  O(n)
    Space Complexity: O(1) - No extra storage used
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric from the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Skip non-alphanumeric from the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            
            # Case-insensitive comparison
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c: str) -> bool:
        """Helper to determine if character is alphanumeric."""
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Reverse Method is concise but uses O(n) extra space.
- The Two-Pointers approach is the gold standard for interviews 
  because it achieves O(1) extra space complexity.

IMPORTANT SYNTAX:
1. s.isalnum(): Built-in Python method to check for letters/numbers.
2. s[::-1]: String slicing to reverse a string efficiently.
3. ord(c): Returns the ASCII/Unicode integer for a character.
4. s.lower(): Necessary to ensure case-insensitivity (e.g., 'A' == 'a').
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    test = "race a car"
    sol = SolutionTwoPointers()
    
    print(f"Original: '{test}'")
    print(f"Is Palindrome: {sol.isPalindrome(test)}")