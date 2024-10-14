import os
import csv
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
from my_package.common.utils.utils_score import (
    get_str_input, get_score_input, get_yes_no_input,
    validate_and_format_subject, validate_and_format_student_id, confirm_exit_to_menu,
    display_menu
)
from my_package.common.constant.constant_score import score_types
from my_package.modules.score.model.score_model import ScoreModel

class ScoreController:
    """
    @author: Do Thuy Vy
    Controller điều khiển chức năng quản lý điểm sinh viên.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            open(self.file_path, 'w').close()

    def _read_scores_from_file(self):
        """Đọc dữ liệu từ file txt."""
        scores = []
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.strip():
                    score_data = line.strip().split('|')
                    scores.append(ScoreModel(
                        score_data[0],
                        score_data[1],
                        score_data[2],
                        score_data[4],
                        score_data[3]
                    ))
        return scores

    def _write_scores_to_file(self, scores):
        """Ghi dữ liệu điểm số vào file txt."""
        with open(self.file_path, 'w') as file:
            for score in scores:
                file.write(f"{score.get_term()}|{score.get_student_id()}|{score.get_subject()}|{score.get_date()}|{score.get_score()}\n")

    def add_score(self):
        """Thêm điểm mới cho sinh viên và lưu vào file."""
        formatted_student_id, formatted_subject = self._input_student_and_subject()
        entered_key = (formatted_student_id, formatted_subject)
        scores = self._read_scores_from_file()

        while True:
            display_menu(list(score_types.keys()))
            choice = input("Chọn một loại đầu điểm: ").strip()
            if choice == '0':
                return

            if choice.isdigit() and 1 <= int(choice) <= len(score_types):
                selected_type = list(score_types.keys())[int(choice) - 1]
                selected_term = self._select_sub_type(selected_type, entered_key, scores)

                if not selected_term:
                    print(f"Đầu điểm {selected_type} đã được nhập cho sinh viên {formatted_student_id} và môn {formatted_subject}.")
                    continue

                score = get_score_input("Nhập điểm (0-10): ")

                new_score = ScoreModel(selected_term, formatted_student_id, formatted_subject, score)
                scores.append(new_score)

                self._write_scores_to_file(scores)

                print(f"\n✅ Thêm điểm cho sinh viên {formatted_student_id} thành công!")

                if confirm_exit_to_menu():
                    return

    def update_score(self):
        """Cập nhật điểm đã có của sinh viên."""
        formatted_student_id, formatted_subject = self._input_student_and_subject()
        scores = self._read_scores_from_file()
        entered_key = (formatted_student_id, formatted_subject)

        find_scores = [score for score in scores if score.get_student_id() == formatted_student_id and score.get_subject() == formatted_subject]

        if find_scores:
            for i, score in enumerate(find_scores, 1):
                print(f"{i}. Đầu điểm: {score.get_term()}, Điểm: {score.get_score()}, Ngày nhập: {score.get_date()}")

            while True:
                selected_index = input("Chọn đầu điểm để cập nhật (0 để quay lại): ").strip()
                if selected_index.isdigit() and 1 <= int(selected_index) <= len(find_scores):
                    selected_score = find_scores[int(selected_index) - 1]
                    break
                elif selected_index == '0':
                    return
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập số hợp lệ.")

            if get_yes_no_input(f"Bạn có chắc chắn muốn cập nhật điểm cho {selected_score.get_term()}? (Y/N)"):
                selected_score.set_score(get_score_input("Nhập điểm mới (từ 0 đến 10): "))
                selected_score.set_date(datetime.datetime.now().strftime("%d/%m/%Y"))
                self._write_scores_to_file(scores)
                print(f"✅ Cập nhật điểm cho {selected_score.get_term()} thành công!")
        else:
            print(f"❌ Không tìm thấy điểm cho sinh viên {formatted_student_id} và môn {formatted_subject}.")

    def export_scores(self):
        """Xuất bảng điểm sinh viên ra file PDF."""
        formatted_student_id = self._input_student()
        scores = self._read_scores_from_file()
        student_scores = [score for score in scores if score.get_student_id() == formatted_student_id]

        if student_scores:
            file_name = f"{formatted_student_id}_score_report.pdf"
            pdf = canvas.Canvas(file_name, pagesize=letter)
            pdf.setTitle("Bảng điểm sinh viên")

            # Thông tin sinh viên
            pdf.drawString(100, 750, f"Mã sinh viên: {formatted_student_id}")
            pdf.drawString(100, 730, "Bảng điểm sinh viên:")

            # Hiển thị danh sách điểm
            y = 700
            for score in student_scores:
                pdf.drawString(100, y, f"🔹 Đầu điểm: {score.get_term()}, Môn học: {score.get_subject()}, Điểm: {score.get_score()}")
                y -= 20

            pdf.save()
            print(f"✅ Xuất bảng điểm ra file PDF thành công: {file_name}")
        else:
            print(f"❌ Không tìm thấy điểm cho sinh viên {formatted_student_id}.")

    def export_average_scores(self):
        """Xuất trung bình các điểm và tạo biểu đồ từ dữ liệu đó."""
        scores = self._read_scores_from_file()

        # Tính trung bình các đầu điểm theo môn học
        subject_scores = {}
        for score in scores:
            subject = score.get_subject()
            score_value = float(score.get_score())
            if subject not in subject_scores:
                subject_scores[subject] = []
            subject_scores[subject].append(score_value)

        averages = {subject: sum(score_list) / len(score_list) for subject, score_list in subject_scores.items()}

        # Xuất dữ liệu trung bình ra file CSV
        file_name = input("Nhập tên file CSV cho biểu đồ (không bao gồm đuôi .csv): ").strip()
        if not file_name:
            print("❌ Tên file không hợp lệ. Vui lòng thử lại.")
            return

        with open(f"{file_name}_averages.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Môn học", "Điểm trung bình"])
            for subject, avg in averages.items():
                writer.writerow([subject, avg])

        # Vẽ biểu đồ trung bình
        subjects = list(averages.keys())
        avg_scores = list(averages.values())

        plt.bar(subjects, avg_scores)
        plt.xlabel('Môn học')
        plt.ylabel('Điểm trung bình')
        plt.title('Biểu đồ điểm trung bình theo môn học')
        plt.savefig(f"{file_name}_chart.png")
        plt.show()

        print(f"✅ Xuất file CSV và biểu đồ trung bình điểm thành công: {file_name}_averages.csv, {file_name}_chart.png")

    def export_data_to_csv(self):
        """Xuất toàn bộ dữ liệu ra file CSV."""
        scores = self._read_scores_from_file()
        file_name = input("Nhập tên file CSV (không bao gồm đuôi .csv): ").strip()
        if not file_name:
            print("❌ Tên file không hợp lệ. Vui lòng thử lại.")
            return

        with open(f"{file_name}.csv", 'w', newline='') as csvfile:
            fieldnames = ['term', 'student_id', 'subject', 'date', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for score in scores:
                writer.writerow({
                    'term': score.get_term(),
                    'student_id': score.get_student_id(),
                    'subject': score.get_subject(),
                    'date': score.get_date(),
                    'score': score.get_score()
                })

        print(f"✅ Xuất dữ liệu ra file CSV thành công: {file_name}.csv")

    def delete_score(self):
        """Xóa điểm theo mã sinh viên."""
        formatted_student_id, formatted_subject = self._input_student_and_subject()
        scores = self._read_scores_from_file()
        find_scores = [score for score in scores if score.get_student_id() == formatted_student_id]

        if find_scores:
            for i, score in enumerate(find_scores, 1):
                print(
                    f"{i}. Đầu điểm: {score.get_term()}, Môn học: {score.get_subject()}, Ngày nhập: {score.get_date()}, Điểm: {score.get_score()}")

            while True:
                selected_index = input("Chọn đầu điểm để xóa (0 để quay lại): ").strip()
                if selected_index.isdigit() and 1 <= int(selected_index) <= len(find_scores):
                    selected_score = find_scores[int(selected_index) - 1]
                    break
                elif selected_index == '0':
                    return
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập số hợp lệ.")

            if get_yes_no_input(f"Bạn có chắc chắn muốn xóa điểm cho {selected_score.get_term()}? (Y/N)"):
                scores.remove(selected_score)
                self._write_scores_to_file(scores)
                print(f"Xóa điểm cho {selected_score.get_term()} thành công!")
        else:
            print(f"Không tìm thấy điểm cho sinh viên {formatted_student_id}.")

    def display_scores(self):
        """Hiển thị danh sách điểm số."""
        scores = self._read_scores_from_file()
        if scores:
            print("\n=== DANH SÁCH ĐIỂM SỐ ===")
            for score in scores:
                print(
                    f"🔹 Đầu điểm: {score.get_term()}, Mã sinh viên: {score.get_student_id()}, Môn học: {score.get_subject()}, Ngày nhập: {score.get_date()}, Điểm: {score.get_score()}")
            print("\n=========================")
        else:
            print("Chưa có dữ liệu điểm số nào.")

    def filter_scores(self):
        """
        Lọc danh sách điểm số theo nhiều điều kiện: mã sinh viên, môn học, khoảng thời gian và khoảng điểm.
        """
        scores = self._read_scores_from_file()
        filtered_scores = scores  # Bắt đầu với toàn bộ danh sách điểm

        # Lọc theo mã sinh viên
        if get_yes_no_input("Bạn có muốn lọc theo mã sinh viên không? (y/n): "):
            student_id = get_str_input("Nhập mã sinh viên để lọc: ").strip()
            formatted_student_id = validate_and_format_student_id(student_id)
            if formatted_student_id:
                filtered_scores = [score for score in filtered_scores if score.get_student_id() == formatted_student_id]

        # Lọc theo môn học
        if get_yes_no_input("Bạn có muốn lọc theo môn học không? (y/n): "):
            subject = get_str_input("Nhập tên môn học để lọc: ").strip()
            formatted_subject = validate_and_format_subject(subject)
            if formatted_subject:
                filtered_scores = [score for score in filtered_scores if score.get_subject() == formatted_subject]

        # Lọc theo khoảng thời gian
        if get_yes_no_input("Bạn có muốn lọc theo khoảng thời gian không? (y/n): "):
            start_date = get_str_input("Nhập ngày bắt đầu (DD/MM/YYYY): ").strip()
            end_date = get_str_input("Nhập ngày kết thúc (DD/MM/YYYY): ").strip()
            filtered_scores = [score for score in filtered_scores if start_date <= score.get_date() <= end_date]

        # Lọc theo khoảng điểm
        if get_yes_no_input("Bạn có muốn lọc theo khoảng điểm không? (y/n): "):
            min_score = float(get_score_input("Nhập điểm tối thiểu: "))
            max_score = float(get_score_input("Nhập điểm tối đa: "))
            filtered_scores = [score for score in filtered_scores if min_score <= float(score.get_score()) <= max_score]

        # Hiển thị kết quả lọc
        if filtered_scores:
            print("\n=== Kết quả lọc ===")
            for score in filtered_scores:
                print(
                    f"🔹 Đầu điểm: {score.get_term()}, Mã sinh viên: {score.get_student_id()}, Môn học: {score.get_subject()}, Ngày nhập: {score.get_date()}, Điểm: {score.get_score()}")
            print("===================")
        else:
            print("❌ Không tìm thấy kết quả nào khớp với điều kiện lọc.")

    def search_scores(self):
        """
        Tìm kiếm điểm theo mã sinh viên hoặc môn học với gợi ý tự động hoàn thành.
        """
        scores = self._read_scores_from_file()
        search_option = input("Bạn muốn tìm kiếm theo mã sinh viên hay môn học? (sinh viên/môn): ").strip().lower()

        if search_option == "sinh viên":
            search_term = get_str_input("Nhập ký tự đầu của mã sinh viên: ").strip()
            matching_students = list(
                {score.get_student_id() for score in scores if score.get_student_id().startswith(search_term)})

            if matching_students:
                print("\n--- Gợi ý mã sinh viên ---")
                for i, student in enumerate(matching_students, 1):
                    print(f"{i}. {student}")
                student_choice = input("Chọn mã sinh viên (nhập số thứ tự): ").strip()
                if student_choice.isdigit() and 1 <= int(student_choice) <= len(matching_students):
                    selected_student = matching_students[int(student_choice) - 1]
                    student_scores = [score for score in scores if score.get_student_id() == selected_student]

                    print("\n=== Điểm của sinh viên ===")
                    for score in student_scores:
                        print(
                            f"🔹 Đầu điểm: {score.get_term()}, Môn học: {score.get_subject()}, Điểm: {score.get_score()}, Ngày nhập: {score.get_date()}")
                    print("===================")
                else:
                    print("Lựa chọn không hợp lệ.")
            else:
                print(f"❌ Không tìm thấy sinh viên nào bắt đầu với {search_term}.")

        elif search_option == "môn":
            search_term = get_str_input("Nhập ký tự đầu của môn học: ").strip()
            matching_subjects = list(
                {score.get_subject() for score in scores if score.get_subject().startswith(search_term)})

            if matching_subjects:
                print("\n--- Gợi ý môn học ---")
                for i, subject in enumerate(matching_subjects, 1):
                    print(f"{i}. {subject}")
                subject_choice = input("Chọn môn học (nhập số thứ tự): ").strip()
                if subject_choice.isdigit() and 1 <= int(subject_choice) <= len(matching_subjects):
                    selected_subject = matching_subjects[int(subject_choice) - 1]
                    subject_scores = [score for score in scores if score.get_subject() == selected_subject]

                    print("\n=== Điểm của môn học ===")
                    for score in subject_scores:
                        print(
                            f"🔹 Đầu điểm: {score.get_term()}, Mã sinh viên: {score.get_student_id()}, Điểm: {score.get_score()}, Ngày nhập: {score.get_date()}")
                    print("===================")
                else:
                    print("Lựa chọn không hợp lệ.")
            else:
                print(f"❌ Không tìm thấy môn học nào bắt đầu với {search_term}.")
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập 'sinh viên' hoặc 'môn'.")

    # Các method support
    @staticmethod
    def _input_student_and_subject():
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

    @staticmethod
    def _input_student():
        """Nhập mã sinh viên và mã môn học, kiểm tra và trả về dạng hợp lệ."""
        while True:
            student_id = get_str_input("Nhập mã sinh viên (ví dụ: PH47972): ")
            formatted_student_id = validate_and_format_student_id(student_id)
            if formatted_student_id:
                break

        return formatted_student_id

    @staticmethod
    def _select_sub_type(self, score_type, entered_key, scores):
        """Chọn đầu điểm theo loại điểm và kiểm tra xem đầu điểm đã được nhập chưa."""
        available_terms = score_types[score_type].copy()
        entered_scores = [score.get_term() for score in scores if (score.get_student_id(), score.get_subject()) == entered_key]

        if not available_terms:
            print(f"Tất cả bài của {score_type} đã nhập điểm.")
            return None

        available_terms = [term for term in available_terms if term not in entered_scores]

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



