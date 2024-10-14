# constants.py

score_types = {
    "Quiz": ["Quiz 1", "Quiz 2", "Quiz 3", "Quiz 4"],
    "Assignment": ["Assignment 1", "Assignment 2"],
    "Bảo vệ": ["Bảo vệ"],
    "Lab": ["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5", "Lab 6", "Lab 7", "Lab 8"],
    "Bài học Online": ["Online 1", "Online 2", "Online 3", "Online 4", "Online 5", "Online 6", "Online 7", "Online 8"]
}

def confirm_exit():
    """
    Xác nhận người dùng có chắc chắn muốn thoát chương trình hay không.
    """
    while True:
        confirm = input("Bạn có chắc chắn muốn thoát chương trình không? (Y/N): ").strip().lower()
        if confirm == 'y':
            print("Đã thoát chương trình.")
            exit()  # Thoát chương trình
        elif confirm == 'n':
            print("Quay lại menu chính.")
            return  # Quay lại menu chính
        else:
            print("❌ Lựa chọn không hợp lệ. Vui lòng nhập 'Y' hoặc 'N'.")


def menu_view():
    print("\n" + "=" * 40)
    print("    📝  QUẢN LÝ ĐIỂM SỐ SINH VIÊN  📝")
    print("=" * 40)
    print("1️⃣  Hiển thị danh sách điểm số")
    print("2️⃣  🔍  Lọc điểm theo điều kiện")
    print("3️⃣  ➕  Thêm mới điểm số")
    print("4️⃣  ✏️  Cập nhật thông tin điểm số")
    print("5️⃣  🗑️  Xóa điểm số")
    print("6️⃣  📊  ....")
    print("7️⃣  🗓️  Lọc nâng cao bảng điểm")
    print("8️⃣  📈  Xuất bảng điểm sinh viên (PDF)")
    print("9️⃣  📉  Xuất biểu đồ trung bình các đầu điểm")
    print("🔟  📄  Xuất dữ liệu ra file CSV")
    print("0️⃣  🚪 Thoát")
    print("=" * 40)


def out_application():
    while True:
        xac_nhan = input("Bạn có chắc chắn muốn thoát khỏi chức năng  Yes/No (Y/N): ").strip().lower()
        if xac_nhan == 'y':
            return True
        elif xac_nhan == 'n':
            return False
        else:
            print("\n Vui lòng nhập Y (Yes) - N (No)\n")