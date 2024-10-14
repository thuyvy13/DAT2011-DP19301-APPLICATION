def check_input(prompt):
    while True:
        xac_nhan = input(prompt).upper().strip()

        # Kiểm tra nếu người dùng nhập số (kể cả dạng số thập phân)
        try:
            float(xac_nhan)
            print("Bạn đã nhập số, vui lòng nhập lại (Y/N).")
            continue
        except ValueError:
            pass

        if xac_nhan == 'Y':
            return 'Y'
        elif xac_nhan == 'N':
            return 'N'
        elif xac_nhan == '':
            print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")

# Hàm xác nhận trước khi thực hiện hành động
def exit_chuc_nang3():
    while True:
            xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
            if xac_nhan == 'Y':
                print("Đang thêm mới sinh viên...")
                # Code xử lý thêm sinh viên ở đây
                break
            elif xac_nhan == 'N':
                print("Thêm mới sinh viên đã bị hủy.")
                break
            elif xac_nhan == '':
                print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
            else:
                print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")
            
import re
from datetime import datetime

def validate_ngay_sinh(ngay_sinh):
    # Kiểm tra định dạng ngày sinh DD/MM/YYYY
    try:
        datetime.strptime(ngay_sinh, '%d/%m/%Y')
        # Kiểm tra xem ngày có lớn hơn ngày hiện tại hay không
        if datetime.strptime(ngay_sinh, '%d/%m/%Y') > datetime.today():
            return False
        return True
    except ValueError:
        return False
    
def validate_email(email):
    # Tạo regex cho email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_ma_sinh_vien(ma_sinh_vien):
    # Kiểm tra định dạng mã sinh viên PH*****
    pattern = r'^PH.{5}$'
    return re.match(pattern, ma_sinh_vien) is not None

def validate_lop(lop):
    # Kiểm tra định dạng lớp DP*****
    pattern = r'^DP.{5}$'
    return re.match(pattern, lop) is not None

# Hàm validate ngày sinh
def validate_ngay_sinh(ngay_sinh):
    from datetime import datetime
    try:
        sinh_nhat = datetime.strptime(ngay_sinh, "%d/%m/%Y")
        if sinh_nhat > datetime.now():
            return False
        return True
    except ValueError:
        return False
    
# Hàm xác nhận trước khi thực hiện hành động
def exit_chuc_nang3():
    while True:
        xac_nhan = input('Mời nhập xác nhận (Y/N): ').upper().strip()
        if xac_nhan == 'Y':
            return True
        elif xac_nhan == 'N':
            print("Hành động đã bị hủy.")
            return False
        elif xac_nhan == '':
            print("Bạn chưa nhập giá trị, vui lòng nhập lại (Y/N).")
        else:
            print("Giá trị không hợp lệ, vui lòng nhập lại (Y/N).")
