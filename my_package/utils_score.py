"""
------------------------------------
File này chứa các function tiện ích có thể 
tái sử dụng trong toàn dự án. 
------------------------------------
"""

from datetime import datetime
import re

def display_menu(options):
    """Hiển thị menu lựa chọn."""
    print("\nChọn đầu điểm để nhập:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    print("0. Quay lại")

# Nhập và kiểm tra điểm số từ người dùng
def check_score_input(prompt):
    """Yêu cầu người dùng nhập điểm trong khoảng từ 0 đến 10."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 10:
                return score
            else:
                print("Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập một số thập phân.")

# Nhập số nguyên từ người dùng
def get_number_input(prompt):
    """Yêu cầu người dùng nhập số nguyên hợp lệ."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập lại!")

# Nhập chuỗi có chứa cả chữ và số
def get_str_input(prompt):
    """Yêu cầu người dùng nhập chuỗi có cả chữ và số."""
    while True:
        user_input = input(prompt).strip()
        if any(char.isalpha() for char in user_input) and any(char.isdigit() for char in user_input):
            return user_input
        else:
            print("Giá trị không hợp lệ. Vui lòng nhập chuỗi có cả chữ và số!")

# Nhập ngày từ người dùng với định dạng DD/MM/YYYY
def get_date_input(prompt):
    """Yêu cầu người dùng nhập ngày với định dạng DD/MM/YYYY và kiểm tra tính hợp lệ."""
    while True:
        user_input = input(prompt).strip()
        try:
            date = datetime.strptime(user_input, "%d/%m/%Y")  # Kiểm tra định dạng ngày
            return date.strftime("%d/%m/%Y")  # Trả về dạng ngày chuẩn
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập theo định dạng DD/MM/YYYY.")

# Kiểm tra địa chỉ email
def is_email(email):
    """Kiểm tra tính hợp lệ của địa chỉ email."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Nhập email hợp lệ từ người dùng
def get_email_input(prompt):
    """Yêu cầu người dùng nhập địa chỉ email hợp lệ."""
    while True:
        user_input = input(prompt)
        if is_email(user_input):
            return user_input
        else:
            print("Địa chỉ email không hợp lệ. Vui lòng nhập lại!")

# Nhập Yes/No từ người dùng
def get_yes_no_input(prompt):
    """Yêu cầu người dùng nhập lựa chọn Yes hoặc No (Y/N)."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập 'Y' (Yes) hoặc 'N' (No).")

# Nhập và kiểm tra điểm số trong khoảng từ 0 đến 10
def get_score_input(prompt):
    """Yêu cầu người dùng nhập điểm số trong khoảng từ 0 đến 10."""
    while True:
        try:
            score = float(input(prompt).replace(",", "."))  # Đổi dấu phẩy thành dấu chấm cho số thập phân
            if 0 <= score <= 10:
                return score
            else:
                print("Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập một số thực.")

# Kiểm tra đầu điểm hợp lệ
def check_value_dau_diem(prompt, valid_terms):
    """Kiểm tra đầu điểm hợp lệ dựa trên danh sách đầu điểm."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_terms:
            return valid_terms[user_input]
        else:
            print("Đầu điểm không hợp lệ.")
            print("Vui lòng nhập Lab 1 -> 8, Quiz 1 -> 4, hoặc Đánh giá Assignment, Đánh giá Assignment GĐ 1/2.")

# Kiểm tra và định dạng mã sinh viên
def validate_and_format_student_id(student_id):
    """Kiểm tra mã sinh viên. Mã sinh viên hợp lệ phải là 'PH' và 5 số, không có khoảng trắng."""
    student_id = student_id.strip().upper()  # Loại bỏ khoảng trắng ở đầu và cuối
    if " " in student_id:  # Kiểm tra nếu có khoảng trắng ở giữa
        print("Mã sinh viên không được chứa khoảng trắng. Vui lòng nhập lại.")
        return None
    if re.match(r'^PH\d{5}$', student_id):  # Định dạng PH kèm 5 số
        return student_id
    else:
        print("Mã sinh viên không hợp lệ. Định dạng phải là 'PH' kèm 5 ký tự số (ví dụ: PH30375).")
        return None

# Kiểm tra mã môn học
def validate_and_format_subject(subject):
    """Kiểm tra mã môn học theo yêu cầu."""
    subject = subject.strip().upper()  # Loại bỏ khoảng trắng ở đầu và cuối
    
    if " " in subject:  # Kiểm tra nếu có khoảng trắng ở giữa
        print("Mã môn học không được chứa khoảng trắng. Vui lòng nhập lại.")
        return None

    # Định dạng 3 chữ cái theo sau là 3-5 ký tự số
    # Nếu có 5 ký tự số, yêu cầu phải có dấu chấm sau 3 chữ cái và 5 số
    pattern_3_or_4_digits = r'^[A-Z]{3}\d{3,4}$'  # 3 chữ cái và 3-4 số (không có dấu chấm)
    pattern_5_digits_with_dot = r'^[A-Z]{3}\d{3}\.\d{2}$'  # 3 chữ cái và 5 số có dấu chấm

    # Kiểm tra các trường hợp nhập hợp lệ
    if re.match(pattern_3_or_4_digits, subject):
        return subject
    elif re.match(pattern_5_digits_with_dot, subject):
        return subject
    else:
        # Xác định lỗi và cung cấp thông báo phù hợp
        if len(re.findall(r'\d+', subject)) == 0:
            print("Mã môn học phải chứa ít nhất 3 ký tự số sau các chữ cái. Vui lòng nhập lại.")
        elif len(subject) > 3 and len(re.findall(r'\d+', subject)[0]) == 5 and '.' not in subject:
            print("Mã môn học có 5 ký tự số phải bao gồm dấu chấm (ví dụ: DAT123.45). Vui lòng nhập lại.")
        else:
            print("Mã môn học không hợp lệ. Định dạng phải là 3 chữ cái theo sau là 3 hoặc 4 số không có dấu chấm, hoặc 5 số với dấu chấm (ví dụ: DAT123 hoặc VIE103.09).")
        return None

# Xác nhận quay lại menu
def confirm_exit_to_menu():
    """Xác nhận từ người dùng về việc quay lại menu chính."""
    while True:
        choice = input("Bạn có muốn quay lại menu chính không? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Quay lại menu chính.")
            return True  # Quay lại menu
        elif choice == 'n':
            print("Tiếp tục chức năng hiện tại.")
            return False  # Tiếp tục chức năng hiện tại
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


# Xác nhận chức năng chưa hoàn thiện
def confirm_incomplete_functionality():
    """Yêu cầu người dùng xác nhận khi chọn chức năng chưa hoàn thiện."""
    while True:
        choice = input("Chức năng này chưa hoàn thiện. Bạn có muốn quay lại menu chính không? (Y/N): ").strip().lower()
        if choice == 'y':
            print("Quay lại menu chính.")
            return True
        elif choice == 'n':
            print("Chức năng chưa hoàn thiện. Tự động quay lại menu chính.")
            return True
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
