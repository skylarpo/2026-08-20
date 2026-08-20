import demo05




# def main():
#     student = {"name": "張三", "Id": "D12345", "chinese": "60", "math": "70", "english": "80"}
#     students = [
#         {"name": "張三", "Id": "D12345", "chinese": "60", "math": "70", "english": "80"},
#         {"name": "李四", "Id": "D12346", "chinese": "70", "math": "80", "english": "90"},
#         {"name": "王五", "Id": "D12347", "chinese": "80", "math": "90", "english": "100"}
#     ]
#     print(students[0]["name"])
#     print(students[0]["Id"])
#     print(students[0]["chinese"])
#     print(students[0]["math"])
#     print(students[0]["english"])
#     print(students[1]["name"])

if __name__ == "__main__":
    # main()
    while True:
        demo05.showmenu()
        choice = input("請輸入選項(1~5)：")
        if choice == "1":
            demo05.showinfore()
        elif choice == "2":
            n = int(input("請輸入數字："))
            demo05.fun1(n)
        elif choice == "3":
            x = demo05.fun3(5)
            print("5! =", x)
        elif choice == "4":
            c = float(input("請輸入攝氏溫度："))
            f = demo05.fun4(c)
            print(f"{c}°C = {f}°F")
        elif choice == "5":
            print("程式結束")
            break

   