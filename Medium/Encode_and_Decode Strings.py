"""
===========================================================
    ENCODE AND DECODE STRINGS — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Design an algorithm to encode a list of strings into a single string.
This encoded string must be decodable back into the original list, 
even if the strings contain characters like "#", ",", or spaces.

Example:
    Input:  ["hello", "world"]
    Encoded: "5,5,#helloworld" (Method 1) or "5#hello5#world" (Method 2)

This file includes TWO methods:
    1. Header Metadata Method (Lengths at the start)
    2. Length-Prefix Method (Length before each individual word)
"""

from typing import List

# ===========================================================
# 1. HEADER METADATA METHOD
# ===========================================================
class SolutionHeader:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — HEADER METADATA
    ----------------------------------------------------------
    Intuition:
    We store all the "instructions" (lengths of the words) at 
    the very beginning of the string, separated by a unique 
    marker (like '#'). This acts as a map for the decoder.

    Algorithm:
        Encode:
            1. Iterate through strings to get all lengths.
            2. Build a header string: "len1,len2,len3,#"
            3. Append all original strings back-to-back.
        Decode:
            1. Read the header to extract the list of lengths.
            2. After the '#', use those lengths to slice the string.

    Time Complexity:  O(N)
    Space Complexity: O(N)
    """

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, res = [], ""
        # Pass 1: Collect lengths
        for s in strs:
            sizes.append(len(s))
        
        # Pass 2: Build Header (e.g., "5,5,#")
        for wordSize in sizes:
            res += str(wordSize) + ","
        res += "#"   
        
        # Pass 3: Attach raw data
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes, res, i = [], [], 0

        # Step 1: Parse the Header until the '#' marker
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1 # Skip the comma
        
        i += 1 # Skip the '#' marker to reach the actual data strings

        # Step 2: Use the collected lengths to slice the data
        for wordSize in sizes:
            res.append(s[i : i + wordSize])
            i += wordSize
        
        return res


# ===========================================================
# 2. LENGTH-PREFIX METHOD (OPTIMIZED)
# ===========================================================
class SolutionLengthPrefix:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — LENGTH-PREFIXING (Standard)
    ----------------------------------------------------------
    Intuition:
    Instead of a global header, we prefix each individual word 
    with its length and a delimiter. This allows the decoder 
    to process the string word-by-word in a single pass.

    Algorithm:
        Encode:
            For each string, append: str(len) + "#" + string.
        Decode:
            1. Use two pointers (i, j). 
            2. Find the '#' to determine the word's length.
            3. Slice the word based on that length.
            4. Move the pointer 'i' to the next length prefix.

    Time Complexity:  O(N)
    Space Complexity: O(N)
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # Format: [length][#][original_string]
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the '#' to isolate the length number
            while s[j] != '#':
                j += 1
            
            # Convert the slice [i:j] (the length) into an integer
            length = int(s[i:j])
            
            # Start of the word is right after '#'
            i = j + 1
            # End of the word is start + length
            j = i + length
            
            # Extract word and update main pointer i
            res.append(s[i:j])
            i = j

        return res


# ===========================================================
# 📌 IMPORTANT SYNTAX NOTES FOR YOUR RECORDS
# ===========================================================
"""
1. Manual Pointer Control: Using 'i' and 'j' is essential when 
   the amount of data to read changes dynamically (like word lengths).
2. String Slicing: s[start:stop] is inclusive of start but 
   exclusive of stop.
3. String to Int: Always use int() when converting metadata 
   stored in strings back into numbers for indexing/math.
4. While Loops: Used here instead of 'for' because the index 
   increments are not always +1 (they vary based on word length).
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    test_case = ["hello", "world", "C#", "is,cool"]

    print("--- Method 1: Header Metadata ---")
    sol1 = SolutionHeader()
    encoded1 = sol1.encode(test_case)
    print(f"Encoded: {encoded1}")
    print(f"Decoded: {sol1.decode(encoded1)}")

    print("\n--- Method 2: Length-Prefix (Optimized) ---")
    sol2 = SolutionLengthPrefix()
    encoded2 = sol2.encode(test_case)
    print(f"Encoded: {encoded2}")
    print(f"Decoded: {sol2.decode(encoded2)}")