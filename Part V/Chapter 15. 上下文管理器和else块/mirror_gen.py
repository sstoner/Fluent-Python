import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:    #以防with时报错，抛出时，stdout不被执行
        yield "Vance Lee used by WITH"
    except ZeroDivisionError:
        msg = "Please DO NOT divide by zero"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

with looking_glass() as f:
    print("hello")
    print(f)



