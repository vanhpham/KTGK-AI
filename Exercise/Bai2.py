# Bài 2: Xử lý danh sách
# Viết một chương trình thực hiện các yêu cầu sau:
# Nhập vào một danh sách số nguyên từ người dùng (tối thiểu 5 số).
# Tìm và in ra số lớn nhất và số nhỏ nhất trong danh sách.
# Sắp xếp danh sách theo thứ tự giảm dần và in ra.
# Loại bỏ các phần tử trùng lặp và in ra danh sách kết quả.
# Tính tổng của tất cả các số chia hết cho 3 trong danh sách.
# VD:
# Input:
# Nhập danh sách các số nguyên (cách nhau bằng dấu cách): 5 12 7 12 3  

# Output:
# Số lớn nhất: 12  
# Số nhỏ nhất: 3  
# Danh sách sắp xếp giảm dần: [12, 12, 7, 5, 3]  
# Danh sách sau khi loại bỏ phần tử trùng lặp: [12, 7, 5, 3]  
# Tổng các số chia hết cho 3: 15 


# Nhập danh sách số nguyên từ người dùng
#C1:
danh_sach = list(map(int, input("Nhập danh sách số nguyên (ít nhất 5 số, cách nhau bởi khoảng trắng): ").split()))

#C2:
# danh_sach = []
# input_str = input("Nhập danh sách số nguyên (ít nhất 5 số, cách nhau bởi khoảng trắng): ")
# input_list = input_str.split()

# for item in input_list:
#     danh_sach.append(int(item))

# Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(danh_sach)
so_nho_nhat = min(danh_sach)
print("Số lớn nhất:", so_lon_nhat)
print("Số nhỏ nhất:", so_nho_nhat)

# Sắp xếp danh sách theo thứ tự giảm dần
danh_sach_giam_dan = sorted(danh_sach, reverse=True)
print("Danh sách giảm dần:", danh_sach_giam_dan)

# Loại bỏ các phần tử trùng lặp
danh_sach_khong_trung = list(set(danh_sach))
print("Danh sách sau khi loại bỏ trùng lặp:", danh_sach_khong_trung)

# Tính tổng các số chia hết cho 3
tong_chia_het_cho_3 = 0
for x in danh_sach:
    if x % 3 == 0:
        tong_chia_het_cho_3 += x
print("Tổng các số chia hết cho 3:", tong_chia_het_cho_3)
