class Student:
    def __init__(self, name):
        self.name = name

    # args: argument
    # kwargs: keyword args
    def show(self, *args, **kwargs):
        x1 = args[0]
        print(x1)

        print(kwargs["x2"])

        print("Show method")
        print("args", args)
        print("kwargs", kwargs)

s1 = Student("Sok")
s1.show("a", "b", 1, 2, 3, x1="10", x2="20", x3="30")