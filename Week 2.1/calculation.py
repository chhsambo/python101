def calculation(x, y, op):
    result = None
    if op == "1":
        result = x + y
    elif op == "2":
        result = x - y
    elif op == "3":
        result = x * y
    elif op == "4":
        result = x / y
    else:
        print(">> Unrecoginize operation!")
    
    return result


print("Calculation")
print("===========")

print("Enter number below:")
x = input("- X: ")
y = input("- Y: ")

if x == "":
    print(">> Unknow X")
if y == "":
    print(">> Unknow Y")

if x and y:
    x = float(x)
    y = float(y)

    print("""
        1. Sum
        2. Minus
        3. Multiply
        4. Divide
        """)
    op = input("Choose what you want to do: ")

    result = calculation(x, y, op)

    if result:
        print(f"Result: {result}")
