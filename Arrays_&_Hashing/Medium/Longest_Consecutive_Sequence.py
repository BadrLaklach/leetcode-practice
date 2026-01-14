"""
===========================================================
 LONGEST CONSECUTIVE SEQUENCE — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Given an unsorted array of integers nums, return the length of 
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
    Input:  nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

This file includes FOUR methods:
    1. Brute Force (O(n²))
    2. Sorting Method (O(n log n))
    3. Hash Set - Sequence Start Method (O(n) - Optimal)
    4. Hash Map - Boundary Merging Method (O(n))
"""

from typing import List
from collections import defaultdict

# ===========================================================
# 1. BRUTE FORCE METHOD
# ===========================================================
class SolutionBruteForce:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — BRUTE FORCE
    ----------------------------------------------------------
    Intuition:
    Start from every number in the list and try to extend a 
    consecutive streak as far as possible by checking if num + 1, 
    num + 2, etc., exist in the set.

    Time Complexity: O(n²) 
    Space Complexity: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res

# ===========================================================
# 2. SORTING METHOD
# ===========================================================
class SolutionSorting:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — SORTING
    ----------------------------------------------------------
    Intuition:
    If we sort the numbers, consecutive values appear next to 
    each other. We walk through the list, skipping duplicates 
    and resetting the streak when a gap is found.

    Time Complexity: O(n log n)
    Space Complexity: O(1) or O(n) depending on sorting implementation
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            # Skip duplicates
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res

# ===========================================================
# 3. HASH SET METHOD (OPTIMAL)
# ===========================================================
class SolutionHashSet:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — HASH SET (START OF SEQUENCE)
    ----------------------------------------------------------
    Intuition:
    A number is the start of a sequence ONLY if (num - 1) is 
    not in the set. We only trigger the 'while' loop for these 
    starting numbers, ensuring each element is visited constant times.

    

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

# ===========================================================
# 4. HASH MAP METHOD (BOUNDARY MERGING)
# ===========================================================
class SolutionHashMap:
    """
    ----------------------------------------------------------
    🔹 METHOD 4 — HASH MAP (BOUNDARY MERGING)
    ----------------------------------------------------------
    Intuition:
    For each number, check its neighbors (num-1, num+1). 
    Calculate the total length of the merged sequence and update 
    the leftmost and rightmost boundaries in the map.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                # Find lengths of left and right sequences
                left = mp[num - 1]
                right = mp[num + 1]
                
                length = left + right + 1
                mp[num] = length
                
                # Update boundaries of the sequence
                mp[num - left] = length
                mp[num + right] = length
                
                res = max(res, length)
        return res

# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Hash Set approach (Method 3) is the most common O(n) interview solution. 
- The Hash Map approach (Method 4) is similar to the Union-Find logic 
  used to track connected components.

IMPORTANT SYNTAX:
1. if (num - 1) not in numSet: Crucial check to prevent O(n²) complexity. 
   It ensures we only start counting from the smallest number in a sequence.
2. set(nums): Converts list to hash set for O(1) lookups.
3. defaultdict(int): Returns 0 for any key not already in the map, 
   simplifying the neighbor length check.
4. max(res, length): Pythonic way to keep track of the largest value found.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    
    sol = SolutionHashSet()
    print(f"Longest Consecutive Sequence Length: {sol.longestConsecutive(nums)}")