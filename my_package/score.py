# 1. Điểm số(Đầu điểm, Sinh viên, Môn học, Ngày nhập, Điểm)
"""------------------------------------
Module1 này quản lý thông tin về điểm số của sinh viên.
Bao gồm các thuộc tính:
- Đầu điểm: Thông tin về nguồn của điểm số (ví dụ: thi cuối kỳ, bài tập, v.v.)
- Sinh viên: Thông tin về sinh viên được ghi nhận điểm số
- Môn học: Môn học mà điểm số đó thuộc về
- Ngày nhập: Ngày điểm số được ghi nhận
- Điểm: Giá trị điểm số của sinh viên
------------------------------------"""

from datetime import datetime

class Score:
    def __init__(self, score_id, student, subject, entry_date, score):
        """
        Khởi tạo đối tượng Student.
        
        score_id: mã điểm số
        student: đối tượng Sinh viên
        subject: đối tượng Môn học
        entry_date: ngày nhập điểm
        score: điểm số
        """
        self.score_id = score_id
        self.student = student
        self.subject = subject
        self.entry_date = entry_date
        self.score = score

    def validate_entry_date(self, entry_date):
        if isinstance(entry_date, str):
            try:
                return datetime.strptime(entry_date, "%d/%m/%y")
            except ValueError:
                return datetime.now()
        elif isinstance(entry_date, datetime):
            return entry_date
        else:
            return datetime.now()
        
    def validate_score(self, score):
        if isinstance(score, (int, float)) and 0 <= score <= 10:
            return score
        else:
            raise ValueError("Điểm số phải là một số từ 0 đến 10")
        
    def update_score(self, new_score):
        self.score = self.validate_score(new_score)
        print(f"Điểm số đã được cập nhật thành {self.score}")
        
    def display_info(self):
        print(f"Mã điểm số: {self.score_id}")
        print(f"Sinh viên: {self.student}")
        print(f"Môn học: {self.subject}")
        print(f"Ngày nhập: {self.entry_date.strptime("%d/%m/%y")}")
        print(f"Điểm: {self.score}")


            