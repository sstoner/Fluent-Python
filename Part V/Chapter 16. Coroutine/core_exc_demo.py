class DemoException(Exception):
    pass

def demo_exc_handing():
    print("- > coroutine started ")
    while True:
        try:
            x = yield
        except DemoException:
            print("**** DemoException handled. Coroutine...")
        else:
            print("- > coroutine reveived: {!r}".format(x))
    raise RuntimeError("This line should never run.")

exc_coro = demo_exc_handing()
next(exc_coro) #yield 向前执行
exc_coro.send(12)  #给协程发送信息
exc_coro.send(34)
exc_coro.send('reqwr')
#exc_coro.throw(DemoException)
exc_coro.throw(ZeroDivisionError)
exc_coro.send(13)

"""
如果协程无法处理传入的异常，就会终止程序
因此最好把 协程定义体放入try/finally块中
"""