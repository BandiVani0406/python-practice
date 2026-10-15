a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operation")