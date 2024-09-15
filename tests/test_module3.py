"""
test_module3: Test các chức năng trong module3.

Sử dụng unittest để kiểm tra các phương thức và lớp trong module3.py.
"""

import unittest
from my_package.student import Student

class TestStudent(unittest.TestCase):
    """
    Class này chứa các bài test cho module `module1.py` 
    """

    def test_add_grade(self):
        """
        Test phương thức thêm điểm cho sinh viên.
        """
        student = Student(student_id=1, name="Nguyen Van A", birth_date=None, email="a@example.com", class_name="10A1", department="Toán")
        student.add_grade(7.5)
        self.assertEqual(student.get_grades(), [7.5])

if __name__ == "__main__":
    unittest.main()
