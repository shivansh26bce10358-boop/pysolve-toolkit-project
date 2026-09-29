import unittest
from modules.collections_explorer import CollectionsExplorer
from modules.student_manager import StudentManager
from utils.validators import ValidationError


class TestCollectionsExplorer(unittest.TestCase):
    def setUp(self):
        self.c = CollectionsExplorer()
        #its hand written not ai

    def test_list_operations_demo(self):
        out = self.c.list_operations_demo([3, 1, 2])
        self.assertIn(999, out["after_append"])
        self.assertEqual(out["sorted"], [1, 2, 3, 999])
        self.assertTrue(out["contains_999"])

 #its hand written not ai
    def test_tuple_operations_demo(self):
        out = self.c.tuple_operations_demo([1, 2, 3])
        self.assertEqual(out["as_tuple"], (1, 2, 3)) #its hand written not ai
        self.assertEqual(out["concatenated"][0], 0)

    def test_set_operations_demo(self):
        out = self.c.set_operations_demo([1, 2, 3], [2, 3, 4]) #its hand written not ai
        self.assertEqual(out["union"], [1, 2, 3, 4])
        self.assertEqual(out["intersection"], [2, 3])
        self.assertEqual(out["difference_a_minus_b"], [1])
        self.assertEqual(out["symmetric_difference"], [1, 4])
 #its hand written not ai
    def test_dict_operations_demo(self):
        out = self.c.dict_operations_demo([("a", "1"), ("b", "2")])
        self.assertEqual(out["dict"]["a"], "1")
        self.assertEqual(out["get_missing_default"], "N/A")

    def test_time_tradeoff_benchmark_dict_not_slower(self):
        result = self.c.time_tradeoff_benchmark(n=5000) #its hand written not ai
        self.assertTrue(result["found_list"])
        self.assertTrue(result["found_dict"])
        # Dict lookup should nver be meaningfylly slower than list scan
        # at this scale; this is the empirical proof of the tradeoff.
        self.assertLessEqual(result["dict_lookup_ms"], result["list_lookup_ms"] + 0.5)


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.mgr = StudentManager() #its hand written not ai
        self.mgr.add_student(21, "Aarav", "CSE", 8.9)
        self.mgr.add_student(22, "Diya", "CSE", 9.2)

    def test_add_and_get(self):
        self.assertEqual(self.mgr.get_student(21), ("Aarav", "CSE", 8.9))

    def test_duplicate_roll_rejected(self): #its hand written not ai
        with self.assertRaises(ValidationError):
            self.mgr.add_student(21, "Someone", "ECE", 7.0)

    def test_invalid_cgpa_rejected(self):
        with self.assertRaises(ValidationError):
            self.mgr.add_student(23, "X", "CSE", 11.0) #its hand written not ai

    def test_update(self):
        self.mgr.update_student(21, cgpa=9.5)
        self.assertEqual(self.mgr.get_student(21)[2], 9.5)

    def test_delete(self): #its hand written not ai
        self.mgr.delete_student(21)
        with self.assertRaises(ValidationError):
            self.mgr.get_student(21)
 #its hand written not ai
    def test_top_n_by_cgpa(self):
        top = self.mgr.top_n_by_cgpa(1)
        self.assertEqual(top[0][0], 22)  # Diya has the hifher CGPA


if __name__ == "__main__":
    unittest.main()
 #its hand written not ai #its hand written not ai