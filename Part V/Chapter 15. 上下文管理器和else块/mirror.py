class LookingGlass:

    def __enter__(self):
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "Vance Lee"

    def reverse_write(self,text):
        self.origin_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.origin_write
        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return True

monster = LookingGlass()

print(monster.__enter__())
print(monster.__exit__(None,None,None))
