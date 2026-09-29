# Problem Statement
When you’re just starting out, algorithms like factorial, GCD, primality testing, array reversal, and dictionary lookups usually appear as separate textbook exercises. You solve one, move to the next, and rarely see how they fit together in a real program.

What’s often missing is a single, well-organized codebase where:

Each technique is implemented correctly

The implementations are tested

Everything is exposed through one consistent interface

That missing piece matters because it shows how top-down design (from Unit 1) can turn a collection of independent algorithms into a coherent, working application.

PySolve fills that gap for CSE1021. It takes every major algorithm category from the syllabus (Units 1, 3, 4, and 5) and packages them into a modular, tested Python toolkit driven by a single command-line app.

In practice, this means you can:

Run any algorithm (factorial, GCD, prime checks, array operations, dictionary-based CRUD, etc.) from the same CLI.

Inspect clean, reference implementations instead of scattered snippets.

See how a top-down design ties problem analysis, algorithm choice, and program structure into one system.

Instead of learning algorithms as isolated exercises, you get a unified learning environment that mirrors how real programs are built.




# Scope of the Project

In scope
This toolkit focuses only on what’s actually taught in CSE1021 and stays aligned with Units 3, 4, and 5 of the syllabus.

Numeric algorithms (Units 3 & 4)

Factorial

Fibonacci

GCD

Primality testing

Integer factorization

Integer square root

Base conversion

Fast exponentiation

Pseudo-random number generation

Array algorithms (Unit 5)

Reversal

Counting occurrences

Finding the maximum element

Removing duplicates (deduplication)

Partitioning around a pivot

Finding the Kth-smallest element

Python collections (Unit 5)

Working with lists, tuples, sets, and dictionaries as covered in the course.

An empirical demonstration comparing:

Linear search in a list (O(n))

Key-based lookup in a dictionary (average O(1))
to show the time tradeoff between the two approaches.

Practical CRUD application

A Student Record Manager that uses dictionary-based storage (roll number → (name, branch, cgpa) tuple) to implement:

Create, Read, Update, Delete operations

A realistic, course-aligned use case for Unit 5 concepts.

Non-functional requirements

Basic input validation

Simple error handling

Minimal execution logging to help with debugging and understanding program flow.

Out of scope
To keep this strictly tied to CSE1021, the following are intentionally excluded:

GUI or web interfaces – the course focuses on console-based problem solving and core Python, not front-end development.

Persistent storage (files, databases) – Unit 5 covers in-memory collections only; there is no DBMS or file-handling component in this course.

Machine learning, networking, or distributed systems – these belong to later, more advanced courses, not to “Introduction to Problem Solving and Programming.”

In short: this is a syllabus-faithful, CLI-only, in-memory toolkit that demonstrates exactly what CSE1021 expects you to learn, nothing more.


# Target Users

-Primary audience:
The course instructor or TA who will evaluate this submission against the CSE1021 learning outcomes. The design, structure, and implemented algorithms are chosen specifically to demonstrate mastery of the syllabus topics in Units 1, 3, 4, and 5.

Secondary audience:
A first-year CS student using the CLI as an interactive study and revision tool. They can:

Run each algorithm with their own inputs

Observe outputs and behavior directly

Use the toolkit to reinforce concepts from lectures and labs

In other words, it’s built first to meet course requirements, and second to serve as a hands-on learning aid for students revisiting CSE1021 topics.


# High-Level Features

1. **Numeric Algorithms Engine** -- there are  13 algorithms from Units 3 & 4,
   each with documented time/space complexity.
2. **Array Algorithms Lab** --there are  6 classical array techniques from Unit 5.
3. **Collections Explorer** -- List/Tuple/Set/Dict operation demos plus
   a real, measured benchmark proving dict lookup outperforms list scan.
4. **Student Record Manager** -- a CRUD system built on a dict-of-tuples,
   showing collections applied to a realistic problem.
5. **Unified CLI** -- one entry point (`main.py`) with a top-down menu
   structure connecting all four modules.
6. **Automated tests** -- 30 unit tests (`unittest`) covering correctness
   and edge cases across all modules.
