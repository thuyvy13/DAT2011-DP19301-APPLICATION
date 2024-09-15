# 2. Đầu điểm(Mã, Tên, Trọng số, Môn học, Phân loại)
"""------------------------------------
Module2 này quản lý thông tin về đầu điểm, tức là các thành phần điểm của sinh viên.
Bao gồm các thuộc tính:
- Mã: Mã định danh của đầu điểm
- Tên: Tên của đầu điểm (ví dụ: Thi cuối kỳ, Bài tập, v.v.)
- Trọng số: Tỷ lệ phần trăm của đầu điểm trong tổng điểm
- Môn học: Môn học mà đầu điểm thuộc về
- Phân loại: Loại của đầu điểm (ví dụ: lý thuyết, thực hành, v.v.)
------------------------------------"""

class GradePoint:
    def __init__(self, grade_point_id, name, weight, subject, classification):
        """
        grade_point_id: mã đầu điểm
        name: tên đầu điểm
        weight: trọng số của đầu điểm
        subject: đối tượng Môn học
        classification: phân loại đầu điểm
        """
        self.grade_point_id = grade_point_id
        self.name = name
        self.weight = weight
        self.subject = subject
        self.classification = classification
