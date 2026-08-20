total = 0
while True:
    while True:    
        c = int (input("請輸入number(輸入999停止)："))
        if c == 999:
            break
        total += c
print("total：", total)    