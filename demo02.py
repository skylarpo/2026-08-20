# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i * j:5d}", end=" ")
#     print() # Print a newline after each row of the multiplication table


# i = 1
# while i <10:
#     j = 1
#     while j < 10:
#         print(f"{i * j:5d}", end=" ")
#         j +=1
#     print()
#     i += 1


# n, m = map(int, input("enter two numbers (n m): ").split())
# i = 1
# while i <= n:
#     j = 1
#     while j <= m:
#         if i * j >= 50:
#               j+=1
#               continue
#         else:
#               print(f"{i * j:5d}", end=" ")
#         j += 1
#     print()
#     i += 1
    

n, m, k = map(int, input("enter three numbers (n m k): ").split())
for i in range(n, m):
    for j in range(n, m):
        if i * j >= k:
             j+=1
             continue
        else:
             print(f"{i * j:5d}", end=" ")
        j += 1
    print()
    i += 1