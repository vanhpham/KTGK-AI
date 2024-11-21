# Bài 1: Xử lý chuỗi
# Hãy viết một chương trình Python thực hiện các yêu cầu sau:
# Nhập vào một chuỗi từ người dùng. Kiểm tra xem chuỗi này có bao gồm ký tự in hoa hay không.
# Đếm số lượng ký tự chữ cái và chữ số trong chuỗi đã nhập.
# Thay thế tất cả các ký tự khoảng trắng bằng dấu gạch dưới _.
# Trích xuất tất cả các từ có độ dài lớn hơn 3 từ chuỗi và in ra màn hình.
# VD: 
# Input:
# Nhập chuỗi: "Hello Python 123!"  
# Output:
# Chuỗi có chứa ký tự in hoa.  
# Số lượng chữ cái: 10  
# Số lượng chữ số: 3  
# Chuỗi sau khi thay thế khoảng trắng: Hello_Python_123!  
# Các từ có độ dài lớn hơn 3: ['Hello', 'Python', '123!'] 

# Bài 1: Xử lý chuỗi
# Nhập chuỗi từ người dùng
chuoi = input("Nhập vào một chuỗi: ")

# Kiểm tra chuỗi có ký tự in hoa hay không
co_in_hoa = False
for char in chuoi:
    if char.isupper():
        co_in_hoa = True
        break
print("Chuỗi có ký tự in hoa:", co_in_hoa)

# Đếm số lượng ký tự chữ cái và chữ số
so_chu_cai = 0
so_chu_so = 0
for char in chuoi:
    if char.isalpha():
        so_chu_cai += 1
    elif char.isdigit():
        so_chu_so += 1
print("Số ký tự chữ cái:", so_chu_cai)
print("Số ký tự chữ số:", so_chu_so)

# Thay thế khoảng trắng bằng dấu gạch dưới
# Thay thế khoảng trắng bằng dấu gạch dưới
chuoi_thay_the = chuoi.replace(" ", "_")
print("Chuỗi sau khi thay thế khoảng trắng:", chuoi_thay_the)

# Trích xuất các từ có độ dài lớn hơn 3
# Trích xuất các từ có độ dài lớn hơn 3
tu_dai_hon_3 = []
cac_tu = chuoi.split(" ")
for tu in cac_tu:
    if len(tu) > 3:
        tu_dai_hon_3.append(tu)
print("Các từ có độ dài lớn hơn 3:", tu_dai_hon_3)

