# 根据示例代码 改为五日均线。。
def averager():

    total = [0,0,0,0,0]
    count = 5
    average = None

    while True:
        term = yield average
        total.append(term)
        total.pop(0)
        #count += 1
        average = sum(total)/count


ave = averager()
next(ave) #向前执行代码（yield之前）
print(ave.send(123))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(456))
print(ave.send(4561))