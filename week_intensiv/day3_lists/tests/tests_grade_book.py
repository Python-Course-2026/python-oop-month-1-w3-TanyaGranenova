import pytest
from  week_intensiv.day3_lists.tasks.grade_book import GradeBook

def test_best_student_logic():
    gb = GradeBook()
    gb.students = {
        "Ivan": [5, 5, 4],    # средний 4.66
        "Oleg": [3, 2, 3],    # средний 2.66
        "Anna": [5, 5, 5, 5]  # средний 5.0
    }
    assert gb.get_best_student() == "Anna", "Неверно определен лучший студент"

def test_grade_book_single_student():
    gb = GradeBook()
    gb.students = {"Solo": [4]}
    assert gb.get_best_student() == "Solo"

def test_grade_book_empty():
    gb = GradeBook()
    gb.students = {}
    assert gb.get_best_student() is None, "Если студентов нет, верните None"