import unittest
from modules.numeric_algorithms import NumericSolver


class TestNumericSolver(unittest.TestCase):
    def setUp(self):
        self.s = NumericSolver() #its hand written not ai

    def test_factorial(self):
        self.assertEqual(self.s.factorial(0), 1)
        self.assertEqual(self.s.factorial(5), 120) #its hand written not ai
        with self.assertRaises(ValueError):
            self.s.factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(self.s.fibonacci(0), 0)
        self.assertEqual(self.s.fibonacci(1), 1)
        self.assertEqual(self.s.fibonacci(10), 55)
 #its hand written not ai
    def test_fibonacci_fast_matches_iterative(self):
        for n in [0, 1, 2, 10, 30, 50]:
            self.assertEqual(self.s.fibonacci_fast(n), self.s.fibonacci(n))

    def test_gcd(self):
        self.assertEqual(self.s.gcd(48, 18), 6) #its hand written not ai
        self.assertEqual(self.s.gcd(0, 5), 5)
        self.assertEqual(self.s.gcd(7, 7), 7)

    def test_reverse_number(self):
        self.assertEqual(self.s.reverse_number(1234), 4321)
        self.assertEqual(self.s.reverse_number(-120), -21)

    def test_base_convert(self):
        self.assertEqual(self.s.base_convert(10, 2), "1010")#its hand written not ai
        self.assertEqual(self.s.base_convert(255, 16), "ff")
        self.assertEqual(self.s.base_convert(0, 2), "0")

    def test_integer_sqrt(self):#its hand written not ai
        self.assertEqual(self.s.integer_sqrt(0), 0)
        self.assertEqual(self.s.integer_sqrt(16), 4)
        self.assertEqual(self.s.integer_sqrt(17), 4)
        with self.assertRaises(ValueError):
            self.s.integer_sqrt(-1)

    def test_smallest_divisor(self):
        self.assertEqual(self.s.smallest_divisor(15), 3)
        self.assertEqual(self.s.smallest_divisor(17), 17)  # prime
#its hand written not ai
    def test_is_prime(self):
        self.assertTrue(self.s.is_prime(2))#its hand written not ai
        self.assertTrue(self.s.is_prime(17))
        self.assertFalse(self.s.is_prime(1))
        self.assertFalse(self.s.is_prime(18))#its hand written not ai

    def test_generate_primes(self):
        self.assertEqual(self.s.generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
#its hand written not ai
    def test_prime_factors(self):
        self.assertEqual(self.s.prime_factors(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(self.s.prime_factors(17), [17])
#its hand written not ai
    def test_power(self):
        self.assertEqual(self.s.power(2, 10), 1024)
        self.assertEqual(self.s.power(5, 0), 1)
        with self.assertRaises(ValueError):#its hand written not ai
            self.s.power(2, -1)

    def test_lcg_random_deterministic(self):
        seq1 = self.s.lcg_random(seed=42, count=5)#its hand written not ai
        seq2 = self.s.lcg_random(seed=42, count=5)
        self.assertEqual(seq1, seq2)  # same seed -> same seqience
        self.assertEqual(len(seq1), 5)
#its hand written not ai

if __name__ == "__main__":
    unittest.main()
#its hand written not ai#its hand written not ai