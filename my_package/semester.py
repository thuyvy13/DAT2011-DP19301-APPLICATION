# 5. Học kỳ(Mã, Tên, Ngày bắt đầu, Ngày kết thúc, Ghi chú)
"""------------------------------------
Module5 này quản lý thông tin về học kỳ.
Bao gồm các thuộc tính:
- Mã: Mã học kỳ
- Tên: Tên của học kỳ
- Ngày bắt đầu: Ngày bắt đầu của học kỳ
- Ngày kết thúc: Ngày kết thúc của học kỳ
- Ghi chú: Ghi chú thêm liên quan đến học kỳ
------------------------------------"""


class Semester:
    def __init__(self, semester_id, name, start_date, end_date, notes):
        """
        semester_id: mã học kỳ
        name: tên học kỳ
        start_date: ngày bắt đầu học kỳ
        end_date: ngày kết thúc học kỳ
        notes: ghi chú về học kỳ
        """
        self.semester_id = semester_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.notes = notes
