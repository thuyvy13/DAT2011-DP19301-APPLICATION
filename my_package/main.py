"""
File này để import các module và chạy chương trình.
Member config module in this
"""

from score import Score
from grade_point import GradePoint
from student import menu_module_3
from subject import Subject
from semester import hien_thi_menu
from utils import get_number_input
from utils import get_str_input
from utils import get_date_input 
from utils import get_email_input

def menu():
    print("QUẢN LÝ ĐIỂM SỐ")
    print("1. Quản lý học kỳ")
    print("2. Quản lý môn học")
    print("3. Quản lý sinh viên")
    print("4. Thêm đầu điểm")
    print("5. Thêm điểm số")
    print("0. Thoát")   

def insert_semester():
    """
        semester_id: mã học kỳ
        name: tên học kỳ
        start_date: ngày bắt đầu học kỳ
        end_date: ngày kết thúc học kỳ
        notes: ghi chú về học kỳ
    """
    semester_id = get_number_input("Nhập mã học kỳ của sinh viên: ")
    name = get_str_input("Nhập tên học kỳ: ")
    start_date = get_date_input("Nhập ngày bắt đầu học kỳ (dd/mm/yyy): ")
    end_date = get_date_input("Nhập ngày kết thúc học kỳ (dd/mm/yyy): ")
    notes = get_str_input("Nhập ghi chú về học kỳ: ")
    semester = Semester(semester_id, name, start_date, end_date, notes)
    
def insert_subject():
    """
        subject_id: mã môn học
        name: tên môn học
        description: mô tả môn học
        credits: tín chỉ của môn học
        instructor: giảng viên môn học
    """
    subject_id = get_number_input("Nhập mã môn học sinh viên: ")
    name = get_str_input("Nhập tên môn học: ")
    description = get_str_input("Nhập mô tả môn học: ")
    credits = get_number_input("Nhập tín chỉ môn học: ")
    instructor = get_str_input("Nhập giảng viên môn học: ")
    subject = Subject(subject_id, name, description, credits, instructor, subject)
    
def insert_student():
    menu_module_3()
    
def insert_grade_point():
    """
        grade_point_id: mã đầu điểm
        name: tên đầu điểm
        weight: trọng số của đầu điểm
        subject: đối tượng Môn học
        classification: phân loại đầu điểm
    """
    grade_point_id = get_number_input("Nhập mã đầu điểm: ")
    name = get_str_input("Nhập tên đầu điểm: ")
    weight = get_number_input("Nhập trọng số của đầu điểm: ")
    subject = get_str_input("Nhập môn học: ")
    classification = get_str_input("Phân loại đầu điểm: ")
    grade_point = GradePoint(grade_point_id, name, weight, subject, classification)

def insert_score():
    """
        score_id: đầu điểm
        student: đối tượng Sinh viên
        subject: đối tượng Môn học
        entry_date: ngày nhập điểm
        score: điểm số
    """
    score_id = get_str_input("Nhập đầu điểm: ")
    student = get_str_input("Sinh viên: ")
    subject = get_str_input("Môn học: ")
    entry_date = get_date_input("Ngày nhập điểm: ")
    score = get_number_input("Điểm số: ")    
    score_point = Score(score_id, student, subject, entry_date, score)    

while True:
    menu()
    choice = input("Chọn chức năng: ")
    
    if choice == "1":
        insert_semester()
    elif choice == "2":
        insert_subject()
    elif choice == "3":
        menu_module_3()
    elif choice == "4":
        insert_grade_point()
    elif choice == "5":
        hien_thi_menu()
    elif choice == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!\n")
        
