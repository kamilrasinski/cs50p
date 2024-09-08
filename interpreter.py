def main ():

    expression = input("Let's do the math: ").strip().split(" ")
    x = int(expression[0])
    y = str(expression[1])
    z = int(expression[2])

    if y == "+":
        print (float(x + z))

    elif y == "-":
        print (float(x - z))

    elif y == "*":
        print (float(x * z))

    elif y == "/" and z != 0:
        print (float(x / z))

    else:
        print("wrong input")

main()
