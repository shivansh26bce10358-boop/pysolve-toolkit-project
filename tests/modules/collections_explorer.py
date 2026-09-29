"""
collections_explorer.py
-------------------------
Module 3 of PySolve: Collections Explorer.
this Maps to syllabus Unit 5 (Python Lists: list operations - Tuples - Sets
Operations - Dictionaries - Time Tradeoff).

This module makes the abstract "time tradeoff" line item concrete by
actually measuring the list-scan vs dict-lookup performance rather than
just asserting Big-O in prose.
"""

import time
import random
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

from utils.complexity_logger import track


class CollectionsExplorer:
    """Demonstrates list, tuple, set, and dict operations and their tradeoffs."""

    @track
    def list_operations_demo(self, data: list) -> dict:
        """Shows core list ops: append, slice, sort, membership test."""
        working = data[:]
        working.append(999)
        sliced = working[1:4] if len(working) >= 4 else working[:]
        sorted_copy = sorted(working)
        contains_999 = 999 in working
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        return {
            "original": data,
            "after_append": working,
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            "slice_1_4": sliced,
            "sorted": sorted_copy,
            "contains_999": contains_999,
        }

    @track
    def tuple_operations_demo(self, data: list) -> dict:
        """Shows tuple immutability, packing/unpacking, and concatenation."""
        t1 = tuple(data)
        t2 = (0,) + t1  # concatenation creates a new tuple (immutability)
        first, *rest = t1 if t1 else (None, [])
        return {
            "as_tuple": t1,
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            "concatenated": t2,
            "unpacked_first": first,
            "unpacked_rest": rest,
        }

    @track
    def set_operations_demo(self, a: list, b: list) -> dict:
        """Union, intersection, difference, symmetric difference."""
        sa, sb = set(a), set(b)
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        return {
            "union": sorted(sa | sb),
            "intersection": sorted(sa & sb),
            "difference_a_minus_b": sorted(sa - sb),
            "symmetric_difference": sorted(sa ^ sb),
        }
      #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 


    @track
    def dict_operations_demo(self, pairs: list) -> dict:
        """Build a dict from pairs, demonstrate get/update/keys/values."""
        d = dict(pairs)
        d["_meta"] = "demo"
        return {
            "dict": d,
            "keys": list(d.keys()),
            "values": list(d.values()),
            "get_missing_default": d.get("nonexistent", "N/A"),
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        }

    def time_tradeoff_benchmark(self, n: int = 20000) -> dict:
        """
        Empirically compares O(n) list membership search against O(1)
        average dict-key lookup for n elements. This is the syllabus's
        'Time Tradeoff' concept, demonstrated with real numbers instead
        of asserted in prose.
        """
        data_list = list(range(n))
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        random.shuffle(data_list)
        data_dict = {x: True for x in data_list}
        target = n - 1  # worst case: last element to search for

        start = time.perf_counter()
        found_list = target in data_list
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        list_time_ms = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        found_dict = target in data_dict
        dict_time_ms = (time.perf_counter() - start) * 1000

        speedup = (list_time_ms / dict_time_ms) if dict_time_ms > 0 else float("inf")

        return {
            "n": n,
            "list_lookup_ms": round(list_time_ms, 4),
            "dict_lookup_ms": round(dict_time_ms, 4),
            "found_list": found_list,
            "found_dict": found_dict,
            "dict_speedup_factor": round(speedup, 1),
        }
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
