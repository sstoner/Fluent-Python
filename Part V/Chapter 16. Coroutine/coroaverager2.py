from collections import namedtuple

Result = namedtuple("Result","count average")

def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield    #yield相当于一个return，但是调用发还可以通过send激活运行yield后面的代码
        if term is None:
            break

        total += term
        count += 1
        average = total/count
    return Result(count,average)

coro_avg = average()
print(next(coro_avg))
print(coro_avg.send(123))
print(coro_avg.send(234))
print(coro_avg.send(None))