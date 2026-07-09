CheckEven = lambda no: no % 2 == 0
Square = lambda no: no * no
Addition = lambda no1, no2: no1 + no2

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
    total = 0
    for no in element:
        total = task(total, no)
    return total

Data = [10, 15, 20, 25, 30, 35, 40]

FData = filterx(CheckEven, Data)
print("Filtered:", FData)

MData = mapx(Square, FData)
print("Mapped:", MData)

RData = reducex(Addition, MData)
print("Sum:", RData)
