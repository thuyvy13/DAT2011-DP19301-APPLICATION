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


