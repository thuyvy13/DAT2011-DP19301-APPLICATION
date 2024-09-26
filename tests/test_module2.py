def check_str(prompt):
    user_input = input(prompt)
    if user_input.isalpha():
        return user_input
    else:
        print("Giá trị nhập không hợp lệ, Vui lòng nhập lại!")
        
poem = check_str("Nhập vào ghi chú: ")
print(poem)
