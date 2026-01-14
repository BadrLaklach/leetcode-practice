"""
===========================================================
 PRODUCT OF ARRAY EXCEPT SELF — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example:
    Input:  nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

This file includes FOUR methods:
    1. Brute Force (O(n²))
    2. Division Method (O(n)) - *Note: Problem constraints usually forbid this*
    3. Prefix & Suffix Arrays (O(n) Time, O(n) Space)
    4. Optimized Prefix & Suffix (O(n) Time, O(1) Extra Space)
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
    For every single element, iterate through the entire rest 
    of the array to calculate the product.

    Time Complexity: O(n²)
    Space Complexity: O(1) extra space (O(n) for output)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res

# ===========================================================
# 2. DIVISION METHOD
# ===========================================================
class SolutionDivision:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — TOTAL PRODUCT / CURRENT NUMBER
    ----------------------------------------------------------
    Intuition:
    Calculate the total product of the array once. Then for each 
    index, divide the total by the current number. 
    Special handling is required for zeros.

    Time Complexity: O(n)
    Space Complexity: O(1) extra space
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if c else prod
            else:
                res[i] = prod // c
        return res

# ===========================================================
# 3. PREFIX & SUFFIX ARRAYS
# ===========================================================
class SolutionPrefixSuffix:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — PREFIX & SUFFIX ARRAYS
    ----------------------------------------------------------
    Intuition:
    Store the cumulative product of everything to the left in 'pref' 
    and everything to the right in 'suff'.
    res[i] = pref[i] * suff[i]
    
    

    Time Complexity: O(n)
    Space Complexity: O(n) - uses two extra arrays
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

# ===========================================================
# 4. OPTIMIZED PREFIX & SUFFIX (SPACE OPTIMAL)
# ===========================================================
class SolutionOptimal:
    """
    ----------------------------------------------------------
    🔹 METHOD 4 — TWO-PASS OPTIMIZED
    ----------------------------------------------------------
    Intuition:
    Instead of full arrays, use a single variable 'prefix' to fill 
    the result array from the left, then a 'postfix' variable to 
    multiply from the right. This saves O(n) space.

    Time Complexity: O(n)
    Space Complexity: O(1) extra space (excluding output array)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        # Pass 1: Left to Right (Prefix)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # Pass 2: Right to Left (Postfix)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res

# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The optimal approach avoids division by calculating Prefix products 
  (everything before index i) and Postfix products (everything after index i).
- Multiplying Prefix * Postfix gives you the total product excluding nums[i].

IMPORTANT SYNTAX:
1. range(n-1, -1, -1): Standard way to iterate backward from the last index to 0.
2. [1] * n: Pre-allocates a list of size n filled with 1s.
3. enumerate(nums): Useful for getting both index and value (used in Division method).
4. if num: (in Python) treats 0 as False and non-zero as True.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    
    print("Optimal Method Output:")
    print(SolutionOptimal().productExceptSelf(nums))