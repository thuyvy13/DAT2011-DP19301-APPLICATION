import unittest
from datetime import datetime
from my_package.feat.score.score import Score

# score.py

from constants import value_dau_diem
from utils import check_value_dau_diem

# Giả sử bạn có danh sách `scores` lưu trữ điểm sinh viên
scores = []

def get_str_input(prompt):
    return input(prompt).strip()

def get_date_input(prompt):
    from datetime import datetime
    while True:
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
            return date
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập theo định dạng DD/MM/YYYY.")

def check_duplicate_student_id(student_id):
    return any(score['student_id'] == student_id for score in scores)

def display_scores():
    if scores:
        for score in scores:
            print(f"Mã SV: {score['student_id']}, Môn học: {score['subject']}, Điểm: {score['score']}")
    else:
        print("Chưa có dữ liệu điểm số nào.")

def add_scores():
    valid_terms = value_dau_diem()  # Lấy từ điển đầu điểm từ constants.py
    term = check_value_dau_diem("Nhập đầu điểm (Lab, Assignment, Quiz,...): ", valid_terms)
    
    student_id = input("Nhập mã sinh viên (ví dụ: PH47972): ").strip()
    if check_duplicate_student_id(student_id):
        print(f"Mã sinh viên {student_id} đã tồn tại. Vui lòng nhập mã khác.")
        return
    
    subject = get_str_input("Nhập tên môn học (ví dụ: DAT2011): ")
    date = get_date_input("Nhập ngày nhập điểm (DD/MM/YYYY): ")
    score = float(input("Nhập điểm: "))
    
    scores.append({
        "term": term,
        "student_id": student_id,
        "subject": subject,
        "date": date,
        "score": score
    })
    
    print(f"Thêm điểm cho mã sinh viên {student_id} thành công!")
    
    view_choice = input("Bạn có muốn xem danh sách điểm không? (Y/N): ").strip().lower()
    if view_choice == 'y':
        display_scores()
    else:
        print("Quay lại menu chính.")


