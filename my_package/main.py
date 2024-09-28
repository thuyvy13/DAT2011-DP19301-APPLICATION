import sys
import os

# Thêm thư mục hiện tại vào sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from score import menu_controller
from grade_point import GradePoint
from student import menu_module_3
from manh import main_module4
from semester import hien_thi_menu

def menu():
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
    GradePoint()

def insert_student():
    menu_module_3()

def insert_subject():
    main_module4()

def insert_semester():
    hien_thi_menu()

def validate_choice(input_value):
    """Hàm kiểm tra xem giá trị nhập vào có phải là số hợp lệ không."""
    if input_value.isdigit():
        return int(input_value)
    else:
        return None

def print_error_message():
    """In ra thông báo lỗi khi nhập giá trị không hợp lệ."""
    print("\n❌ Lỗi: Lựa chọn không hợp lệ. Vui lòng chỉ nhập các số từ 0 đến 5.")
    print("📌 Lưu ý: Không được nhập ký tự chữ, ký tự đặc biệt hoặc khoảng trắng!")

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
            print("🚪 Thoát chương trình.")
            break
        else:
            print_error_message()
    else:
        print_error_message()
