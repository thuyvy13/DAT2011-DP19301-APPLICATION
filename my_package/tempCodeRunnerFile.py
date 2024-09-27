while True:
    menu()
    choice = input("Chọn chức năng: ")
    
    if choice == "1":
        insert_semester()
    elif choice == "2":
        insert_subject()
    elif choice == "3":
        menu_module_3()
    elif choice == "4":
        insert_grade_point()
    elif choice == "5":
        hien_thi_menu()
    elif choice == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!\n")
        