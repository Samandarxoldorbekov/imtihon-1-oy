def Canculator(number_first,number_second,amallar):
    lst = ["+","-","*","/"]
    if amallar == "+":
        print(number_first +number_second)
    if amallar == "-":
        print(number_first=number_second)
    if amallar == "*" or amallar == "x":
        print(number_first * number_second)
    if amallar == "/":
        print(number_first / number_second)
    if amallar not in lst:
        print("bunday amal mavjud emas axmoq /:")
    


number_1 = int(input("1-chi sondi kiriting:"))
amal = input("amalni bajaring(+|-|*|/): ")
number_2 = int(input("ikkinchi sindi kiriting: "))

Canculator(number_1,number_1,amal)