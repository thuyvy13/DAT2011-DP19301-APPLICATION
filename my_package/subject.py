# 4. Môn học(Mã, Tên, Mô tả, Tín chỉ, Giảng viên)
"""------------------------------------
Module4 này quản lý thông tin về môn học.
Bao gồm các thuộc tính:
- Mã: Mã định danh của môn học
- Tên: Tên của môn học
- Mô tả: Mô tả ngắn về môn học
- Tín chỉ: Số tín chỉ của môn học
- Giảng viên: Tên giảng viên phụ trách môn học
------------------------------------"""


class Subject:
    def __init__(self, subject_id, name, description, credits, instructor):
        """
        subject_id: mã môn học
        name: tên môn học
        description: mô tả môn học
        credits: tín chỉ của môn học
        instructor: giảng viên môn học
        """
        self.subject_id = subject_id
        self.name = name
        self.description = description
        self.credits = credits
        self.instructor = instructor


        def addSubject(self, subject):
            self.subjects.append(subject)
            print(f"Môn học {subject.name} đã được thêm vào danh sách môn học")
            print("cho nay la cho can sua")

        def removeSubject(self, subject):
            self.subjects.remove(subject)
            print(f"Môn học {subject.name} đã được xóa khỏi danh sách môn học")

        
