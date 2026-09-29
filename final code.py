"""
main.py – PySolve CLI
1
This is the main file for the PySilve project.
It shows a top-down menu and then sends the user to digferent modules:
 numeric algorithms

 array algorithms
 collections demo
 student record manager

It also validates user input before calling any algorithm and prints
the result on the console.
"""

import sys
from modules.numeric_algorithms import NumericSolver
from modules.array_algorithms import ArraySolver
from modules.collections_explorer import CollectionsExplorer
#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
from modules.student_manager import StudentManager
from utils.validators import (
    ValidationError,
    require_non_negative_int,
    require_positive_int,
    require_int_list,
    require_base,
)

# Create solver objecys
numeric = NumericSolver()
#this is a hand written ciode which took me 15 days 
arrays = ArraySolver()
collections_demo = CollectionsExplorer()
#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
students = StudentManager()


def _prompt(msg: str) -> str:
    """Simple helper to get stripped input from user."""
    return input(msg).strip()
#this is a hand written ciode which took me 15 days 


def numeric_menu():
    """Menu for numeric algorithms."""
    while True:
        print("""
--- Numeric Algorithms ---
1. Factorial
2. Fibonacci (iterative)
3. Fibonacci (fast doubling, O(log n))
4. GCD
5. Reverse a number
6. Base conversion
7. Integer square root
8. Smallest divisor
9. Is prime?
10. Generate primes up to N
11. Prime factorization
12. Power (a^b)
13. Pseudo-random numbers (LCG)
0. Back
""")
        choice = _prompt("Choose: ")

        try:
            if choice == "1":
                n = require_non_negative_int(_prompt("n = "), "n")
                print(f"{n}! = {numeric.factorial(n)}")

            elif choice == "2":
                n = require_non_negative_int(_prompt("n = "), "n")
                print(f"fib({n}) = {numeric.fibonacci(n)}")

#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
            elif choice == "3":
                n = require_non_negative_int(_prompt("n = "), "n")
                print(f"fib_fast({n}) = {numeric.fibonacci_fast(n)}")
                #this is a hand written ciode which took me 15 days 

            elif choice == "4":
                a = require_non_negative_int(_prompt("a = "), "a")
                #this is a hand written ciode which took me 15 days 
                b = require_non_negative_int(_prompt("b = "), "b")
                print(f"gcd({a},{b}) = {numeric.gcd(a, b)}")
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD

            elif choice == "5":
                n = int(_prompt("n = "))
                print(f"reversed = {numeric.reverse_number(n)}")

            elif choice == "6":
                n = int(_prompt("n = "))
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
                base = require_base(_prompt("base (2-36) = "))
                print(f"{n} in base {base} = {numeric.base_convert(n, base)}")

            elif choice == "7":
                #this is a hand written ciode which took me 15 days 
                n = require_non_negative_int(_prompt("n = "), "n")
                print(f"isqrt({n}) = {numeric.integer_sqrt(n)}")

            elif choice == "8":
                n = require_positive_int(_prompt("n = "), "n")
                print(f"smallest divisor of {n} = {numeric.smallest_divisor(n)}")

#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
            elif choice == "9":
                n = require_non_negative_int(_prompt("n = "), "n")
                print(f"{n} is prime: {numeric.is_prime(n)}")
                #this is a hand written ciode which took me 15 days 

            elif choice == "10":
                limit = require_positive_int(_prompt("limit = "), "limit")
                print(f"primes up to {limit}: {numeric.generate_primes(limit)}")
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD

            elif choice == "11":
                n = require_positive_int(_prompt("n = "), "n")
                print(f"prime factors of {n} = {numeric.prime_factors(n)}")
                #this is a hand written ciode which took me 15 days 

            elif choice == "12":
                a = int(_prompt("base = "))
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
                b = require_non_negative_int(_prompt("exponent = "), "exponent")
                print(f"{a}^{b} = {numeric.power(a, b)}")

            elif choice == "13":
                seed = require_non_negative_int(_prompt("seed = "), "seed")
                count = require_positive_int(_prompt("count = "), "count")
                print(f"random sequence: {numeric.lcg_random(seed, count)}")
                #this is a hand written ciode which took me 15 days 

            elif choice == "0":
                return

            else:
                print("Invalid choice.")

        except ValidationError as e:
            #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
            print(f"Input error: {e}")
        except ValueError as e:
            print(f"Error: {e}")


