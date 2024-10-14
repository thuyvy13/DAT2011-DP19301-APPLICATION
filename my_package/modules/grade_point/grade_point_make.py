import re
import csv

from my_package.modules.grade_point.grade_point_check import get_subject_code, get_type_choice, get_number, check_user, \
    thoat_chuong_trinh

score_items = []


def display_scores():
    if not score_items:
        print("Danh sách đầu điểm trống.")
        return
    print(f"{'Mã':<15} {'Tên':<20} {'Trọng số (%)':<15} {'Môn học':<15} {'Phân loại'}")
    print("-" * 70)
    for item in score_items:
        print(
            f"{item['Mã']:<15} {item['Tên']:<20} {item['Trọng số (%)']:<15} {item['Môn học']:<15} {item['Phân loại']}")

def add_score():
    while True:
        global score_items  # Đảm bảo biến score_items có thể được sửa đổi trong hàm

        # Kiểm tra mã môn học
        mon_hoc = get_subject_code()

        # Nhập loại đầu điểm và kiểm tra
        type_choice = get_type_choice()

        if type_choice == "quiz":
            current_quiz_count = sum(1 for item in score_items if 'Quiz' in item['Tên'])
            if current_quiz_count >= 4:
                print("Đã đạt tối đa 4 quiz. Không thể thêm thêm quiz.")
                return

            quiz_number = get_number("Bạn muốn thêm quiz số mấy? (1-4): ", 1, 4)
            ma_diem = f"QZ{quiz_number:02}"

            # Kiểm tra mã đầu điểm có tồn tại không
            while any(item['Mã'] == ma_diem and item['Môn học'] == mon_hoc for item in score_items):
                print(f"Quiz {quiz_number} đã tồn tại trong môn {mon_hoc}. Vui lòng nhập một quiz khác.")
                quiz_number = get_number("Nhập lại số thứ tự quiz: (1-4): ", 1, 4)
                ma_diem = f"QZ{quiz_number:02}"

            score_items.append({
                "Mã": ma_diem,
                "Tên": f"Quiz {quiz_number}",
                "Trọng số (%)": 3,
                "Môn học": mon_hoc,
                "Phân loại": "Lý thuyết"
            })
            print(f"Đã thêm {ma_diem} - Quiz {quiz_number}.")

        elif type_choice == "lab":
            current_lab_count = sum(1 for item in score_items if 'Lab' in item['Tên'])
            if current_lab_count >= 8:
                print("Đã đạt tối đa 8 lab. Không thể thêm thêm lab.")
                return

            lab_number = get_number("Bạn muốn thêm lab số mấy? (1-8): ", 1, 8)
            ma_diem = f"LB{lab_number:02}"

            # Kiểm tra lab đã tồn tại hay chưa
            while any(item['Mã'] == ma_diem and item['Môn học'] == mon_hoc for item in score_items):
                print(f"Lab {lab_number} đã tồn tại trong môn {mon_hoc}. Vui lòng nhập một lab khác.")
                lab_number = get_number("Nhập lại lab số mấy? (1-8): ", 1, 8)
                ma_diem = f"LB{lab_number:02}"

            score_items.append({
                "Mã": ma_diem,
                "Tên": f"Lab {lab_number}",
                "Trọng số (%)": 3.5,
                "Môn học": mon_hoc,
                "Phân loại": "Thực hành"
            })
            print(f"Đã thêm {ma_diem} - Lab {lab_number}.")

        elif type_choice == "assignment":
            current_assignment_count = sum(1 for item in score_items if 'Assignment' in item['Tên'])
            if current_assignment_count >= 3:
                print("Đã đạt tối đa 3 assignment. Không thể thêm thêm assignment.")
                return

            assignment_number = get_number("Bạn muốn thêm assignment số mấy? (1-3): ", 1, 3)
            ma_diem = f"ASS{assignment_number:02}"

            # Kiểm tra assignment đã tồn tại hay chưa
            while any(item['Mã'] == ma_diem and item['Môn học'] == mon_hoc for item in score_items):
                print(
                    f"Assignment {assignment_number} đã tồn tại trong môn {mon_hoc}. Vui lòng nhập một assignment khác.")
                assignment_number = get_number("Nhập lại số thứ tự assignment: (1-3): ", 1, 3)
                ma_diem = f"ASS{assignment_number:02}"

            # Đặt tên và trọng số cho assignment
            if assignment_number == 3:
                ten_assignment = "Assignment Final"
                trong_so = 40
            else:
                ten_assignment = f"Assignment {assignment_number}"
                trong_so = 10

            score_items.append({
                "Mã": ma_diem,
                "Tên": ten_assignment,
                "Trọng số (%)": trong_so,
                "Môn học": mon_hoc,
                "Phân loại": "Thực hành"
            })
            print(f"Đã thêm {ma_diem} - {ten_assignment}.")

        if not check_user():
            print('Hủy chức năng thêm học sinh')
            break

