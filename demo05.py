def showinfore():
    print("My name is Skylar")
    print("My major is AITA")


def fun1(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()


def fun2(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end="")
        print()


def fun3(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res


def fun4(n):
    return n * 9 / 5 + 32


def showmenu():
    print("1. show information")
    print("2. print *")
    print("3. calculate 5!")
    print("4. C to F")
    print("5. exit")


if __name__ == "__main__":
    fun2(5)
    showinfore()
    fun1(5)

    x = fun3(5)
    print("5! =", x)

    c = float(input("請輸入攝氏溫度："))
    f = fun4(c)
    print(f"{c}°C = {f}°F")