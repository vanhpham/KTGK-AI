import pandas as pd

# Đọc nội dung từ tệp CSV
df = pd.read_csv("Exercise/students.csv")
print("Bảng dữ liệu từ tệp CSV:")
print(df)

# Thêm cột Điểm Trung Bình
df["Điểm Trung Bình"] = df[["Điểm ĐS", "Điểm GT1", "Điểm GT2"]].mean(axis=1)
print("\nBảng dữ liệu sau khi thêm cột Điểm Trung Bình:")
print(df)

# Lọc sinh viên có điểm trung bình >= 7
passed_students = df[df["Điểm Trung Bình"] >= 7]
passed_students.to_csv("passed_students.csv", index=False)
print("\nDanh sách sinh viên có điểm trung bình >= 7:")
print(passed_students)

# Tính điểm trung bình môn Đại Số
diem_tb_ds = df["Điểm ĐS"].mean()
print("\nĐiểm trung bình môn Đại Số của tất cả sinh viên:", round(diem_tb_ds, 2))
