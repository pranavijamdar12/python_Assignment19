
def CheckPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False
    return True

Multiply = lambda no: no * 2

Maximum = lambda no1, no2: no1 if no1 > no2 else no2

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
    maximum = element[0]
    for no in element[1:]:
        maximum = task(maximum, no)
    return maximum

Data = [10, 11, 12, 13, 14, 15, 17, 19]

FData = filterx(CheckPrime, Data)
print("Prime Numbers:", FData)

MData = mapx(Multiply, FData)
print("After Multiply by 2:", MData)

RData = reducex(Maximum, MData)
print("Maximum:", RData)
