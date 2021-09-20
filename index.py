num = 20

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "Mai Chai naja")
else:
    print(num, "Tuk Tong lawja")