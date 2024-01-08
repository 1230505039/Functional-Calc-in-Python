print('''
	[1]  Addition/Subtraction/Multiplying/Division
	[2]  Exponentiation
	[3]  Mod
	[4]  Percentage
	[5]  Root
	[6]  Factorial
        [7]  Finding roots of any equation
        [8]  Finding sum of any geometric shapes angle
        [9]  Taking Derivative
        [10] Logarithm
        [11] Is It Triangle?
        [12] Finding any equation's derivative's equation
   	[Q]  Exit
''')

def addsubmuldiv():
    print("Example: 2+2-((7*5)/(2))")
    try:
        result = eval(input("Type Your operation: "))
        print(result)

    except ZeroDivisionError:
        print("You can't divide any number by zero!")
    except SyntaxError:
        print("You typed wrong!")

def exponention():
    x = input('Base Number: ')
    x = float(x)
    y = input('Top Number: ')
    y = float(y)

    if x == 0 and y == 0:
        print("It's undefined.")
    else:
        print('Equals:', x ** y)

def mod():
    x = input('First Number: ')
    x = float(x)
    y = input('Second Number: ')
    y = float(y)

    try:
        print('Equals:', x % y)
    except ZeroDivisionError:
        print("Any number can't divide by zero.")

def percentage():
    x = float(input('Number: '))
    y = float(input('Percentage: '))
    print('Equals: ', x * y / 100)

def root():
    x = float(input('Number: '))
    y = float(input('Power of the root: '))

    if x < 0:

        if y >= 2:

            if y % 2 == 0:
                print(str((-1 * x) ** y ** -1) + 'i')

            else:
                print('Equals:', round((-1 * (-1 * x) ** (y ** -1))))

        else:
            print('The power of the root must be greater than 2 or equals.')

    elif y >= 2:

        print('Equals: ', round(x ** y ** -1))

    else:
        print('The power of the root must be greater than 2 or equals.')

def factorial():
    x = int(input('Number: '))
    fact = 1
    for a in range(1, x + 1):
        fact = fact * a
    print('Equals: ', fact)

def findingrootsofanyequation():
    a = float(input("Head Number: "))
    b = float(input("Second Number: ")) 
    c = float(input("Fixed Number: "))

    D = b ** 2 - (4 * a * c)

    if D < 0:
        print("There is no real root.")

        print("x1= ", str((-1 * b + (-1 * D) ** 0.5) / (2 * a)) + 'i')
        print("x2= ", str((-1 * b - (-1 * D) ** 0.5) / (2 * a)) + 'i')

    else:

        x1 = (-1 * b + D ** 0.5) / (2 * a)
        x2 = (-1 * b - D ** 0.5) / (2 * a)

        print("x1 =", x1, "x2 =", x2, end="")

def findinganglesofanyshapes():
    n = float(input("Number of edges: "))

    if n != int(n):
        print("Number of the edges has to be integer number!")

    elif n <= 2:
        print("Number of the edges have to be larger than 2!")

    else:
        print((n - 2) * 180)

def takingderivative():
    a = float(input("First Number: "))
    b = float(input("Second Number: "))
    c = float(input("Fixed Number: "))


    if b < 0:
        print(str(2*a) + "x", "-", str(-1*b))

    else:
        print(str(2 * a) + "x", "+", str(b))

def logarithm():
    from math import log
    x = float(input("Top number: "))
    base = float(input("Base number: "))

    if x <= 0 or base < 0:
        print("The top number and base number have to be greater than 0!")

    else:
        try:
            result = log(x, base)
            a = bool()
            x = 3 ** a
            if round((x)**(1/3)) >= 1 and x%10 == 0 and base %10 == 0 and round(result) >= 3:
                print(round(result))

            elif round(result) > 4 and base == 3 and a == int() :
                print(round(result))

            else:
                print(result)
        except ValueError:
            print("Base number can't be 0!")
        except ZeroDivisionError:
            print("Base number can't be 1!")

def isittriangle():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a < 0 or b < 0 or c < 0:
        print("The edge of the triangle has to be a positive number!")
        input("Press 'enter'!")
        isittriangle()

    elif abs(a-b) < c < a+b:
        print("It is a triangle!")

    else:
        print("It is not a triangle!")

def derivativeequation():
    a = 3;
    b = float(input("Enter the point: "))

    number_list = list()

    i = a
    c = i

    while i != 0:
        indice = abs(a - i + 1)
        number = float(input("Enter the {}. elemen: ".format(indice)))
        number_list.append(number)
        i -= 1

    y_point = 0

    for i in number_list:
        y_point = y_point + (i * pow(b, a - 1))
        a -= 1

    slope = 0

    for i in number_list:
        i = i * (c - 1)
        c -= 1
        i = i * (pow(b, c - 1))
        slope += i

    n = y_point - (slope * b)

    if n == 0:
        print(str(slope) + "x")
    elif slope == 0:
        print(str(n))
    else:
        print(str(slope) + " x "+ "+ " + str(n))

def again():
    input('You entered wrong. Press enter to get back to the main menu.')

while True:
    enter = input('Selection: ')

    if enter == "q" or enter == "Q":
        print("Quitting!")
        quit()
    else:
        if enter == "1":
            addsubmuldiv()
        elif enter == "2":
            exponention()
        elif enter == "3":
            mod()
        elif enter == "4":
            percentage()
        elif enter == "5":
            root()
        elif enter == "6":
            factorial()
        elif enter == "7":
            findingrootsofanyequation()
        elif enter == "8":
            findinganglesofanyshapes()
        elif enter == "9":
            takingderivative()
        elif enter == "10":
            logarithm()
        elif enter == "11":
            isittriangle()
        elif enter == "12":
            derivativeequation()
        else:
            again()






