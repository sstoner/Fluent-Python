from collections import namedtuple

Result = namedtuple("Result","count average")

#子生成器
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count,average)

#委派生成器
def grouper(results,key):
    while True:
        results[key] = yield from average()

#客户端代码，调用方
def main(data):
    results = {}
    for key,values in data.items():
        group = grouper(results,key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)

#输出报告
def report(results):
    for key,result in sorted(results.items()):
        group,unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count,group,result.average,unit))

data = {
    "girls;kg":
        [43,43,53,34,56,75,43,65,10,122],
    "girls;m":
        [1.4,1.6,1.6,1.6,1.6,1.6,1.6,1.7,1.8,1.9],
    "boys;kg":
        [12,34,45,67,56,42,56,23,15,65],
    "boys;m":
        [1.2,2.4,2.4,5.2,5.6,1.5,1.6,1.7,1.7,1.9]
}


if __name__ == '__main__':
    main(data)
