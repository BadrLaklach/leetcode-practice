"""
===========================================================
    3SUM — MULTIPLE METHODS WITH FULL EXPLANATION
===========================================================

📌 Problem Summary:
Given an integer array nums, return all the triplets [nums[i], 
nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
    Input:  nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

This file includes THREE methods:
    1. Brute Force (O(n³))
    2. Hash Map (O(n²))
    3. Two Pointers (O(n²) Time, O(1) Space - Optimal)
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
    Try every possible combination of three numbers. We use a 
    set of tuples to automatically handle and remove duplicate 
    triplets. Sorting the input first ensures that identical 
    triplets appear in the same order before being added to the set.

    Time Complexity:  O(n³)
    Space Complexity: O(m) - where m is the number of unique triplets
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return [list(i) for i in res]


# ===========================================================
# 2. HASH MAP METHOD
# ===========================================================
class SolutionHashMap:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — HASH MAP (FREQUENCY COUNT)
    ----------------------------------------------------------
    Intuition:
    Fix the first two numbers and use a hash map to see if the 
    required third number (target) exists. We manage counts 
    to avoid using the same element index twice.

    Time Complexity:  O(n²)
    Space Complexity: O(n) - for the frequency map
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            # Backtrack: Restore counts for the next iteration of 'i'
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res


# ===========================================================
# 3. TWO POINTERS METHOD (OPTIMAL)
# ===========================================================
class SolutionTwoPointers:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — TWO POINTERS
    ----------------------------------------------------------
    Intuition:
    Sort the array and iterate through. For each element 'a', 
    treat the problem as a "Two Sum II" problem for the rest 
    of the array using two pointers (l and r).

    

    Algorithm:
        1. Sort nums.
        2. Loop through with index i. Skip duplicates of nums[i].
        3. If nums[i] > 0, break (no triplet can sum to 0 anymore).
        4. Use l = i+1 and r = len-1.
        5. Move l/r based on sum vs 0.

    Time Complexity:  O(n²)
    Space Complexity: O(1) or O(n) - depending on sorting implementation
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Optimization: If the smallest number is > 0, sum can't be 0
            if a > 0:
                break

            # Skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate second elements
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Two-Pointers method (Method 3) is the most memory-efficient 
  O(n²) solution and is highly preferred in interviews.
- Sorting is the most critical first step for all optimized solutions.

IMPORTANT SYNTAX:
1. enumerate(nums): Provides both the index (i) and the value (a).
2. res.append([a, b, c]): Lists are added to the results list.
3. while l < r and nums[l] == nums[l-1]: A nested loop to skip 
   duplicates while maintaining the main pointer loop bounds.
4. -(nums[i] + nums[j]): Calculating the complement needed to reach zero.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    sol = SolutionTwoPointers()
    print(f"Unique triplets that sum to 0: {sol.threeSum(nums)}")