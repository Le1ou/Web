def Newton(num, rootDegree):
    eps = 0.00001
    root = num / rootDegree
    rn = num
    while(abs(root - rn) >= eps):
        rn = num
        i = 1
        while(i < rootDegree):
            rn = rn / root
            i = i + 1
        root = 0.5 * ( rn + root)
    return root
num = float(input("Число, корень которого считаем: "))
rootDegree = int(input("Корень степени n: "))
result = Newton(num, rootDegree)
print(result)