def array_menu():
    """Menu for array-related algorithms."""
    while True:
        print("""
--- Array Algorithms ---
1. Reverse array
2. Count occurrences
3. Find maximum
4. Remove duplicates (ordered)
5. Partition around pivot
6. Kth smallest element
0. Back
""")
        choice = _prompt("Choose: ")

        try:
            if choice == "0":
                return

            # Read array once for all options that need it
            if choice in {"1", "2", "3", "4", "5", "6"}:
                raw = _prompt("Enter numbers space-separated: ").split()
                arr = require_int_list(raw, "array")

            if choice == "1":
                print(f"reversed = {arrays.reverse(arr)}")

            elif choice == "2":
                target = int(_prompt("target = "))
                print(f"count of {target} = {arrays.count_occurrences(arr, target)}")

            elif choice == "3":
                print(f"max = {arrays.find_max(arr)}")
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD

            elif choice == "4":
                print(f"deduplicated = {arrays.remove_duplicates_ordered(arr)}")

            elif choice == "5":
                print(f"partitioned = {arrays.partition(arr)}")

            elif choice == "6":
                k = require_positive_int(_prompt("k = "), "k")
                print(f"{k}th smallest = {arrays.kth_smallest(arr, k)}")

            elif choice != "0":
                print("Invalid choice.")

        except (ValidationError, ValueError) as e:
            print(f"Error: {e}")


def collections_menu():
    """Menu to explore Python collections (list, tuple, set, dict)."""
    while True:
        print("""
--- Collections Explorer ---
1. List operations demo
2. Tuple operations demo
3. Set operations demo (two lists)
4. Dict operations demo
5. Time tradeoff benchmark (list vs dict lookup)
0. Back
""")
        choice = _prompt("Choose: ")

        try:
            if choice == "1":
                raw = _prompt("Enter numbers space-separated: ").split()
                data = require_int_list(raw, "data")
                print(collections_demo.list_operations_demo(data))

            elif choice == "2":
                raw = _prompt("Enter numbers space-separated: ").split()
                data = require_int_list(raw, "data")
                print(collections_demo.tuple_operations_demo(data))


#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
            elif choice == "3":
                a = require_int_list(_prompt("List A: ").split(), "A")
                b = require_int_list(_prompt("List B: ").split(), "B")


                print(collections_demo.set_operations_demo(a, b))

            elif choice == "4":
                raw = _prompt("Enter key=value pairs comma-separated (k=v,k=v): ")
                pairs = [tuple(p.split("=")) for p in raw.split(",") if "=" in p]
                print(collections_demo.dict_operations_demo(pairs))

            elif choice == "5":
                n = require_positive_int(
                    _prompt("n (dataset size, e.g. 20000): "), "n"
                )
                print(collections_demo.time_tradeoff_benchmark(n))

            elif choice == "0":
                return

            else:
                print("Invalid choice.")

        except (ValidationError, ValueError) as e:
            print(f"Error: {e}")
            #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD


def student_menu():
    """Simple student record manager using a dict internally."""
    while True:
        print("""
--- Student Record Manager ---
1. Add student
2. View student
3. Update student
4. Delete student
5. List all
6. Top-N by CGPA
0. Back
""")
        choice = _prompt("Choose: ")

        try:
            if choice == "1":
                roll = require_positive_int(_prompt("Roll: "), "roll")
                name = _prompt("Name: ")

                branch = _prompt("Branch: ")
                cgpa = float(_prompt("CGPA: "))
                #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
                students.add_student(roll, name, branch, cgpa)

                print("Added.")

            elif choice == "2":
                roll = require_positive_int(_prompt("Roll: "), "roll")
                print(students.get_student(roll))

            elif choice == "3":
                roll = require_positive_int(_prompt("Roll: "), "roll")

                cgpa = _prompt("New CGPA (blank to skip): ")
                fields = {"cgpa": float(cgpa)} if cgpa else {}

                students.update_student(roll, **fields)

                print("Updated.")

            elif choice == "4":
                roll = require_positive_int(_prompt("Roll: "), "roll")
                students.delete_student(roll)


                print("Deleted.")

#this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD

            elif choice == "5":
                print(students.list_all())

            elif choice == "6":
                n = require_positive_int(_prompt("N: "), "n")
                print(students.top_n_by_cgpa(n))


            elif choice == "0":
                return

            else:
                print("Invalid choice.")

        except (ValidationError, ValueError) as e:
            print(f"Error: {e}")


def main():
    """Main loop showing the top-level menu."""
    
    while True:
        print("""
====================================
  PySolve - Problem Solving Toolkit
====================================
1. Numeric Algorithms
2. Array Algorithms
3. Collections Explorer
4. Student Record Manager
0. Exit
""")
        choice = _prompt("Choose a module: ")
        #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD

        if choice == "1":
            numeric_menu()

        elif choice == "2":
            array_menu()

        elif choice == "3":
            collections_menu()

        elif choice == "4":
            student_menu()

        elif choice == "0":
            print("Goodbye.")
            sys.exit(0)

        else:

            print("Invalid choice.")


if __name__ == "__main__":
    main()
    #this is not ai i have writen the code and this is my watermark I AM SHIVANSH PRASAD
    print("thank you for viewing my first python project which took me 15 days")