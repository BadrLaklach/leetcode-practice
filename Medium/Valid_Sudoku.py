"""
===========================================================
 VALID SUDOKU — MULTIPLE METHODS WITH FULL EXPLANATION
===========================================================

📌 Problem Summary:
Determine if a 9 x 9 Sudoku board is valid. Only the filled 
cells need to be validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain 
       the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but 
is not necessarily solvable.

This file includes THREE methods:
    1. Brute Force (Multi-pass)
    2. Hash Set (One Pass)
    3. Bitmask (Optimized Space)
"""

from typing import List
from collections import defaultdict

# ===========================================================
# 1. BRUTE FORCE METHOD
# ===========================================================
class SolutionBruteForce:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — MULTI-PASS VALIDATION
    ----------------------------------------------------------
    Intuition:
    Directly check all three conditions one by one. Use a fresh 
    set for every row, every column, and every 3x3 box to 
    ensure no number appears twice.

    Time Complexity: O(n²) - where n is 9 (fixed size)
    Space Complexity: O(n) - for the 'seen' set
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check all rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": continue
                if board[row][i] in seen: return False
                seen.add(board[row][i])

        # 2. Check all columns
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".": continue
                if board[i][col] in seen: return False
                seen.add(board[i][col])

        # 3. Check all 3x3 boxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    # Formula to map 'square' index to actual row/col
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".": continue
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])
        return True

# ===========================================================
# 2. HASH SET METHOD (ONE PASS)
# ===========================================================
class SolutionHashSet:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — ONE PASS WITH MULTIPLE SETS
    ----------------------------------------------------------
    Intuition:
    Instead of looping 3 times, we loop once and maintain three 
    collections of sets: one for rows, one for columns, and one 
    for the 3x3 squares.

    

    Time Complexity: O(n²) - Single pass through 81 cells
    Space Complexity: O(n²) - To store all seen numbers in sets
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Key is (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                # Check for conflicts in all three tracking sets
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True

# ===========================================================
# 3. BITMASK METHOD
# ===========================================================
class SolutionBitmask:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — BITMASK (MEMORY OPTIMIZED)
    ----------------------------------------------------------
    Intuition:
    Since we only have digits 1-9, we can represent 'seen' 
    digits as bits in a single integer (0 or 1). 
    Bit 0 = digit 1, Bit 1 = digit 2, etc.

    Time Complexity: O(n²)
    Space Complexity: O(n) - stores 27 integers total
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # Convert digit string to 0-8 bit position
                val = int(board[r][c]) - 1
                mask = 1 << val
                
                # Formula for box index: (r // 3) * 3 + (c // 3)
                square_idx = (r // 3) * 3 + (c // 3)

                # Check if bit is already '1' using bitwise AND
                if (rows[r] & mask or 
                    cols[c] & mask or 
                    squares[square_idx] & mask):
                    return False

                # Mark bit as '1' using bitwise OR
                rows[r] |= mask
                cols[c] |= mask
                squares[square_idx] |= mask

        return True

# ===========================================================
# 📌 METHOD SUMMARY & SYNTAX NOTES
# ===========================================================
"""
METHOD APPLICATION:
- Brute Force is easiest to read but least efficient in terms of code repetition.
- Hash Set (One Pass) is the standard interview solution.
- Bitmask is the most professional/performant for small, fixed ranges like 1-9.

IMPORTANT SYNTAX:
1. defaultdict(set): Automatically creates a new empty set if the key is missing.
2. 1 << val: Bitwise Shift. Moves the '1' to the position of the digit.
3. (r // 3, c // 3): A tuple used as a key in a dictionary to identify a 3x3 box.
4. |= (Bitwise OR): Sets the bit to 1.
5. & (Bitwise AND): Checks if a bit is already 1.
"""

# ===========================================================
# EXAMPLE USAGE 
# ===========================================================
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    sol = SolutionBitmask()
    print(f"Is Valid Sudoku: {sol.isValidSudoku(board)}")