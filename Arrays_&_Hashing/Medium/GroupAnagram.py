"""
===========================================================
 GROUP ANAGRAMS — MULTIPLE METHODS WITH FULL EXPLANATION
===========================================================

📌 Problem Summary:
Given an array of strings, group all the anagrams together.

An anagram is a word formed by rearranging the letters of
another word. Example:
    "eat", "tea", "ate" → all are anagrams

Your task:
    Input:  ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

You must return a list of groups, where each group contains
strings that are anagrams of each other.

This file includes TWO methods:

    1. Sorting Method (O(m * n log n))
    2. Hash Table — Character Count Method (O(m * n))

Where:
    m = number of strings
    n = max length of a string
"""

from typing import List
from collections import defaultdict


# ===========================================================
# 1. SORTING METHOD
# ===========================================================
class SolutionSorting:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — SORTING EACH STRING
    ----------------------------------------------------------
    Intuition:
    Two strings are anagrams if they contain the same characters
    in a different order. If we sort the characters inside each
    string, all anagrams will transform into the *same* string.

    Example:
        "eat" → "aet"
        "tea" → "aet"
        "ate" → "aet"

    Therefore, we use the sorted string as a key in a hash map.

    Algorithm:
        1. Create dictionary: sorted_string → list of original strings
        2. For each string:
               sort characters
               use sorted version as a key
               append the string to its group
        3. Return all hash map values

    Time Complexity:
        O(m * n log n)
        Sorting each string of length n takes n log n, repeated m times.

    Space Complexity:
        O(m * n)
        We store all strings in the output structure.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list) automatically creates an empty list when key doesn't exist
        res = defaultdict(list)

        for s in strs:
            # Sort the string to get a canonical key
            # Example: "tea" → ['a','e','t'] → "aet"
            sorted_key = ''.join(sorted(s))

            # Append original string to its anagram group
            res[sorted_key].append(s)

        # Return all grouped anagrams
        return list(res.values())


# ===========================================================
# 2. HASH TABLE — CHARACTER COUNT METHOD
# ===========================================================
class SolutionHashCount:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — HASH BY CHARACTER FREQUENCY
    ----------------------------------------------------------
    Intuition:
    Sorting costs O(n log n). But we can do EVEN BETTER.

    All input strings use only lowercase English letters.
    That means each word can be represented by a 26-length
    frequency array showing how many times each letter appears.

    Example:
        "eat" → 1 'a', 1 'e', 1 't'
        "tea" → same frequency
        "ate" → same frequency

    The frequency array uniquely identifies an anagram group.

    Algorithm:
        1. For each string:
            - Create a count array of size 26 (initially zeros)
            - For each char, increment count[char - 'a']
            - Convert the array to a tuple (hashable key)
            - Append the string to the dictionary[key]
        2. Return all values of the dictionary

    Time Complexity:
        O(m * n)
        We iterate through each character once.

    Space Complexity:
        Extra Space: O(m)
            One tuple key per string
        Output Space: O(m * n)
            All strings stored in grouped lists
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26  # frequency array for 'a' to 'z'

            # Fill frequency array
            for char in s:
                count[ord(char) - ord('a')] += 1

            # Convert to tuple so it can be used as dict key
            key = tuple(count)

            # Add original string to its group
            res[key].append(s)

        return list(res.values())


# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("Sorting Method:")
    print(SolutionSorting().groupAnagrams(words))

    print("\nCharacter Count Method:")
    print(SolutionHashCount().groupAnagrams(words))