def delete_score():
    while True:
        if not score_items:
            print("Danh sách đầu điểm trống. Không thể xóa.")
            return

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
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại (1 , 2 , 3)")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        # Hiển thị các quiz, lab và assignment thuộc môn học đã chọn
        items_to_delete = [item for item in score_items if item['Môn học'] == chosen_subject]

        if not items_to_delete:
            print(f"Không có thành phần nào trong môn học {chosen_subject}.")
            return

        print(f"Các thành phần trong môn học '{chosen_subject}':")
        for index, item in enumerate(items_to_delete, start=1):
            print(f"{index}. {item['Tên']} - Mã: {item['Mã']}")

        # Người dùng chọn thành phần để xóa
        while True:
            delete_choice_str = input("Nhập số tương ứng với thành phần bạn muốn xóa: ")
            try:
                delete_choice = int(delete_choice_str)
                if 1 <= delete_choice <= len(items_to_delete):
                    item_to_delete = items_to_delete[delete_choice - 1]
                    score_items.remove(item_to_delete)
                    print(f"Đã xóa thành phần: {item_to_delete['Tên']} - Mã: {item_to_delete['Mã']}")
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        if not check_user():
            print('Hủy chức năng xóa')
            break

def check_subject_exists():
    if not score_items:
        print("Danh sách đầu điểm trống.")
        return
    while True:
        mon_hoc = get_subject_code()
        # Tạo biểu thức chính quy để tìm kiếm tên môn
        pattern = re.compile(re.escape(mon_hoc), re.IGNORECASE)  # Tìm kiếm không phân biệt chữ hoa chữ thường

        # Tìm kiếm trong danh sách
        matched_subjects = [item for item in score_items if pattern.search(item['Môn học'])]

        if matched_subjects:
            print(f"Có {len(matched_subjects)} môn học phù hợp với '{mon_hoc}':")
            for subject in matched_subjects:
                print(
                    f"{subject['Mã']:<15} {subject['Tên']:<20} {subject['Trọng số (%)']:<15} {subject['Môn học']:<15} {subject['Phân loại']}")
        else:
            print(f"Tên môn '{mon_hoc}' không có trong danh sách.")

        if thoat_chuong_trinh():
            print("Cảm ơn bạn đã sử dụng chức năng")
            break
        else:
            print("Tiếp tục chương trình")

