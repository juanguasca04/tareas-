def num_mayor():

    num1=int(input("ingrese el primer numero"))
    num2=int(input("ingrese el segundo numero"))
    num3=int(input("ingrese el tercer numero"))

    if num1 > num2 and num1 > num3:
        print("el num mayor es",num1)
    elif num2 > num1 and num2 > num3:
        print("el num mayor es",num2)
    elif num3 > num1 and num3 > num2:
        print("el num mayor es",num3)
    else:
        print("error")
num_mayor()
