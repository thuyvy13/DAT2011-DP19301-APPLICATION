import sys
import os

from my_package.modules.grade_point.grade_point import grade_point
from my_package.modules.semester.semester import hien_thi_menu
from my_package.modules.student.student import menu_module_3
from my_package.modules.subject.manh import main_module_4

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from my_package.modules.score.score import menu_controller

"""
    Chương trình quản lý thông tin học tập sinh viên
    @author: Do Thuy Vy
    @version: 2.0: 
     
"""


def confirm_exit():
    """Hàm yêu cầu xác nhận trước khi thoát chương trình."""
    while True:
        confirmation = input("❓ Bạn có chắc chắn muốn thoát? (y/n): ").strip().lower()
        if confirmation == 'y':
            print("🚪 Thoát chương trình.")
            break
        elif confirmation == 'n':
            return False
        else:
            print("❌ Vui lòng chỉ nhập 'y' (có) hoặc 'n' (không).")

def menu():
    """Hiển thị menu chính."""
    print("\n+------------------------------------------+")
    print("|        📝  QUẢN LÝ ĐIỂM SỐ SINH VIÊN      |")
    print("+------------------------------------------+")
    print("|1️⃣  Quản lý điểm số                        |")
    print("|2️⃣  Quản lý đầu điểm                       |")
    print("|3️⃣  Quản lý sinh viên                      |")
    print("|4️⃣  Quản lý môn học                        |")
    print("|5️⃣  Quản lý học kỳ                         |")
    print("|0️⃣  Thoát                                  |")
    print("+------------------------------------------+")

def insert_score():
    menu_controller()

def insert_grade_point():
    grade_point()

def insert_student():
    menu_module_3()

def insert_subject():
    main_module_4()

def insert_semester():
    hien_thi_menu()

def validate_choice(input_value):
    """Hàm kiểm tra xem giá trị nhập vào có phải là 1 số duy nhất từ 0 đến 5 không."""
    if len(input_value) == 1 and input_value.isdigit():
        num = int(input_value)
        if 0 <= num <= 5:
            return num
    return None

def print_error_message():
    """In ra thông báo lỗi khi lựa chọn không hợp lệ."""
    print("\n❌ Lỗi: Vui lòng chỉ nhập một số nguyên duy nhất từ 0 đến 5.")
    print("📌 Lưu ý: Không được nhập chuỗi dài hoặc ký tự không hợp lệ!")

while True:
    menu()
    choice = input("👉 Nhập lựa chọn của bạn: ").strip()
    valid_choice = validate_choice(choice)

    if valid_choice is not None:
        if valid_choice == 1:
            insert_score()
        elif valid_choice == 2:
            insert_grade_point()
        elif valid_choice == 3:
            insert_student()
        elif valid_choice == 4:
            insert_subject()
        elif valid_choice == 5:
            insert_semester()
        elif valid_choice == 0:
            if confirm_exit():
                break
    else:
        print_error_message()