def update_score():
    global score_items  # Đảm bảo biến score_items có thể được sửa đổi trong hàm

    if not score_items:
        print("Danh sách đầu điểm trống.")
        return

    while True:

        subjects = set(item['Môn học'] for item in score_items)
        print("Bạn muốn câp nhật các thành phần trong môn học nào?")
        for index, subject in enumerate(subjects, start=1):
            print(f"{index}. {subject}")

        # Người dùng chọn môn học
        while True:
            subject_choice_str = input("Nhập số tương ứng với môn học: ")
            try:
                subject_choice = int(subject_choice_str)
                if 1 <= subject_choice <= len(subjects):
                    chosen_subject = list(subjects)[subject_choice - 1]
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại (1, 2, 3)")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        # Nhập loại đầu điểm và kiểm tra
        while True:
            type_choice = input("Bạn muốn cập nhật loại đầu điểm nào? (Quiz/Lab/Assignment): ").strip().lower()
            if type_choice in ["quiz", "lab", "assignment"]:
                existing_items = [item for item in score_items if
                                  item['Môn học'] == chosen_subject and type_choice.capitalize() in item['Tên']]
                if existing_items:
                    break
                else:
                    print(f"{type_choice.capitalize()} không tồn tại trong môn {chosen_subject}. Vui lòng nhập lại.")
            else:
                print("Loại đầu điểm không hợp lệ. Vui lòng nhập lại (Quiz/Lab/Assignment).")

        # Hiển thị danh sách các đầu điểm hiện có
        print("Danh sách đầu điểm hiện có:")
        for item in existing_items:
            print(f"- {item['Tên']} (Mã: {item['Mã']}, Trọng số: {item['Trọng số (%)']}%)")

        # Nhập số thứ tự của quiz, lab hoặc assignment mà bạn muốn sửa
        while True:
            quiz_number_str = input(
                f"Nhập số thứ tự {type_choice} bạn muốn sửa (1-4 cho Quiz, 1-8 cho Lab, 1-3 cho Assignment): ")
            try:
                quiz_number = int(float(quiz_number_str))
                if type_choice == "quiz" and 1 <= quiz_number <= 4:
                    ma_diem = f"QZ{quiz_number:02}"  # Cấu trúc mã quiz
                    break
                elif type_choice == "lab" and 1 <= quiz_number <= 8:
                    ma_diem = f"LB{quiz_number:02}"  # Cấu trúc mã lab
                    break
                elif type_choice == "assignment" and 1 <= quiz_number <= 3:
                    ma_diem = f"ASS{quiz_number:02}"  # Cấu trúc mã assignment
                    break
                else:
                    print("Số thứ tự không hợp lệ. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        # Kiểm tra mã đầu điểm có tồn tại không trong danh sách
        if any(item['Mã'] == ma_diem and item['Môn học'] == chosen_subject for item in score_items):
            item_to_update = next(
                item for item in score_items if item['Mã'] == ma_diem and item['Môn học'] == chosen_subject)
        else:
            print("Mã đầu điểm không tồn tại trong danh sách cho môn học này.")
            return

        # Nhập số thứ tự mới cho quiz, lab hoặc assignment
        while True:
            new_number_str = input(
                f"Nhập số thứ tự mới cho {item_to_update['Tên']} (nếu là Quiz, 1-4; nếu là Lab, 1-8; nếu là Assignment, 1-3): ")
            try:
                new_number = int(new_number_str)
                if (type_choice == "quiz" and 1 <= new_number <= 4) or (
                        type_choice == "lab" and 1 <= new_number <= 8) or (
                        type_choice == "assignment" and 1 <= new_number <= 3):
                    # Kiểm tra xem mã mới đã tồn tại chưa
                    new_ma_diem = f"QZ{new_number:02}" if type_choice == "quiz" else f"LB{new_number:02}" if type_choice == "lab" else f"ASS{new_number:02}"

                    if any(item['Mã'] == new_ma_diem and item['Môn học'] == chosen_subject for item in score_items):
                        print(f"Không thể cập nhật thành {type_choice.capitalize()} {new_number} vì nó đã tồn tại.")
                        continue  # Yêu cầu người dùng nhập lại số thứ tự mới
                    break
                else:
                    print("Số thứ tự không hợp lệ. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        # Cập nhật thông tin
        for item in score_items:
            if item['Mã'] == ma_diem and item['Môn học'] == chosen_subject:
                old_name = item['Tên']  # Lưu tên cũ
                old_code = item['Mã']  # Lưu mã cũ
                item['Tên'] = f"{type_choice.capitalize()} {new_number}"  # Cập nhật tên mới
                item['Mã'] = new_ma_diem  # Cập nhật mã mới
                print(f"Đã cập nhật {old_name} (Mã: {old_code}) thành {item['Tên']} (Mã: {item['Mã']}).")
                break

        if not check_user():
            print('Hủy chức năng cập nhật')
            break

def find_highest_score():
    if not score_items:
        print("Danh sách đầu điểm trống.")
        return
    while True:
        # Liệt kê các môn học có trong danh sách
        subjects = set(item['Môn học'] for item in score_items)
        if not subjects:
            print("Không có môn học nào trong danh sách.")
            return

        print("Các môn học có trong danh sách (bắt đầu với 'DAT'):")
        for index, subject in enumerate(subjects, start=1):
            if subject.startswith("DAT"):
                print(f"{index}. {subject}")

        while True:
            selected_subject = input("Chọn mã môn học để tìm đầu điểm có trọng số cao nhất: ").strip().upper()
            if selected_subject in subjects:
                break
            else:
                print("Môn học không hợp lệ. Vui lòng chọn lại.")

        # Tìm đầu điểm có trọng số cao nhất trong môn học đã chọn
        highest_score_item = max(
            (item for item in score_items if item['Môn học'] == selected_subject),
            key=lambda item: item['Trọng số (%)'],
            default=None
        )

        if highest_score_item:
            print(f"\nĐầu điểm có trọng số cao nhất trong môn '{selected_subject}':")
            print(
                f"Mã: {highest_score_item['Mã']}, Tên: {highest_score_item['Tên']}, Trọng số: {highest_score_item['Trọng số (%)']}%, Môn học: {highest_score_item['Môn học']}, Phân loại: {highest_score_item['Phân loại']}")
        else:
            print(f"Không có đầu điểm nào trong môn '{selected_subject}'.")

        if thoat_chuong_trinh():
            print("Cảm ơn bạn đã sử dụng chức năng")
            break
        else:
            print("Tiếp tục chương trình")

def Thong_ke():
    print("Thực hiện thống kê số lượng đầu điểm theo từng môn học.")

    if not score_items:
        print("Danh sách đầu điểm trống. Không thể thực hiện thống kê.")
        return
    while True:
        # Tạo danh sách các môn học có trong score_items
        subjects = set(item['Môn học'] for item in score_items)

        for subject in subjects:
            current_quiz_count = sum(1 for item in score_items if item['Môn học'] == subject and 'QZ' in item['Mã'])
            current_lab_count = sum(1 for item in score_items if item['Môn học'] == subject and 'LB' in item['Mã'])
            current_assignment_count = sum(
                1 for item in score_items if item['Môn học'] == subject and 'ASS' in item['Mã'])

            # Tính số lượng đầu điểm còn thiếu
            quizzes_needed = 4 - current_quiz_count
            labs_needed = 8 - current_lab_count
            assignments_needed = 3 - current_assignment_count

            # Hiển thị kết quả thống kê
            print(f"\nMôn học: {subject}")
            print(
                f"Số lượng quiz hiện có: {current_quiz_count}, cần thêm: {quizzes_needed if quizzes_needed > 0 else 0}")
            print(f"Số lượng lab hiện có: {current_lab_count}, cần thêm: {labs_needed if labs_needed > 0 else 0}")
            print(
                f"Số lượng assignment hiện có: {current_assignment_count}, cần thêm: {assignments_needed if assignments_needed > 0 else 0}")

        if thoat_chuong_trinh():
            print("Cảm ơn bạn đã sử dụng chức năng")
            break
        else:
            print("Tiếp tục chương trình")

def kiem_tra():
    if not score_items:
        print("Danh sách đầu điểm trống. Không thể thực hiện kiểm tra.")
        return

    while True:
        Mon_hoc = get_subject_code()

        # Kiểm tra định dạng mã đầu điểm
        if not re.match(r'^DAT\d{1,4}$', Mon_hoc):
            print(" Đầu điểm không hợp lệ. Mã phải bắt đầu bằng 'DAT' và chỉ có tối đa 4 số phía sau.")
            return

        # Kiểm tra sự tồn tại của mã đầu điểm
        for item in score_items:
            if item['Môn học'] == Mon_hoc:
                print(f"Môn học '{Mon_hoc}' tồn tại trong danh sách.")
                return

        print(f"Môn học '{Mon_hoc}' không tồn tại trong danh sách.")

        if thoat_chuong_trinh():
            print("Cảm ơn bạn đã sử dụng chức năng")
            break
        else:
            print("Tiếp tục chương trình")

def kiem_tra_thua_thieu():
    if not score_items:
        print("Danh sách đầu điểm trống. Không thể kiểm tra.")
        return

    while True:
        # Lấy danh sách các môn học
        subjects = set(item['Môn học'] for item in score_items)
        print("Bạn muốn kiểm tra môn học nào?")
        for index, subject in enumerate(subjects, start=1):
            print(f"{index}. {subject}")

        # Người dùng chọn môn học
        while True:
            subject_choice_str = input("Nhập số tương ứng với môn học: ")  # Sửa hàm get_subject_code() thành input()
            try:
                subject_choice = int(subject_choice_str)
                if 1 <= subject_choice <= len(subjects):
                    chosen_subject = list(subjects)[subject_choice - 1]
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ.")

        # Lọc các đầu điểm thuộc môn học đã chọn
        items_to_check = [item for item in score_items if item['Môn học'] == chosen_subject]

        # Đếm số lượng từng loại đầu điểm trong môn học đã chọn
        expected_quiz = 4
        expected_lab = 8
        expected_assignment = 3

        current_quiz_count = sum(1 for item in items_to_check if 'Quiz' in item['Tên'])
        current_lab_count = sum(1 for item in items_to_check if 'Lab' in item['Tên'])
        current_assignment_count = sum(1 for item in items_to_check if 'Assignment' in item['Tên'])

        print(f"--- Kiểm tra môn học: {chosen_subject} ---")
        if current_quiz_count == expected_quiz:
            print("Quiz: Đủ")
        elif current_quiz_count < expected_quiz:
            print(f"Quiz: Thiếu {expected_quiz - current_quiz_count} quiz.")
        else:
            print(f"Quiz: Thừa {current_quiz_count - expected_quiz} quiz.")

        if current_lab_count == expected_lab:
            print("Lab: Đủ")
        elif current_lab_count < expected_lab:
            print(f"Lab: Thiếu {expected_lab - current_lab_count} lab.")
        else:
            print(f"Lab: Thừa {current_lab_count - expected_lab} lab.")

        if current_assignment_count == expected_assignment:
            print("Assignment: Đủ")
        elif current_assignment_count < expected_assignment:
            print(f"Assignment: Thiếu {expected_assignment - current_assignment_count} assignment.")
        else:
            print(f"Assignment: Thừa {current_assignment_count - expected_assignment} assignment.")

        # Kiểm tra điều kiện thoát chương trình
        if thoat_chuong_trinh():
            print("Cảm ơn bạn đã sử dụng chức năng.")
            break
        else:
            print("Tiếp tục chương trình.")

def xuat_file_csv():
    if not score_items:
        print("Danh sách đầu điểm trống. Không thể xuất file.")
        return

    # Lấy danh sách các môn học
    subjects = set(item['Môn học'] for item in score_items)
    print("Bạn muốn xuất file cho môn học nào?")
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")

    # Người dùng chọn môn học
    while True:
        subject_choice_str = input("Nhập số tương ứng với môn học: ")
        try:
            subject_choice = int(subject_choice_str)
            if 1 <= subject_choice <= len(subjects):
                chosen_subject = list(subjects)[subject_choice - 1]
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ.")

    # Lọc các đầu điểm thuộc môn học đã chọn
    items_to_export = [item for item in score_items if item['Môn học'] == chosen_subject]

    # Nếu không có đầu điểm nào
    if not items_to_export:
        print(f"Không có đầu điểm nào trong môn học {chosen_subject}.")
        return

    # Tên file CSV
    filename = f"{chosen_subject}_scores.csv"

    # Ghi dữ liệu vào file CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Mã", "Tên", "Trọng số (%)", "Môn học", "Phân loại"])
        writer.writeheader()
        writer.writerows(items_to_export)

    print(f"Đã xuất file {filename} thành công.")




