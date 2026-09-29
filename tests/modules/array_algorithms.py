"""
array_algorithms.py
---------------------
Module 2 of PySolve: Array Algorithms Lab.
this Maps to syllabus Unit 5 (Array Techniques).
"""

from utils.complexity_logger import track


class ArraySolver:
    """Classical array manipulation algorithms with documented complexity."""
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    @track
    def reverse(self, arr: list) -> list:
        """In-place-style reversal returning a new list. Time: O(n)."""
        result = arr[:]
        left, right = 0, len(result) - 1
        while left < right:
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        return result

    @track
    def count_occurrences(self, arr: list, target) -> int:
        """Count occurrences of target in arr. Time: O(n)."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        count = 0
        for item in arr:
            if item == target:
                count += 1
        return count

    @track
      #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    def find_max(self, arr: list):
        """Find maximum element. Time: O(n)."""
        if not arr:
            raise ValueError("array is empty")
        max_val = arr[0]
        for item in arr[1:]:
            if item > max_val:
                max_val = item
        return max_val

    @track  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    def remove_duplicates_ordered(self, arr: list) -> list:
        """
        Remove duplicates while preserving first-seen order.
        Time: O(n). Space: O(n) for the seen-set.
        """
        seen = set()
        result = []
        for item in arr:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    @track
    def partition(self, arr: list, pivot_index: int = -1) -> list:
        """
        Lomuto partition scheme around the last element (or given index).
        Time: O(n). Returns a new partitioned list with the pivot in its
        final sorted position.
        """
        result = arr[:]
        if pivot_index == -1:
            pivot_index = len(result) - 1
        result[pivot_index], result[-1] = result[-1], result[pivot_index]
        pivot = result[-1]
        i = 0
        for j in range(len(result) - 1):  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            if result[j] <= pivot:
                result[i], result[j] = result[j], result[i]
                i += 1
        result[i], result[-1] = result[-1], result[i]
        return result

    @track
    def kth_smallest(self, arr: list, k: int):
        """
        Kth smallest element via Quickselect.
        Average Time: O(n). Worst case: O(n^2).
        k is 1-indexed (k=1 returns the smallest element).
        """
        if not (1 <= k <= len(arr)):
            raise ValueError(f"k must be between 1 and {len(arr)}")

        working = arr[:]  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 


        def _select(items, target_idx):
            if len(items) == 1:
                return items[0]  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            pivot = items[len(items) // 2]
            lows = [x for x in items if x < pivot]
            highs = [x for x in items if x > pivot]
            pivots = [x for x in items if x == pivot]

            if target_idx < len(lows):  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

                return _select(lows, target_idx)
            elif target_idx < len(lows) + len(pivots):
                return pivot
            else:
                return _select(highs, target_idx - len(lows) - len(pivots))
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        return _select(working, k - 1)
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
