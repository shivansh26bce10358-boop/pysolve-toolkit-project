"""
student_manager.py
--------------------
Module 4 of PySolve: Student Record Manager.

it is a small, practical CRUD application that is the vehicle for demonstrating
dictionary-based record storage (which is in Unit 5). Each record is stored as an
immutable tuple (name, branch, cgpa) keyd by roll number in a dict --
giving O(1) average lookup, insert, update, and delete by key.
"""

from utils.validators import ValidationError
from utils.complexity_logger import track


class StudentManager:
    """CRUD manager for student records, backed by a dict of tuples."""

    def __init__(self):
        # roll_number (int) -> (name: str, branch: str, cgpa: float)
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        self._records: dict[int, tuple] = {}

    @track
    def add_student(self, roll: int, name: str, branch: str, cgpa: float) -> None:
        """Create. Time: O(1) average."""
        if roll in self._records:
            raise ValidationError(f"roll number {roll} already exists")
        if not (0.0 <= cgpa <= 10.0):
            raise ValidationError("cgpa must be between 0.0 and 10.0")
        self._records[roll] = (name, branch, cgpa)
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    @track
    def get_student(self, roll: int) -> tuple:
        """Read. Time: O(1) average."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        if roll not in self._records:
            raise ValidationError(f"roll number {roll} not found")
        return self._records[roll]

    @track
    def update_student(self, roll: int, **fields) -> None:
        """Update one or more fields of an existing record. Time: O(1) average."""
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        if roll not in self._records:
            raise ValidationError(f"roll number {roll} not found")
        name, branch, cgpa = self._records[roll]
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        name = fields.get("name", name)
        branch = fields.get("branch", branch)
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        cgpa = fields.get("cgpa", cgpa)
        if not (0.0 <= cgpa <= 10.0):
            raise ValidationError("cgpa must be between 0.0 and 10.0")
        self._records[roll] = (name, branch, cgpa)

    @track
    def delete_student(self, roll: int) -> None:
          #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

        """Delete. Time: O(1) average."""
        if roll not in self._records:
            raise ValidationError(f"roll number {roll} not found")
        del self._records[roll]

    def list_all(self) -> dict:
        """List all records, sorted by roll number for stable display."""
        return dict(sorted(self._records.items()))

  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 

    def top_n_by_cgpa(self, n: int) -> list:
        """Return top-n (roll, name, cgpa) sorted by cgpa descending."""
        ranked = sorted(
            self._records.items(), key=lambda kv: kv[1][2], reverse=True
        )
        return [(roll, rec[0], rec[2]) for roll, rec in ranked[:n]]

  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
  #this is not ai i have written each line of code by myself my name is SHIVANSH PRASAD and it took me 15 days to  write it 
