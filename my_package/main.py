"""
File này để import các module và chạy chương trình.
Member config module in this
"""

from score import menu_module_1
from grade_point import GradePoint
from student import menu_module_3
from subject import Subject
from semester import hien_thi_menu
from utils import get_number_input, get_str_input

def menu():
    print("+------------------------------------------+")
    print("|        QUẢN LÝ ĐIỂM SỐ SINH VIÊN         |")
    print("+------------------------------------------+")
    print("|1. Quản lý học kỳ                         |")
    print("|2. Quản lý môn học                        |")
    print("|3. Quản lý sinh viên                      |")
    print("|4. Thêm đầu điểm                          |")
    print("|5. Thêm điểm số                           |")
    print("|0. Thoát                                  |")
    print("+------------------------------------------+")

def insert_score():
    """
    Function to add scores.
    """
    menu_module_1()
    
def insert_grade_point():
    """
    Function to add grade points.
    """
    GradePoint()
    # grade_point_id = get_number_input("Nhập mã đầu điểm: ")
    # name = get_str_input("Nhập tên đầu điểm: ")
    # weight = get_number_input("Nhập trọng số của đầu điểm: ")
    # subject = Subject()  # This needs proper subject assignment logic.
    # classification = get_str_input("Nhập phân loại đầu điểm: ")
    # grade_point = GradePoint(grade_point_id, name, weight, subject, classification)
    # print("Đầu điểm đã được thêm thành công!")

def insert_student():
    """
    Function to manage student details.
    """
    menu_module_3()

def insert_subject():
    """
    Function to manage subject details.
    """
    # subject_id = get_number_input("Nhập mã môn học: ")
    # name = get_str_input("Nhập tên môn học: ")
    # description = get_str_input("Nhập mô tả môn học: ")
    # credits = get_number_input("Nhập tín chỉ môn học: ")
    # instructor = get_str_input("Nhập giảng viên môn học: ")
    # subject = Subject(subject_id, name, description, credits, instructor)
    # print("Môn học đã được thêm thành công!")

def insert_semester():
    """
    Function to manage semester details.
    """
    hien_thi_menu()
    
    

while True:
    menu()
    choice = input("Chọn chức năng: ")

    if choice == "1":
        insert_score()
    elif choice == "2":
        insert_grade_point()
    elif choice == "3":
        insert_student()
    elif choice == "4":
        insert_subject()
    elif choice == "5":
        insert_semester()
    elif choice == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ.Hãy nhập một số nguyên dương!!!\n")
        print("Vui lòng chọn lại từ (1 - 10): ")
