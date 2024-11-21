import subprocess
import sys
import io

def run_script(script_path, input_data=None):
    # Redirect stdout to capture print statements
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    # Run the script
    if input_data:
        sys.stdin = io.StringIO(input_data)
    with open(script_path, 'r', encoding='utf-8') as file:
        exec(file.read())
    
    # Get the output and reset stdout
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

def check_bai1():
    test_cases = [
        ("Hello123 World! Python\n", 
         "Nhập một chuỗi: Chuỗi có chứa ký tự viết hoa.\n"
         "Số lượng chữ số trong chuỗi: 3\n"
         "Chuỗi sau khi thay thế khoảng trắng: Hello123-World!-Python\n"
         "Các từ có độ dài lớn hơn hoặc bằng 7: ['Hello123']\n"),
        
        ("hello world\n", 
         "Nhập một chuỗi: Chuỗi không có ký tự viết hoa.\n"
         "Số lượng chữ số trong chuỗi: 0\n"
         "Chuỗi sau khi thay thế khoảng trắng: hello-world\n"
         "Các từ có độ dài lớn hơn hoặc bằng 7: []\n"),
        
        ("12345\n", 
         "Nhập một chuỗi: Chuỗi không có ký tự viết hoa.\n"
         "Số lượng chữ số trong chuỗi: 5\n"
         "Chuỗi sau khi thay thế khoảng trắng: 12345\n"
         "Các từ có độ dài lớn hơn hoặc bằng 7: []\n"),
        
        ("This is a test string with 1234567\n", 
         "Nhập một chuỗi: Chuỗi có chứa ký tự viết hoa.\n"
         "Số lượng chữ số trong chuỗi: 7\n"
         "Chuỗi sau khi thay thế khoảng trắng: This-is-a-test-string-with-1234567\n"
         "Các từ có độ dài lớn hơn hoặc bằng 7: ['1234567']\n"),
        
        ("AnotherTest123\n", 
         "Nhập một chuỗi: Chuỗi có chứa ký tự viết hoa.\n"
         "Số lượng chữ số trong chuỗi: 3\n"
         "Chuỗi sau khi thay thế khoảng trắng: AnotherTest123\n"
         "Các từ có độ dài lớn hơn hoặc bằng 7: ['AnotherTest123']\n")
    ]
    
    points_per_test = 0.8
    total_points = 0
    for input_data, expected_output in test_cases:
        output = run_script("Exam/Bai1.py", input_data)
        if output.strip() != expected_output.strip():
            print("Test Failed for input:", input_data)
            print("Your Output:")
            print(repr(output))
            print("Expected Output:")
            print(repr(expected_output))
        else:
            print(f"Test Passed for input: {input_data}")
            total_points += points_per_test
    return total_points

def check_bai2():
    test_cases = [
        ("0", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 0 đồng\n"),
        ("50", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 150000 đồng\n"),
        ("100", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 350000 đồng\n"),
        ("150", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 550000 đồng\n"),
        ("200", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 800000 đồng\n"),
        ("250", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 1050000 đồng\n"),
        ("300", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 1550000 đồng\n"),
        ("365", "Nhập vào số điện đã sử dụng: Số tiền điện phải trả là: 2200000 đồng\n"),
    ]
    
    points_per_test = 0.375
    total_points = 0
    for input_data, expected_output in test_cases:
        output = run_script("Exam/Bai2.py", input_data)
        if output.strip() != expected_output.strip():
            print("Test Failed for input:", input_data)
            print("Your Output:")
            print(repr(output))
            print("Expected Output:")
            print(repr(expected_output))
        else:
            print(f"Test Passed for input: {input_data}")
            total_points += points_per_test
    return total_points

def check_bai3():
    test_cases = [
        ("write\n", "Nhập động từ: Động từ sau khi thêm 'ing': writing\n"),
        ("make\n", "Nhập động từ: Động từ sau khi thêm 'ing': making\n"),
        ("lie\n", "Nhập động từ: Động từ sau khi thêm 'ing': lying\n"),
        ("die\n", "Nhập động từ: Động từ sau khi thêm 'ing': dying\n"),
        ("run\n", "Nhập động từ: Động từ sau khi thêm 'ing': running\n"),
        ("sit\n", "Nhập động từ: Động từ sau khi thêm 'ing': sitting\n"),
        ("play\n", "Nhập động từ: Động từ sau khi thêm 'ing': playing\n"),
        ("jump\n", "Nhập động từ: Động từ sau khi thêm 'ing': jumping\n"),
    ]
    
    points_per_test = 0.375
    total_points = 0
    for input_data, expected_output in test_cases:
        output = run_script("Exam/Bai3.py", input_data)
        if output.strip() != expected_output.strip():
            print("Test Failed for input:", input_data)
            print("Your Output:")
            print(repr(output))
            print("Expected Output:")
            print(repr(expected_output))
        else:
            print(f"Test Passed for input: {input_data}")
            total_points += points_per_test
    return total_points

def main():
    bai1_points = check_bai1()
    bai2_points = check_bai2()
    bai3_points = check_bai3()

    total_points = bai1_points + bai2_points + bai3_points
    print(f"Bài 1: {bai1_points}/4")
    print(f"Bài 2: {bai2_points}/3")
    print(f"Bài 3: {bai3_points}/3")
    print(f"Tổng điểm: {total_points}/10")

if __name__ == "__main__":
    main()