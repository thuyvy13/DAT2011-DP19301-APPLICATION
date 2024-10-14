<<<<<<< HEAD
# 1. Điểm số(Đầu điểm, Sinh viên, Môn học, Ngày nhập, Điểm)
"""------------------------------------
Module1 này quản lý thông tin về điểm số của sinh viên.
Bao gồm các thuộc tính:
- Đầu điểm: Thông tin về nguồn của điểm số (ví dụ: lab1, lab2, v.v.)
- Sinh viên: Thông tin về sinh viên được ghi nhận điểm số
- Môn học: Môn học mà điểm số đó thuộc về
- Ngày nhập: Ngày điểm số được ghi nhận
- Điểm: Giá trị điểm số của sinh viên
------------------------------------"""
from utils import get_str_input
from utils import get_date_input
scores = []
def display_scores():
    if scores:
        print("Danh sách điểm số:")
        for score in scores:
            print(f"Đầu điểm: {score['term']}, Mã sinh viên: {score['student_id']}, Môn học: {scores['subject']}, Ngày nhập: {score['date']}, Điểm: {score['score']}")
    else:
        print("Chưa có dữ liệu điểm số nào.")
        add_scores_prompt()
        
def add_scores_prompt():
    choice = get_str_input("Bạn có muốn thêm điểm số không? (Y/N): ").strip().lower()
    if choice == 'Y':
        add_scores()
    else:
        print("Quay lại menu chính")
def add_scores():
    term = get_str_input("Nhập đầu điểm (ví dụ: Lab, Assignment, Quiz,...): ")
    student_id = input("Nhập mã sinh viên (ví dụ: PH47972)")
    subject = get_str_input("Nhập tên môn học (ví dụ: DAT2011): ")
    date = get_date_input("Nhập ngày nhập điểm (YYYY-MM-DD): ")
    score = float(input("Nhập điểm: "))
    
    scores.append({
        "term": term,
        "student_id": student_id,
        "subject": subject,
        "date": date,
        "score": score
    })
    print(f"Thêm điểm cho mã sinh viên {student_id} thành công!")

    view_choice = input("Bạn có muốn xem danh sách điểm không? (Y/N): ").strip().lower()
    if view_choice == 'c':
        display_scores()

def search_scores_by_id(student_id):
    find_scores = [score for score in scores if score['student_id'] == student_id]
    if find_scores:
        print("Kết quả tìm kiếm:")
        for score in find_scores:
            print(f"Đầu điểm: {score['term']}, Mã sinh viên: {score['student_id']}, Môn học: {score['subject']}, Ngày nhập: {score['date']}, Điểm: {score['score']}")
    else:
        print(f"Không tìm thấy điểm cho mã sinh viên {student_id}")
            
def update_scores():
    student_id = input("Nhập mã sinh viên của điểm số cần cập nhật: ")
    for score in scores:
        if score['student_id'] == student_id:
            score['term'] = input("Nhập đầu điểm mới (ví dụ: Giữa kỳ, Cuối kỳ): ")
            score['subject'] = input("Nhập môn học mới: ")
            score['date'] = input("Nhập ngày mới (YYYY-MM-DD): ")
            score['score'] = float(input("Nhập điểm mới: "))
            print(f"Cập nhật điểm số cho mã sinh viên {student_id} thành công!")
            return
    print(f"Không tìm thấy điểm số với mã sinh viên {student_id}")            
    
def delete_scores():
    student_id = input("Nhập mã sinh viên của điểm số cần xóa: ")
    found = False
    
    scores_to_delete = [score for score in scores if score['student_id'] == student_id]

    if scores_to_delete:
        for score in scores_to_delete:
            scores.remove(score)
        found = True
        print(f"Xóa điểm số cho mã sinh viên {student_id} thành công!")
    if not found:
        print(f"Không tìm thấy điểm số với mã sinh viên {student_id}")
            
def menu_module_1():
    while True:
        print("+" + "-" * 42 + "+")
        print("|" + " QUẢN LÝ ĐIỂM SỐ SINH VIÊN ".center(42) + "|")
        print("+" + "-" * 42 + "+")
        print("|" + "1. Hiển thị danh sách điểm số".ljust(42) + "|")
        print("|" + "2. Tìm kiếm/Lọc điểm số".ljust(42) + "|")
        print("|" + "3. Thêm mới điểm số".ljust(42) + "|")
        print("|" + "4. Cập nhật thông tin điểm số".ljust(42) + "|")
        print("|" + "5. Xóa điểm số".ljust(42) + "|")
        print("|" + "6. Hiển thị bảng điểm".ljust(42) + "|")
        print("|" + "7. Hiển thị bảng điểm theo kỳ".ljust(42) + "|")
        print("|" + "8. Phân tích thống kê điểm số".ljust(42) + "|")
        print("|" + "9. Xuất biểu đồ".ljust(42) + "|")
        print("|" + "10. Xuất dữ liệu ra file CSV".ljust(42) + "|")
        print("|" + "0. Thoát".ljust(42) + "|")
        print("+" + "-" * 42 + "+")
        
        choice = input("Chọn chức năng: ")

        if choice == "1":
            display_scores()
        elif choice == "2":
            name = input("Nhập tên sinh viên cần tìm: ")
            search_scores_by_id(name)
        elif choice == "3":
            add_scores()
        elif choice == "4":
            update_scores()
        elif choice == "5":
            delete_scores()
        # elif choice == "6":
        #     analyze_statistics()
        # elif choice == "7":
        #     export_to_csv()
        # elif choice == "8":
            
        # elif choice == "9":
            
        # elif choice == "10":
            
        # elif choice == "0":
        #     print("Thoát chương trình.")
        #     break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")




=======
from score_controller import (
    add_score, update_score, delete_score, search_score_by_student_id,display_scores,feat_incomplete
)

def menu_controller():
    while True:
        print("\n" + "=" * 40)
        print("    📝  QUẢN LÝ ĐIỂM SỐ SINH VIÊN  📝")
        print("=" * 40)
        print("1️⃣  Hiển thị danh sách điểm số")
        print("2️⃣  🔍  Tìm kiếm điểm số")
        print("3️⃣  ➕  Thêm mới điểm số")
        print("4️⃣  ✏️  Cập nhật thông tin điểm số")
        print("5️⃣  🗑️  Xóa điểm số")
        print("6️⃣  📊  Hiển thị bảng điểm")
        print("7️⃣  🗓️  Hiển thị bảng điểm theo kỳ")
        print("8️⃣  📈  Phân tích thống kê điểm số")
        print("9️⃣  📉  Xuất biểu đồ")
        print("🔟  📄  Xuất dữ liệu ra file CSV")
        print("0️⃣  🚪 Thoát")
        print("=" * 40)

        choice = input("Chọn một lựa chọn: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                display_scores()
            elif choice == 2:
                search_score_by_student_id()  
            elif choice == 3:
                add_score()  
            elif choice == 4:
                update_score()  
            elif choice == 5:
                delete_score()  
            elif choice == 6:
                delete_score()
            elif choice == 7:
                feat_incomplete()
            elif choice == 8:
                feat_incomplete()
            elif choice == 9:
                feat_incomplete()
            elif choice == 10:
                feat_incomplete()
            elif choice == 0:
                print("Đã thoát khỏi chương trình.")
                return
            else:
                print("❌ Lựa chọn không hợp lệ. Vui lòng nhập số từ 0 đến 5.")
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập một số.")
>>>>>>> 4c7fc06e3a80b636b39ff7d92a24148e87ab77ee


