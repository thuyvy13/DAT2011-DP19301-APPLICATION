"""
File này để import các module và chạy chương trình.
"""

from my_package.student import Student

def main():
    # Tạo đối tượng sinh viên
    student = Student(student_id=1, name="Nguyễn Văn A", birth_date="2000-01-01", email="a@example.com", class_name="10A1", department="Toán")
    
    # Thêm điểm cho sinh viên
    student.add_grade(9.0)
    student.add_grade(8.5)

if __name__ == "__main__":
    main()
