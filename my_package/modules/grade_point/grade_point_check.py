def get_subject_code():
    while True:
        mon_hoc = input("Nhập mã môn học (bắt đầu với 'DAT' và tiếp theo là số, tối đa 4 số): ").strip().upper()
        if mon_hoc.startswith("DAT") and len(mon_hoc) <= 7 and mon_hoc[3:].isdigit():
            return mon_hoc
        else:
            print("Mã môn học không hợp lệ. Vui lòng nhập lại (ví dụ: DAT1234).")

def get_type_choice():
    while True:
        type_choice = input("Bạn muốn thêm loại đầu điểm nào? (Quiz/Lab/Assignment): ").strip().lower()
        if type_choice in ["quiz", "lab", "assignment"]:
            return type_choice
        else:
            print("Loại đầu điểm không hợp lệ. Vui lòng nhập lại (Quiz/Lab/Assignment).")

def get_number(prompt, min_val, max_val):
    while True:
        number_str = input(prompt)
        try:
            number = int(float(number_str))
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Số phải nằm trong khoảng từ {min_val} đến {max_val}. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

def check_user():

    while True :
        user_input = input("Bạn có muốn thay đổi dữ liệu không Yes/No ? (Y/N): ").strip().lower()
        if user_input == "y":
            print("Bạn đã chọn thay đổi dữ liệu.")
            return True
        elif user_input == "n":
            print("Thao tác bị hủy")
            return False
        else:
            print("Vui lòng nhập Y hoặc N.")

def thoat_chuong_trinh():
    while True:
        xac_nhan = input("Ban co muon thoat chuong trinh khong Yes/No (Y/N): ").strip().lower()
        if xac_nhan == 'y':
            return True
        elif xac_nhan == 'n':
            return False
        else:
            print("\n--- Vui lòng chỉ nhập Y hoặc N ---\n")

def get_subject_choice(score_items):
    # Lấy danh sách môn học
    subjects = set(item['Môn học'] for item in score_items)
    print("Bạn muốn xóa các thành phần trong môn học nào?")
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")

    # Người dùng chọn môn học
    while True:
        subject_choice_str = input("Nhập số tương ứng với môn học: ")
        try:
            subject_choice = int(subject_choice_str)
            if 1 <= subject_choice <= len(subjects):
                chosen_subject = list(subjects)[subject_choice - 1]
                return chosen_subject
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại (1, 2, 3)")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")