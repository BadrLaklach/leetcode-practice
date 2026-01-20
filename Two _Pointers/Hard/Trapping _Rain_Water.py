"""
===========================================================
    TRAPPING RAIN WATER — MULTIPLE METHODS
===========================================================

📌 Problem Summary:
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it 
can trap after raining.

Example:
    Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6

This file includes FOUR methods:
    1. Brute Force (O(n²))
    2. Prefix & Suffix Arrays (O(n) Time, O(n) Space)
    3. Monotonic Stack (O(n) Time, O(n) Space)
    4. Two Pointers (O(n) Time, O(1) Space - Optimal)
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
    For every bar, find the maximum height to its left and its 
    right. The water trapped at that bar is: 
    min(leftMax, rightMax) - currentHeight.

    Time Complexity:  O(n²)
    Space Complexity: O(1)
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n, res = len(height), 0

        for i in range(n):
            leftMax = rightMax = height[i]
            # Scan left
            for j in range(i):
                leftMax = max(leftMax, height[j])
            # Scan right
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]
        return res

# ===========================================================
# 2. PREFIX & Suffix ARRAYS
# ===========================================================
class SolutionDP:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — PRECOMPUTED MAXIMA (DP)
    ----------------------------------------------------------
    Intuition:
    Instead of re-scanning for every index, we pre-calculate 
    the leftMax and rightMax for every position using two 
    arrays. This trades space for a significant speed boost.

    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0

        leftMax, rightMax = [0] * n, [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res

# ===========================================================
# 3. MONOTONIC STACK
# ===========================================================
class SolutionStack:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — MONOTONIC STACK
    ----------------------------------------------------------
    Intuition:
    We use a stack to store indices of bars with decreasing 
    heights. When we find a bar taller than the stack top, it 
    acts as a "right wall," creating a "basin" with the previous 
    elements in the stack.

    Time Complexity:  O(n)
    Space Complexity: O(n)
    """
    def trap(self, height: List[int]) -> int:
        stack, res = [], 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid_idx = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid_idx]
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res

# ===========================================================
# 4. TWO POINTERS (OPTIMAL)
# ===========================================================
class SolutionTwoPointers:
    """
    ----------------------------------------------------------
    🔹 METHOD 4 — TWO POINTERS
    ----------------------------------------------------------
    Intuition:
    Since water is limited by the shorter side, we can use 
    two pointers. We always process the side with the smaller 
    maximum height, as it dictates the water level regardless 
    of how high the other side is.

    

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- The Two-Pointers approach (Method 4) is the optimal solution 
  because it eliminates the O(n) space required by DP or Stacks.
- Monotonic Stack is useful if you need to process water 
  horizontally (row by row) rather than vertically (column by column).

IMPORTANT SYNTAX:
1. range(n-2, -1, -1): Syntax for iterating backward from the 
   second-to-last element down to index 0.
2. stack[-1]: Accesses the top element of the stack (the most 
   recent index) without popping it.
3. min(leftMax, rightMax) - height[i]: The fundamental formula 
   for the volume of water trapped above a single bar.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol = SolutionTwoPointers()
    print(f"Total Trapped Water: {sol.trap(h)}")