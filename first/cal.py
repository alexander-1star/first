def cal():
    try:
     a = float(input('Enter the first number: '))
     b = float(input('Enter the second number: '))


    print("what do you want to do:")
    print("Addition is (+)")
    print(" Subtraction is (-)")
    print(" Multiplykation is (*)")
    print(" Division is  (/)")

    times = input("Type the symbol you need: ")

    if times in ['1', '+']:
        result = a + b
        operation = '+'
    elif times in ['2', '-']:
        result = a - b
        operation = '-'
    elif times in ['3', '*']:
        result = a * b
        operation = '*'
    elif times in ['4', '/']:
        if b == 0:
            print("Its impossoble.")
            return
        result = a / b
        operation = '/'
    else:
        print("Invalid operation.")
        return

    print(f"\n{a} {operation} {b} = {result}")

cal()