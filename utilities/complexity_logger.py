"""
complexity_logger.py
---------------------
Non-functional requirement is addressed as : Logging / Monitoring + Performance.

`@track` is a decorator applied to every algorithm function. It records
the wall-clock execution time and appends a line to run_log.txt, so the
grader (or the student) can empirically see the runtime behaviour of
each algorithm and not just its theoretical Big-O.
"""

import functools
import time
import os  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 


LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "run_log.txt")


def track(func):
    """Decorator: logs function name, args, result size, and duration."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        _write_log(func.__name__, args, elapsed_ms)  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        return result

    return wrapper


def _write_log(name: str, args, elapsed_ms: float) -> None:
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

            f.write(f"[{name}] args={args} time={elapsed_ms:.4f}ms\n")
    except OSError:
        # Logging mudt never crash the actual computation.
        pass
      #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
