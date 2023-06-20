import math

print('addition(1) subtraction(2) multiplication(3)  division(4)  sine(5)  cosine(6) tangent(7) pythagorean theorem(8)')
mode = input('What do mode do you want to calculate in: ')

if mode == '1':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2:"))
    output = num1 + num2
    print(f"Result: {output}")

elif mode == '2':

    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2:"))
    output = num1 - num2
    print(f"Result: {output}")

elif mode == '3':
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2:"))
    output = num1 * num2
    print(f"Result: {output}")

elif mode == '4':
    round_num = input("Do you want it to be rounded (y) (n): ")
    if round_num == 'y':
        num1 = int(input("Number 1:  "))
        num2 = int(input("Number 2: "))
        output = num1 / num2
        print(f"Result: {round(output)}")
    else:
        num1 = int(input("Number 1: "))
        num2 = int(input("Number 2: "))
        output = num1 / num2
        print(f"Result: {output}")
elif mode == '5':
    deg_rad = input("Calculation in degrees or radians (d) (r): ")
    if deg_rad == 'd':
        con_num = float(input("Sine number: "))
        sine_num = math.sin(math.radians(con_num))
        print(f'Result: {round(sine_num, 3)}')
    else:
        con_num = float(input("Sine number: "))
        sine_num = math.sin(con_num)
        print(f'Result: {round(sine_num, 3)}')

elif mode == '6':
    deg_rad = input("Calculation in degrees or radians (d) (r): ")
    if deg_rad == 'd':
        con_num = float(input("Cosine number: "))
        cos_num = math.cos(math.radians(con_num))
        print(f'Result: {round(cos_num, 3)}')
    else:
        con_num =float(input("Cosine number: "))
        cos_num = math.cos(con_num)
        print(f'Result: {round(cos_num, 3)}')
elif mode == '7':
    deg_rad = input("Calculation in degrees or radians (d) (r): ")
    if deg_rad == 'd':
        con_num = float(input("Tangent number: "))
        tan_num = math.tan(math.radians(con_num))
        print(f'Result: {round(tan_num, 3)}')
    else:
        con_num = float(input("Tangent number: "))
        tan_num = math.tan(con_num)
        print(f'Result: {round(tan_num, 3)}')

elif mode == '8':
    print("Skip prompt if value is unknown")
    a = input("Value of a: ")
    b = input("Value of b: ")
    c = input("Value of c: ")
    if a == '':
        squ_a = math.sqrt(float(b)**2 + float(c)**2)
        print(f"Value of a: {round(squ_a, 3)}")
    try:
        if b == '':
            squ_b = math.sqrt(float(a) ** 2 - float(c) ** 2)
            print(f"Value of c: {round(squ_b, 3)}")
    except ValueError:
        print('')
        print('###################################')
        print('')
        print('Value of c cannot be bigger than a')
        print('')
        print('###################################')
    try:
        if c == '':
            squ_c = math.sqrt(float(a) ** 2 - float(b) ** 2)
            print(f"Value of c: {round(squ_c, 3)}")

    except ValueError:
        print('')
        print('###################################')
        print('')
        print('Value of b cannot be bigger than a')
        print('')
        print('###################################')
else:
    print('I do not understand that')





