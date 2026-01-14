"""
===========================================================
 TOP K FREQUENT ELEMENTS — MULTIPLE METHODS 
===========================================================

📌 Problem Summary:
Given an integer array 'nums' and an integer 'k', return the 
k most frequent elements.

Example:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1, 2]

This file includes THREE methods:
    1. Sorting Method (O(N log N))
    2. Min-Heap Method (O(N log K))
    3. Bucket Sort Method (O(N))

Where:
    N = number of elements in the input array
"""

import heapq
from typing import List

# ===========================================================
# 1. SORTING METHOD
# ===========================================================
class SolutionSorting:
    """
    ----------------------------------------------------------
    🔹 METHOD 1 — FULL SORTING
    ----------------------------------------------------------
    Intuition:
    Count the frequency of every number, then sort the unique 
    numbers based on their counts in descending order.

    Algorithm:
        1. Create a frequency map (dictionary).
        2. Convert the map into a list of pairs [frequency, value].
        3. Sort the list (Python sorts by the first element, frequency).
        4. Pop the last 'k' elements (the largest ones).

    Time Complexity: O(N log N) - due to sorting all unique elements.
    Space Complexity: O(N) - to store the frequency map and list.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  
        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        # Structure as [count, value] for easy sorting
        arr = []
        for key, cnt in count.items():
            arr.append([cnt, key])

        arr.sort() # Sorts ascending by count

        res = []
        while len(res) < k:
            # .pop() takes from the end (highest counts)
            res.append(arr.pop()[1])   

        return res     

# ===========================================================
# 2. MIN-HEAP METHOD
# ===========================================================
class SolutionHeap:
    """
    ----------------------------------------------------------
    🔹 METHOD 2 — MIN-HEAP (SIZE K)
    ----------------------------------------------------------
    Intuition:
    Instead of sorting everything, maintain a "Top K" list using
    a Min-Heap. If the heap exceeds size K, remove the smallest.
    The remaining elements will be the K largest.

    Algorithm:
        1. Create frequency map.
        2. Push each [count, value] into a min-heap.
        3. If heap size > k, pop the smallest element.
        4. Collect the remaining K elements from the heap.

    Time Complexity: O(N log K) - Better than O(N log N) if K < N.
    Space Complexity: O(N + K) - Map of size N, Heap of size K.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap = []
        for n in count.keys():
            # Push [frequency, number]
            heapq.heappush(heap, [count[n], n])
            # If heap is too big, remove the one with the smallest frequency
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while len(heap) != 0:
            res.append(heapq.heappop(heap)[1])

        return res          

# ===========================================================
# 3. BUCKET SORT METHOD
# ===========================================================
class SolutionBucketSort:
    """
    ----------------------------------------------------------
    🔹 METHOD 3 — BUCKET SORT
    ----------------------------------------------------------
    Intuition:
    The maximum frequency of any number is N. We can create 
    an array of "buckets" where the index represents the frequency.
    
    Example: 
        nums = [1,1,1,2,2,100]
        Index 2: [2] (2 appears twice)
        Index 3: [1] (1 appears thrice)

    Algorithm:
        1. Count frequencies.
        2. Create a list of lists 'freq' where freq[i] stores 
           numbers that appear exactly 'i' times.
        3. Iterate backwards from the end of 'freq' to collect 
           the top K numbers.

    Time Complexity: O(N) - We iterate through the array a few times.
    Space Complexity: O(N) - To store the buckets and the map.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq[i] will store numbers that appear 'i' times
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, cnt in count.items():
            freq[cnt].append(key)

        res = []
        # Iterate from highest possible frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


# ===========================================================
# IMPORTANT SYNTAX NOTES FOR YOUR RECORDS
# ===========================================================
"""
1. count.get(n, 0): 
   Returns count[n] if it exists, otherwise 0. Prevents KeyError.

2. list.pop(): 
   Removes and returns the last item (O(1)).

3. heapq.heappush / heapq.heappop: 
   Maintains the min-heap property. pop always returns the smallest.

4. range(start, stop, step): 
   range(len(freq)-1, 0, -1) starts at the last index and moves 
   down to 1 (useful for finding "maximums" first).

5. List Comprehension: 
   [[] for i in range(len(nums)+1)] creates a list of independent empty lists.
"""

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Bucket Sort Result:", SolutionBucketSort().topKFrequent(nums, k))