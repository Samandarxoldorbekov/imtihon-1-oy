def cheak_number(number):
    if number // 2 == 0:
        return True
    else:
        return False


a = cheak_number(int(input("son kiriting: ")))

if a == True:
    print("bu son juft")
else:
    print(" bu son toq")