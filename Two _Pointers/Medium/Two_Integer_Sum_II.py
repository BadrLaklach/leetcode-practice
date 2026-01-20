"""
===========================================================
    TWO SUM II (SORTED ARRAY) — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Given a 1-indexed array of integers 'numbers' that is already 
sorted in non-decreasing order, find two numbers such that they 
add up to a specific target number.

Return the indices of the two numbers [index1, index2] as an 
integer array of length 2, where 1 <= index1 < index2 <= numbers.length.

Example:
    Input:  numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

This file includes FOUR methods:
    1. Brute Force (O(n²))
    2. Binary Search (O(n log n))
    3. Hash Map (O(n) Time, O(n) Space)
    4. Two Pointers (O(n) Time, O(1) Space - Optimal)
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
    Check every possible pair. For each index i, look at every 
    index j > i and check if their sum equals the target. 
    Ignores the fact that the array is sorted.

    Time Complexity:  O(n²)
    Space Complexity: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1] # 1-indexed
        return []


# ===========================================================
# 2. BINARY SEARCH METHOD
# ===========================================================
class SolutionBinarySearch:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — BINARY SEARCH
    ----------------------------------------------------------
    Intuition:
    For each number at index i, we search for (target - numbers[i]) 
    in the remaining part of the array. Since the array is sorted, 
    we use Binary Search to find the complement.

    Time Complexity:  O(n log n)
    Space Complexity: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []


# ===========================================================
# 3. HASH MAP METHOD
# ===========================================================
class SolutionHashMap:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — HASH MAP
    ----------------------------------------------------------
    Intuition:
    Store seen numbers and their indices in a map. For each 
    number, check if its complement exists in the map.

    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []


# ===========================================================
# 4. TWO POINTERS METHOD (OPTIMAL)
# ===========================================================
class SolutionTwoPointers:
    """
    ----------------------------------------------------------
    🔹 METHOD 4 — TWO POINTERS
    ----------------------------------------------------------
    Intuition:
    Use one pointer at the start (l) and one at the end (r). 
    Since the array is sorted:
    - If sum > target: move 'r' left to decrease the sum.
    - If sum < target: move 'l' right to increase the sum.

    

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Two-Pointers method (Method 4) is the most efficient because 
  it exploits the "Sorted" property to achieve O(1) space.
- Binary search is a good middle ground if you only wanted to 
  search for one side.

IMPORTANT SYNTAX:
1. l + (r - l) // 2: Prevents potential integer overflow in other 
   languages (though Python handles large ints, this is best practice).
2. [i + 1, j + 1]: Be careful with "1-indexed" requirements. Python 
   lists are 0-indexed, so we must add 1 to the result.
3. while l < r: The loop condition for two pointers ensures we don't 
   use the same element twice.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    t = 9
    sol = SolutionTwoPointers()
    print(f"Indices for target {t}: {sol.twoSum(nums, t)}")