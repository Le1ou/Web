def ThreeLists(initial_list):
    a = list()
    b = list()
    c = list()
    for i in initial_list:
        if(i%2==0):
            a.append(i)
        if(i%3==0):
            b.append(i)
        if(i%5==0):
            c.append(i)
    return [a, b, c]
initial_list = list(map(int,input('Введите значения через пробел: ').split()))
result = ThreeLists(initial_list)
print(result)