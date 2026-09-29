"""
numeric_algorithms.py
----------------------
Module 1 of PySolve: Numeric Algorithms Engine.

this Maps to syllabus Unit 3 (Fundamental Algorithms) and Unit 4 (Factoring
Methods). Each method is implemented iteratively where possible to keep
space complexity O(1) and avoid Python's recurson-depth ceiling.
"""

from utils.complexity_logger import track


class NumericSolver:
    """Collection of classical numeric algorithms with documented complexity."""

    # ---------- Unit 3: Fundamental Algorithms ----------

    @track
    def factorial(self, n: int) -> int:
        """Iterative factorial. Time: O(n). Space: O(1)."""
        #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
        if n < 0:
            raise ValueError("factorial undefined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
     #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    @track
    def fibonacci(self, n: int) -> int:
        """Iterative nth Fibonacci number. Time: O(n). Space: O(1)."""
        if n < 0:
             #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            raise ValueError("fibonacci undefined for negative index")
        a, b = 0, 1
        for _ in range(n):
             #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            a, b = b, a + b
        return a

    @track
    def fibonacci_fast(self, n: int) -> int:
        """
        nth Fibonacci via fast doubling. Time: O(log n). Space: O(log n)
        (recursion stack). Demonstrates that a smarter algorithm beats a
        straightforward O(n) loop for very large n -- the core lesson of
        Unit 1's 'efficiency of algorithms'.
        """
        def _fib_pair(k):
            if k == 0:
                return (0, 1)
            a, b = _fib_pair(k // 2)
             #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            c = a * (2 * b - a)
            d = a * a + b * b
            if k % 2 == 0:
                return (c, d)
            return (d, c + d)
         #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        if n < 0:
            raise ValueError("fibonacci undefined for negative index")
        return _fib_pair(n)[0]

    @track
    def gcd(self, a: int, b: int) -> int:
        """Euclidean algorithm. Time: O(log(min(a,b))). Space: O(1)."""
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    @track
    def reverse_number(self, n: int) -> int:
        """Reverse the digits of n. Time: O(d) where d = digit count."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
        
        sign = -1 if n < 0 else 1
        n = abs(n)
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return sign * rev

    @track
    def base_convert(self, n: int, base: int) -> str:
        """Convert decimal n to given base (2-36). Time: O(log_base(n))."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
        
        if n == 0:
            return "0"
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        sign = "-" if n < 0 else ""
        n = abs(n)
        out = []
        while n > 0:
            out.append(digits[n % base])
            n //= base
        return sign + "".join(reversed(out))

    # ---------- Unit 4: Factoring Methods ----------

    @track
    def integer_sqrt(self, n: int) -> int:
        """
        
        Floor of sqrt(n) via Newton's method. Time: O(log n). Space: O(1).
        Avoids floating-point error for large integers, unlike math.sqrt.
        """
        if n < 0:
            raise ValueError("sqrt undefined for negative numbers")
        if n < 2:
            return n
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            
            y = (x + n // x) // 2
        return x

    @track
    def smallest_divisor(self, n: int) -> int:
        """Smallest divisor > 1 of n. Time: O(sqrt(n))."""
        if n < 2:
            raise ValueError("n must be >= 2")
        i = 2
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return n  # n is prime

    @track
      #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
    
    def is_prime(self, n: int) -> bool:
        """Primality test by trial division. Time: O(sqrt(n))."""
        if n < 2:
            return False
        if n in (2, 3):
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
                
                return False
            i += 2
        return True

    @track
    def generate_primes(self, limit: int) -> list:
        """Sieve of Eratosthenes up to limit. Time: O(n log log n)."""
        if limit < 2:
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            
            return []
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit + 1, i):
                      #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
                    
                    sieve[j] = False
        return [i for i, is_p in enumerate(sieve) if is_p]

    @track
    def prime_factors(self, n: int) -> list:
        """Prime factorization of n. Time: O(sqrt(n))."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
        
        if n < 2:
            raise ValueError("n must be >= 2")
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
                
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors

    @track
    def power(self, base: int, exp: int) -> int:
        """Fast exponentiation (exponentiation by squaring). Time: O(log exp)."""
        if exp < 0:
            raise ValueError("negative exponents not supported for integers")
        result = 1
        b = base
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
        
        e = exp
        while e > 0:
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            
            if e & 1:
                result *= b
            b *= b
            e >>= 1
        return result

    @track
    def lcg_random(self, seed: int, count: int) -> list:
        """
        Pseudo-random number generation via a Linear Congruential
        Generator (syllabus term: 'Generating Pseudo-random numbers').
        Time: O(count).
        """
        a, c, m = 1103515245, 12345, 2 ** 31
        values = []
        x = seed
        for _ in range(count):
              #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
            
            x = (a * x + c) % m
            values.append(x)
        return values
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
