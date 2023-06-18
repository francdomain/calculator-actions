def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

if __name__ == "__main__":

    n1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    n2 = float(input("Enter second number: "))

    if op == '+':
        print(add(n1, n2))
    elif op == '-':
        print(sub(n1, n2))
    elif op == '*':
        print(mul(n1, n2))
    elif op == '/':
        print(div(n1, n2))
    else:
        print("You have not entered the right operation")



