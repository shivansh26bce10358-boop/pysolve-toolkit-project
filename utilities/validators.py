"""
validators.py
--------------
Centralised input validation for PySolve.

Non-functional requirement is addressed as: Reliability & Error Handling.
Every public function in the toolkit routes user input through here
instead of trusting raw input(), so a single bad value cannot crash
the CLI session.
"""

from typing import List
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 



class ValidationError(ValueError):
    """Raised when user-supplied input fails a validation rule."""
    pass


def require_non_negative_int(value: str, field_name: str = "value") -> int:
    """Convert `value` to int and ensure it is >= 0."""
    try:
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        parsed = int(value)
    except (TypeError, ValueError):
        raise ValidationError(f"{field_name} must be a whole number, got '{value}'.")
    if parsed < 0:
        raise ValidationError(f"{field_name} must be non-negative, got {parsed}.")
    return parsed


def require_positive_int(value: str, field_name: str = "value") -> int:  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    """Convert `value` to int and ensure it is > 0."""
    parsed = require_non_negative_int(value, field_name)
    if parsed == 0:
        raise ValidationError(f"{field_name} must be greater than zero.")
    return parsed

  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

def require_int_list(values: List[str], field_name: str = "list") -> List[int]:
    """Convert a list of strings to a list of ints, validating each element."""
    if not values:
        raise ValidationError(f"{field_name} cannot be empty.")
    result = []
    for i, v in enumerate(values):  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        try:
            result.append(int(v))
        except (TypeError, ValueError):
            raise ValidationError(
                f"{field_name}[{i}] must be an integer, got '{v}'."
            )
    return result
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 


def require_base(value: str, low: int = 2, high: int = 36) -> int:  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    """Validate a numeral base is within a usable range."""
    base = require_positive_int(value, "base")
    if not (low <= base <= high):  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        raise ValidationError(f"base must be between {low} and {high}, got {base}.")
    return base
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
