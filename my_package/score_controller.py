from utils_score import (
    get_str_input, get_date_input, get_score_input, get_yes_no_input,
    validate_and_format_subject, validate_and_format_student_id, confirm_exit_to_menu,
    display_menu, confirm_incomplete_functionality
)
from constant_score import score_types

scores = []  # Danh sách chứa điểm của sinh viên
entered_scores = {}  # Lưu lại các đầu điểm đã nhập

# --- Helper Functions ---
def add_scores_prompt():
    """Hiển thị tùy chọn thêm điểm hoặc quay lại menu chính."""
    if get_yes_no_input("Bạn có muốn thêm điểm số không? (Y/N): "):
        add_score()


def input_student_and_subject():
    """Nhập mã sinh viên và mã môn học, kiểm tra và trả về dạng hợp lệ."""
    while True:
        student_id = get_str_input("Nhập mã sinh viên (ví dụ: PH47972): ")
        formatted_student_id = validate_and_format_student_id(student_id)
        if formatted_student_id:
            break

    while True:
        subject = get_str_input("Nhập tên môn học (ví dụ: DAT109 hoặc VIE103.09): ")
        formatted_subject = validate_and_format_subject(subject)
        if formatted_subject:
            break

    return formatted_student_id, formatted_subject


def select_sub_type(score_type, entered_key):
    """Chọn đầu điểm theo loại điểm và kiểm tra xem đầu điểm đã được nhập chưa."""
    available_terms = score_types[score_type].copy()  # Sao chép trạng thái đầu điểm ban đầu
    if not available_terms:
        print(f"Tất cả bài của {score_type} đã nhập điểm.")
        return None

    if entered_key in entered_scores:
        available_terms = [term for term in available_terms if term not in entered_scores[entered_key]]

    if not available_terms:
        print(f"Tất cả đầu điểm của {score_type} cho sinh viên này đã được nhập.")
        return None

    display_menu(available_terms)
    while True:
        choice = input("Chọn một lựa chọn: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(available_terms):
            return available_terms.pop(int(choice) - 1)
        elif choice == '0':
            return None
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số trong danh sách.")


# --- Core Functions ---
def add_score():
    """Thêm điểm mới cho sinh viên và cung cấp tùy chọn tiếp tục thêm điểm."""
    formatted_student_id, formatted_subject = input_student_and_subject()
    entered_key = (formatted_student_id, formatted_subject)

    while True:
        display_menu(list(score_types.keys()))
        choice = input("Chọn một loại đầu điểm: ").strip()
        if choice == '0':
            return

        if choice.isdigit() and 1 <= int(choice) <= len(score_types):
            selected_type = list(score_types.keys())[int(choice) - 1]
            selected_term = select_sub_type(selected_type, entered_key)

            if not selected_term:
                print(f"Đầu điểm {selected_type} đã được nhập cho sinh viên {formatted_student_id} và môn {formatted_subject}.")
                continue  # Chọn lại đầu điểm khác

            date = get_date_input("Nhập ngày nhập điểm (DD/MM/YYYY): ")
            score = get_score_input("Nhập điểm (0-10): ")

            scores.append({
                "term": selected_term,
                "student_id": formatted_student_id,
                "subject": formatted_subject,
                "date": date,
                "score": score
            })

            if entered_key not in entered_scores:
                entered_scores[entered_key] = []
            entered_scores[entered_key].append(selected_term)

            print(f"\n✅ Thêm điểm cho sinh viên {formatted_student_id} thành công!")

            while True:
                print("\n--- Lựa chọn tiếp theo ---")
                print("1. Tiếp tục thêm điểm cho sinh viên này.")
                print("2. Thêm điểm cho sinh viên mới.")
                print("0. Quay lại menu chính.")

                next_choice = input("Chọn một tùy chọn: ").strip()

                if next_choice == '1':
                    # Nếu chọn tiếp tục với sinh viên hiện tại, chỉ thêm đầu điểm mới
                    add_score_for_existing_student(formatted_student_id, formatted_subject)
                    break
                elif next_choice == '2':
                    # Nếu chọn thêm sinh viên mới, reset trạng thái và gọi lại hàm thêm sinh viên
                    add_score()
                    break
                elif next_choice == '0':
                    print("Quay lại menu chính.")
                    return
                else:
                    print("❌ Lựa chọn không hợp lệ. Vui lòng chọn lại.")


def add_score_for_existing_student(formatted_student_id, formatted_subject):
    """Thêm điểm cho sinh viên hiện tại (không nhập lại mã sinh viên và môn học)."""
    entered_key = (formatted_student_id, formatted_subject)

    while True:
        display_menu(list(score_types.keys()))
        choice = input("Chọn một loại đầu điểm: ").strip()
        if choice == '0':
            return

        if choice.isdigit() and 1 <= int(choice) <= len(score_types):
            selected_type = list(score_types.keys())[int(choice) - 1]
            selected_term = select_sub_type(selected_type, entered_key)

            if not selected_term:
                print(f"Đầu điểm {selected_type} đã được nhập cho sinh viên {formatted_student_id} và môn {formatted_subject}.")
                continue  # Chọn lại đầu điểm khác

            date = get_date_input("Nhập ngày nhập điểm (DD/MM/YYYY): ")
            score = get_score_input("Nhập điểm (0-10): ")

            scores.append({
                "term": selected_term,
                "student_id": formatted_student_id,
                "subject": formatted_subject,
                "date": date,
                "score": score
            })

            if entered_key not in entered_scores:
                entered_scores[entered_key] = []
            entered_scores[entered_key].append(selected_term)

            print(f"\n✅ Thêm điểm cho sinh viên {formatted_student_id} thành công!")

            if confirm_exit_to_menu():
                return


def reset_state():
    """Reset lại trạng thái cho một sinh viên mới, làm mới danh sách đầu điểm."""
    global entered_scores
    entered_scores = {}


def display_scores():
    """Hiển thị danh sách điểm số."""
    if scores:
        print("\n=== DANH SÁCH ĐIỂM SỐ ===")
        for score in scores:
            print(f"🔹 Đầu điểm: {score['term']}, Mã sinh viên: {score['student_id']}, Môn học: {score['subject']}, Ngày nhập: {score['date']}, Điểm: {score['score']}")
        print("\n=========================")
    else:
        print("Chưa có dữ liệu điểm số nào.")
        add_scores_prompt()


def delete_score():
    """Xóa điểm theo mã sinh viên."""
    formatted_student_id, formatted_subject = input_student_and_subject()

    find_scores = [score for score in scores if score['student_id'] == formatted_student_id]
    if find_scores:
        for i, score in enumerate(find_scores, 1):
            print(f"{i}. Đầu điểm: {score['term']}, Môn học: {score['subject']}, Ngày nhập: {score['date']}, Điểm: {score['score']}")

        while True:
            selected_index = input("Chọn đầu điểm để xóa (0 để quay lại): ").strip()
            if selected_index.isdigit() and 1 <= int(selected_index) <= len(find_scores):
                selected_score = find_scores[int(selected_index) - 1]
                break
            elif selected_index == '0':
                return
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập số hợp lệ.")

        if get_yes_no_input(f"Bạn có chắc chắn muốn xóa điểm cho {selected_score['term']}?"):
            scores.remove(selected_score)
            entered_scores[(formatted_student_id, selected_score['subject'])].remove(selected_score['term'])
            print(f"Xóa điểm cho {selected_score['term']} thành công!")
    else:
        print(f"Không tìm thấy điểm cho sinh viên {formatted_student_id}.")


def update_score():
    """Cập nhật điểm đã có của sinh viên."""
    formatted_student_id, formatted_subject = input_student_and_subject()
    entered_key = (formatted_student_id, formatted_subject)

    if entered_key in entered_scores:
        for i, term in enumerate(entered_scores[entered_key], 1):
            print(f"{i}. {term}")

        while True:
            selected_option = input("Chọn đầu điểm để cập nhật (0 để quay lại): ").strip()
            if selected_option.isdigit() and 1 <= int(selected_option) <= len(entered_scores[entered_key]):
                selected_term = entered_scores[entered_key][int(selected_option) - 1]
                break
            elif selected_option == '0':
                return
            else:
                print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số hợp lệ.")

        # Tìm điểm tương ứng và cập nhật
        for score in scores:
            if score['student_id'] == formatted_student_id and score['subject'] == formatted_subject and score['term'] == selected_term:
                if get_yes_no_input(f"Bạn có chắc chắn muốn cập nhật điểm cho {selected_term}?"):
                    score['date'] = get_date_input("Nhập ngày mới (DD/MM/YYYY): ")
                    score['score'] = get_score_input("Nhập điểm mới (từ 0 đến 10): ")
                    print(f"✅ Cập nhật điểm cho {selected_term} thành công!")
                return
    else:
        print(f"❌ Sinh viên {formatted_student_id} chưa nhập đầu điểm nào cho môn {formatted_subject}.")


def search_score_by_student_id():
    """Tìm kiếm điểm theo mã sinh viên."""
    while True:
        formatted_student_id, _ = input_student_and_subject()

        find_scores = [score for score in scores if score['student_id'] == formatted_student_id]
        if find_scores:
            print(f"\n🔎 Kết quả tìm kiếm cho sinh viên {formatted_student_id}:")
            entered_terms = {score['term'] for score in find_scores}
            for score in find_scores:
                print(f"🔹 Đầu điểm: {score['term']}, Môn học: {score['subject']}, Ngày nhập: {score['date']}, Điểm: {score['score']}")

            all_terms = {term for terms in score_types.values() for term in terms}
            missing_terms = all_terms - entered_terms
            if missing_terms:
                print("\nNhững đầu điểm còn thiếu: " + ", ".join(missing_terms))
            else:
                print("\n✅ Sinh viên đã nhập đủ tất cả các đầu điểm.")
            break
        else:
            print(f"❌ Không có dữ liệu cho sinh viên {formatted_student_id}.")
            break

def feat_incomplete():
    confirm_incomplete_functionality()