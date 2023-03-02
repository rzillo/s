big_num = 0
small_num = 0
l1 = []
i = 0

while i < 5:
    x = int(input("type a number: "))
    if i == 0:
        big_num = x
        small_num = x
        l1.append(x)
        i += 1
    else:
        if x > big_num:
            l1.append(x)
            big_num = x
            i += 1
        elif x < small_num:
            l1.insert(0, x)
            small_num = x
            i += 1
        else:
            for k in range(len(l1)):
                if x <= l1[k]:
                    l1.insert(k, x)
                    i += 1
                    break

print(l1)
