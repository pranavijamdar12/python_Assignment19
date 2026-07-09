Compare = lambda no: (no >= 70) and (no <= 90)
Increase = lambda no: no + 10
Product = lambda no1, no2: no1 * no2

def filterx(task, element):
    result = []
    for no in element:
        if task(no):
            result.append(no)
    return result

def mapx(task, element):
    result = []
    for no in element:
        result.append(task(no))
    return result

def reducex(task, element):
    mul = 1
    for no in element:
        mul = task(mul, no)
    return mul

Data = [50, 75, 80, 95, 85]

FData = filterx(Compare, Data)
print("Filtered:", FData)

MData = mapx(Increase, FData)
print("Mapped:", MData)

RData = reducex(Product, MData)
print("Product:", RData)
