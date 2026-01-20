"""
===========================================================
    CONTAINER WITH MOST WATER — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
You are given an integer array 'heights' where each element 
represents the height of a vertical line. Find two lines that, 
together with the x-axis, form a container such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Example:
    Input:  heights = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The max area is formed by heights[1]=8 and heights[8]=7.
    Width = 8 - 1 = 7. Height = min(8, 7) = 7. Area = 7 * 7 = 49.

This file includes TWO methods:
    1. Brute Force (O(n²))
    2. Two Pointers (O(n) - Optimal)
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
    Try every possible pair of lines (i, j) and calculate the 
    area. The area is defined by the shorter of the two lines 
    (height) multiplied by the distance between them (width).

    Time Complexity:  O(n²)
    Space Complexity: O(1)
    """
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                # Area = min(h1, h2) * width
                current_area = min(heights[i], heights[j]) * (j - i)
                res = max(res, current_area)
        return res


# ===========================================================
# 2. TWO POINTERS METHOD (OPTIMAL)
# ===========================================================
class SolutionTwoPointers:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — TWO POINTERS
    ----------------------------------------------------------
    Intuition:
    Start with the maximum possible width (pointers at both ends).
    To find a larger area, we must find a taller height. Since 
    the area is limited by the shorter line, moving the taller 
    line inward will only decrease the width without increasing 
    the height. Therefore, we always move the shorter pointer.

    

    Algorithm:
        1. Initialize l = 0, r = len(heights) - 1.
        2. While l < r:
            - Calculate area = min(heights[l], heights[r]) * (r - l).
            - Update res.
            - Move the pointer pointing to the shorter line.

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # Calculate current volume
            width = r - l
            h = min(heights[l], heights[r])
            res = max(res, h * width)
            
            # Greedily move the pointer with the smaller height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res


# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Two-Pointers method (Method 2) is the optimal O(n) approach. 
  It works because it systematically eliminates widths that 
  cannot possibly produce a larger area than the current maximum.

IMPORTANT SYNTAX:
1. min(a, b): Essential here because the water level cannot 
   exceed the shorter side (the "bottleneck").
2. max(res, area): Standard way to track the global maximum 
   during an iteration.
3. width = (r - l): Note that we do not use (r - l + 1) because 
   the indices represent the positions of the lines, and the 
   distance is the simple difference between indices.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    heights_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = SolutionTwoPointers()
    print(f"Maximum water container area: {sol.maxArea(heights_list)}")