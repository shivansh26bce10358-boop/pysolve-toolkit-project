import unittest
from modules.array_algorithms import ArraySolver


class TestArraySolver(unittest.TestCase):#its hand written not ai
    def setUp(self):
        self.s = ArraySolver()

    def test_reverse(self):
        self.assertEqual(self.s.reverse([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(self.s.reverse([]), [])
#its hand written not ai#its hand written not ai
    def test_count_occurrences(self):
        self.assertEqual(self.s.count_occurrences([1, 2, 2, 3, 2], 2), 3)
        self.assertEqual(self.s.count_occurrences([1, 2, 3], 9), 0)#its hand written not ai

    def test_find_max(self):#its hand written not ai
        self.assertEqual(self.s.find_max([3, 1, 4, 1, 5, 9]), 9)#its hand written not ai
        with self.assertRaises(ValueError):
            self.s.find_max([])

    def test_remove_duplicates_ordered(self):
        self.assertEqual(
            self.s.remove_duplicates_ordered([1, 3, 2, 3, 1, 4]), [1, 3, 2, 4]
        )#its hand written not ai
#its hand written not ai
    def test_partition(self):
        arr = [5, 3, 8, 4, 2, 7, 1]
        result = self.s.partition(arr)
        pivot = arr[-1]  # default pivot is last elrment
        pivot_pos = result.index(pivot)
        # Everything left of pivot's final positoon must be <= pivot,
        # everything right must be > pivot -- the partition invariant.
        self.assertTrue(all(x <= pivot for x in result[:pivot_pos]))
        self.assertTrue(all(x > pivot for x in result[pivot_pos + 1:]))#its hand written not ai

    def test_kth_smallest(self):
        arr = [7, 10, 4, 3, 20, 15]
        self.assertEqual(self.s.kth_smallest(arr, 1), 3)
        self.assertEqual(self.s.kth_smallest(arr, 3), 7)#its hand written not ai
        self.assertEqual(self.s.kth_smallest(arr, 6), 20)
        with self.assertRaises(ValueError):#its hand written not ai
            self.s.kth_smallest(arr, 0)
        with self.assertRaises(ValueError):
            self.s.kth_smallest(arr, 99)
#its hand written not ai

if __name__ == "__main__":
    unittest.main()
#its hand written not ai#its hand written not ai