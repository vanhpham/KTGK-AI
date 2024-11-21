# Bài 3: Làm việc với từ điển
# Hãy viết một chương trình xử lý dữ liệu sinh viên dựa trên từ điển:
# Tạo một từ điển chứa thông tin của 3 sinh viên, với mỗi sinh viên gồm các trường: Họ tên, MSSV, và Điểm trung bình.
# In thông tin của sinh viên có điểm trung bình cao nhất.
# Thêm một sinh viên mới vào từ điển từ dữ liệu người dùng nhập vào.
# Kiểm tra xem trong từ điển có sinh viên nào có điểm trung bình dưới 5 không, nếu có hãy in danh sách các sinh viên này.
# Tính điểm trung bình chung của tất cả các sinh viên trong từ điển.
# VD: 
# Input:
# # Từ điển ban đầu  
# students = {  
#     101: {"Họ Tên": "Vũ Việt A", "MSSV": 101, "Điểm Trung Bình": 8.5},  
#     102: {"Họ Tên": "Đinh Tùng B", "MSSV": 102, "Điểm Trung Bình": 9.0},  
#     103: {"Họ Tên": "Đặng Tùng C", "MSSV": 103, "Điểm Trung Bình": 4.0},  
# }  

# # Nhập sinh viên mới:  
# Họ tên: Trịnh Văn D  
# MSSV: 104  
# Điểm trung bình: 5.5  

# Output:
# Sinh viên có điểm trung bình cao nhất:  
# {'Họ Tên': 'Đinh Tùng B', 'MSSV': 102, 'Điểm Trung Bình': 9.0}  

# Danh sách sinh viên có điểm trung bình dưới 5:  
# {'Họ Tên': 'Đặng Tùng C', 'MSSV': 103, 'Điểm Trung Bình': 4.0}  

# Điểm trung bình chung của tất cả sinh viên: 6.75
# Tạo từ điển chứa thông tin sinh viên
sinh_vien = {
    101: {"Họ Tên": "Vũ Việt A", "MSSV": 101, "Điểm trung bình": 8.5},  
    102: {"Họ Tên": "Đinh Tùng B", "MSSV": 102, "Điểm trung bình": 9.0},  
    103: {"Họ Tên": "Đặng Tùng C", "MSSV": 103, "Điểm trung bình": 4.0},
}
# Tìm sinh viên có điểm trung bình cao nhất
sinh_vien_max = None
diem_tb_max = -1
for sv in sinh_vien.values():
    if sv["Điểm trung bình"] > diem_tb_max:
        sinh_vien_max = sv
        diem_tb_max = sv["Điểm trung bình"]
print("Sinh viên có điểm trung bình cao nhất:", sinh_vien_max)

# Thêm một sinh viên mới
ho_ten = input("Nhập họ tên sinh viên mới: ")
mssv = input("Nhập MSSV sinh viên mới: ")
diem_tb = float(input("Nhập điểm trung bình sinh viên mới: "))
sinh_vien[len(sinh_vien) + 1] = {"Họ tên": ho_ten, "MSSV": mssv, "Điểm trung bình": diem_tb}

# Kiểm tra sinh viên có điểm trung bình dưới 5
sinh_vien_duoi_5 = []
for sv in sinh_vien.values():
    if sv["Điểm trung bình"] < 5:
        sinh_vien_duoi_5.append(sv)
print("Danh sách sinh viên có điểm trung bình dưới 5:", sinh_vien_duoi_5)

# Tính điểm trung bình chung
tong_diem = 0
so_luong_sv = len(sinh_vien)
for sv in sinh_vien.values():
    tong_diem += sv["Điểm trung bình"]
diem_trung_binh_chung = tong_diem / so_luong_sv
print("Điểm trung bình chung:", round(diem_trung_binh_chung, 2))