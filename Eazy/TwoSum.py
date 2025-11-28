"""
===========================================================
 TWO SUM — MULTIPLE METHODS WITH EXPLANATION
===========================================================

📌 Problem Summary:
Given an array of integers (nums) and an integer (target),
return the *indices* of the two numbers in the array that
add up to the target.

• You may assume exactly one valid answer exists.
• You cannot use the same element twice.
• Indices must refer to the *original* array positions.

We will show FOUR different methods to solve this problem:

    1. Brute Force (O(n²) time)
    2. Sorting + Two Pointers (O(n log n) time)
    3. Hash Map — Two Pass (O(n) time)
    4. Hash Map — One Pass (O(n) time, best solution)

Each method has:
    - Explanation
    - Step-by-step reasoning
    - Full code
    - Time & space complexity
"""

from typing import List


# ===========================================================
# 1. BRUTE FORCE METHOD
# ===========================================================
class SolutionBruteForce:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — BRUTE FORCE
    ----------------------------------------------------------
    Intuition:
    The simplest way to solve the problem is to check *every*
    possible pair of numbers in the array and see if they add
    up to the target.

    How it works:
        • Loop i from 0 to n-1
        • Loop j from i+1 to n-1
        • If nums[i] + nums[j] == target → return [i, j]

    This method is very slow for large arrays because it must
    examine all possible pairs.

    Time Complexity:
        O(n²) — double nested loop
    Space Complexity:
        O(1) — uses no extra data structure
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through every element except the last
        for i in range(len(nums)):
            # Loop through the elements after nums[i]
            for j in range(i + 1, len(nums)):
                # Check whether they add up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]

        # Problem guarantees a solution, but included for completeness
        return []


# ===========================================================
# 2. SORTING + TWO POINTERS METHOD
# ===========================================================
class SolutionSorting:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — SORTING + TWO POINTERS
    ----------------------------------------------------------
    Intuition:
    Sorting allows us to use the "two-pointer technique"
    (left pointer starts at the beginning, right pointer at end).
    However, sorting changes the order of elements, so we must
    store BOTH value and original index before sorting.

    Algorithm:
        1. Create array A = [[value, index], ...]
        2. Sort A by value
        3. Use two pointers:
              left = 0
              right = len(nums) - 1
        4. If sum < target → move left pointer right (increase sum)
           If sum > target → move right pointer left (decrease sum)
           If sum == target → RETURN original indices

    Time Complexity:
        O(n log n) — sorting step dominates
    Space Complexity:
        O(n) — storing value/index pairs
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Create array of [value, index] pairs
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        # Step 2: Sort based on value
        A.sort()  # now values are in ascending order

        # Step 3: Two pointers
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = A[left][0] + A[right][0]

            if current_sum == target:
                # Return original indices
                return [
                    min(A[left][1], A[right][1]),
                    max(A[left][1], A[right][1])
                ]

            elif current_sum < target:
                left += 1  # increase sum
            else:
                right -= 1  # decrease sum

        return []


# ===========================================================
# 3. HASH MAP — TWO PASS SOLUTION
# ===========================================================
class SolutionHashTwoPass:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — HASH MAP (TWO PASS)
    ----------------------------------------------------------
    Intuition:
    A hash map allows O(1) lookup of elements. We first store
    EVERY number with its index in the hash map.
    
    Then, in a second pass, we compute:
        complement = target - nums[i]
    and check whether the complement exists in the map.

    Important:
        The complement must not be the same element,
        so index must differ.

    Steps:
        1. Build a dictionary: value → index
        2. Loop again:
              diff = target - nums[i]
              If diff in dictionary and index != i:
                  return answer

    Time Complexity:
        O(n) — two simple passes
    Space Complexity:
        O(n) — dictionary storing all elements
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Step 1: Build hash map
        indices = {}  # value → index
        for i, n in enumerate(nums):
            indices[n] = i

        # Step 2: Search for complement
        for i, n in enumerate(nums):
            diff = target - n
            # check if diff exists and is not same element
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []


# ===========================================================
# 4. HASH MAP — ONE PASS SOLUTION (BEST)
# ===========================================================
class SolutionHashOnePass:
    """
    ----------------------------------------------------------
    🔹 METHOD 4 — HASH MAP (ONE PASS)
    ----------------------------------------------------------
    Intuition:
    This is the BEST and MOST EFFICIENT solution.

    Instead of first building the full map, we build the map
    WHILE we loop through the array.

    For each number:
        diff = target - nums[i]
    Before adding nums[i] to the map, check whether diff
    already exists.

    Why this works?
        • Ensures we never reuse the same element
        • Only single pass through the list
        • Constant time lookups

    Steps:
        1. Create empty map: value → index
        2. Loop through nums:
               diff = target - n
               If diff exists → return its index + current index
               Otherwise store n in the map

    Time Complexity:
        O(n)
    Space Complexity:
        O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # value → index

        for i, n in enumerate(nums):
            diff = target - n
            
            # If the complement exists, we found the pair
            if diff in prevMap:
                return [prevMap[diff], i]

            # Otherwise, store current number’s index
            prevMap[n] = i


# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", SolutionBruteForce().twoSum(nums, target))
    print("Sorting Method:", SolutionSorting().twoSum(nums, target))
    print("Hash Two Pass:", SolutionHashTwoPass().twoSum(nums, target))
    print("Hash One Pass:", SolutionHashOnePass().twoSum(nums, target))
