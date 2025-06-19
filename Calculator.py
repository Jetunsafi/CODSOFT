def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

print("CALCULATOR:\n")
print("1. Addition")
print("2. Subtractoin")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice = input("\nEnter Your Choice:")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("\nEnter first no:"))
        num2 = float(input("Enter second no:"))

        if choice == '1':
            print("\nADDITION:", num1, "+", num2, "=", add(num1,num2))

        elif choice == '2':
            print("\nSUBTRACTION:", num1, "-", num2, "=", sub(num1,num2))

        elif choice == '3':
            print("MULTIPLICATION:", num1, "*", num2, "=", mul(num1,num2))

        elif choice == '4':
            print("DIVISION:", num1, "/", num2, "=", div(num1,num2))
       
    if choice == '5':
            break
