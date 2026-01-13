
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Output = [1] * n # Initialize output array with size n

        # LRAccum (Prefix): Product from left to right
        LRAccum = [1] * n
        LRAccum[0] = nums[0]
        for i in range(0, n - 1):
            LRAccum[i+1] = LRAccum[i] * nums[i+1]

        # RLAccum (Suffix): Product from right to left
        RLAccum = [1] * n
        RLAccum[n-1] = nums[n-1]
        for i in range(n - 1, 0, -1):
            RLAccum[i-1] = RLAccum[i] * nums[i-1]
        
        # --- COMBINATION PHASE ---
        
        # Edge Case: Index 0 only uses the suffix from index 1
        Output[0] = RLAccum[1]
        
        # Edge Case: Last index only uses the prefix from second-to-last
        Output[n-1] = LRAccum[n-2]

        # Middle Phase: Multiply prefix (left) and suffix (right)
        for i in range(1, n - 1):
            # For nums[i], we want: (everything left) * (everything right)
            Output[i] = RLAccum[i+1] * LRAccum[i-1]
        
        # Abbreviations for Debugging
        print(f"RLA (Suffix): {RLAccum}")
        print(f"LRA (Prefix): {LRAccum}")

        return Output