"""------------------------------------
File này chứa các function tiện ích có thể 
tái sử dụng trong toàn dự án. 
------------------------------------"""
from datetime import datetime
import re


def check_score_input(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 10:
                return score
            else:
                print("Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập một số thập phân.")


def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại!")
    
def get_str_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if any(char.isalpha() for char in user_input) and any(char.isdigit() for char in user_input):
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập chuỗi có cả chữ và số!")

def get_date_input(prompt):
    today = datetime.now().strftime("%d/%m/%Y")  
    while True:
        user_input = input(prompt)
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")
            if user_input == today:
                return date
            else:
                print(f"Ngày nhập phải là ngày hôm nay. (Gợi ý: Hôm nay là ngày {today})")
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập theo định dạng DD/MM/YYYY")
                        
def is_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def get_email_input(prompt):
    while True:
        user_input = input(prompt)
        if is_email(user_input):
            return user_input
        else: 
            print("Địa chỉ email không hợp lệ. Vui lòng nhập lại!")
            
def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập 'Y' (Yes) hoặc 'N' (No).")


def get_score_input(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 10:
                return score
            else:
                print("Điểm phải trong khoảng từ 0 đến 10.")
        except ValueError:
            print("Dữ liệu không hợp lệ, vui lòng nhập lại một số thực.")            
            

def check_value_dau_diem(prompt, valid_terms):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input in valid_terms:
            return valid_terms[user_input]
        else:
            print("Đầu điểm không hợp lệ.")
            print("Vui lòng nhập Lab 1 -> 8, Quiz 1 -> 4, hoặc Đánh giá Assignment, Đánh giá Assignment GĐ 1/2.")

def validate_and_format_student_id(student_id):
    student_id = student_id.replace(" ", "").upper()

    if student_id.startswith("PH") and len(student_id) == 7 and student_id[2:].isdigit():
        return student_id
    else:
        print("Mã sinh viên không hợp lệ. Mã sinh viên phải bắt đầu bằng 'PH' và 5 ký tự số ở sau (ví dụ: PH47972).")
        return None
    
    
def confirm_exit_to_menu():
    while True:
        choice = input("Bạn có muốn quay lại menu chính không? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Quay lại menu chính.")
            break  
        elif choice == 'n':
            print("Tiếp tục chức năng hiện tại.")
            break  
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

def confirm_incomplete_functionality():
    while True:
        choice = input("Chức năng này chưa hoàn thiện. Bạn có muốn quay lại menu chính không? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Quay lại menu chính.")
            # Gọi hàm quay lại menu chính ở đây
            return True  # Hoặc gọi hàm menu() tại đây
        elif choice == 'n':
            print("Chức năng chưa hoàn thiện. Tự động quay lại menu chính.")
            return True  # Quay lại menu chính khi chưa hoàn thiện chức năng
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
# def validate_and_format_student_id(student_id):
#     pattern = r'^PH\d{5}$'
#     if re.match(pattern, student_id):
#         return student_id
#     else:
#         return None
    
def validate_and_format_subject(subject):
    pattern = r'^[A-Za-z]+\d+$'
    if re.match(pattern, subject):
        return subject
    else:
        return None