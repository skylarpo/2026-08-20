lst = [1, 2, 3, 4, 5]

"""
讓使用者輸入溫度 直到輸入999停止（不含999），將輸入的溫度存入list中，最後印出list中所有溫的平均值
"""

c = int(input("請輸入數字（輸入999停止）："))
total = 0
while c != 999 :
    if c % 2 == 0:
        total += c
    c = int(input("請輸入數字（輸入999停止）："))
print("平均數字為：", total )