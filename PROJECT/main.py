# Danh sách chứa các dictionary (mỗi dictionary là 1 sinh viên)
students = []

# Hàm thêm sinh viên mới
def add_student():
    print("\n_____Them mot sinh vien_____")
    sid = input("Nhap ma sinh vien: ")
    name = input("Nhap ten sinh vien: ")
    score1 = float(input("Diem thanh phan 1: "))
    score2 = float(input("Diem thanh phan 2: "))
    score3 = float(input("Diem thanh phan 3: "))


    student = {
        "id" : sid,
        "name" : name,
        "score1" : score1 ,
        "score2" : score2  ,
        "score3" : score3 , 
        "overall" : round(score1*0.1 +  score2*0.3 + score3*0.6 , 2)
    }

    students.append(student)
    print("Them sinh vien thanh cong!\n")


# Hàm tìm kiếm sinh viên theo MSV 
def search_student_MSV():
    print("\n_____Tim kiem bang ma sinh vien_____")
    sid = input("Nhap ma sinh vien de tim kiem: ")

    for s in students:
        if s["id"] == sid:
            print(f"Found: ID={s['id']}, Name={s['name']}, Score1={s['score1']} , Score2={s['score2']} , Score3={s['score3']} , Overall={s['overall']}\n")
            return
    
    print("Khong tim thay sinh vien co MSV nay.\n")

# Hàm tìm kiếm theo Họ và Tên 
def search_student_name() : 
    print("\n_____Tim kiem bang ho va ten______") 
    name = input("Nhap ho va ten de tim kiem : ") 

    for s in students : 
        if s["name"].lower() == name.lower() : 
            print(f"Found: ID={s['id']}, Name={s['name']}, Score1={s['score1']} , Score2={s['score2']} , Score3={s['score3']} , Overall={s['overall']}\n")
            return 
    
    print("Khong tim thay sinh vien co ten nay.\n")

# Hàm hiển thị tất cả điểm số
def display_all():
    print("\n______DANH SACH SINH VIEN______")
    if not students:
        print("chua co du lieu sinh vien.\n")
        return
    
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']},  Score1={s['score1']} , Score2={s['score2']} , Score3={s['score3']} , Overall={s['overall']} \n")
    print()


# ------------------------------
# MENU CHÍNH
# ------------------------------
def main():
    while True:
        print("____________CLASSROOM DATA MANAGER____________")
        print("1. Them sinh vien")
        print("2. Tim kiem bang MSV")
        print("3. Tim kiem bang Ho va Ten")
        print("4. Hien thi tat ca sinh vien")
        print("5. Exit")
        print("==============================================")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student_MSV()
        elif choice == "3" : 
            search_student_name()
        elif choice == "4":
            display_all()
        elif choice == "5":
            print("Dang thoat khoi chuong trinh...")
            break
        else:
            print(" Lua chon khong hop le , vui long chon lai.\n")

# Chạy chương trình
main()
