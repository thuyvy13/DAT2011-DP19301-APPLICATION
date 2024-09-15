# 3. Sinh viên(Mã, Tên, Ngày sinh, Email, Lớp, Bộ môn)
"""------------------------------------
Module3 này quản lý thông tin của sinh viên.
Bao gồm các thuộc tính:
- Mã: Mã số sinh viên (ID)
- Tên: Họ và tên của sinh viên
- Ngày sinh: Ngày sinh của sinh viên
- Email: Địa chỉ email của sinh viên
- Lớp: Lớp mà sinh viên đang theo học
- Bộ môn: Bộ môn hoặc khoa mà sinh viên thuộc về
------------------------------------"""


class Student:
    def __init__(self, student_id, name, birth_date, email, class_name, department):
        """
        student_id: mã sinh viên
        name: tên sinh viên
        birth_date: ngày sinh của sinh viên
        email: email của sinh viên
        class_name: lớp của sinh viên
        department: bộ môn của sinh viên
        """
        self.student_id = student_id
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.class_name = class_name
        self.department = department
