user_string=input("Name:")
output_string= ""
if len(user_string)>20:
    print("The length of your name should be less than 20 characters")
else:
    while True:
        if len(user_string)>19:
            break
        for i in range(25):
            if i >= 20 - len(user_string):
                break
            user_string += user_string[i]
    for i in range(len(user_string)):
        n1=ord(user_string[i])
        n2= (n1 * n1 >> 1) ^ (4 * i)
        while(n2 > 90):
            n2= n2 - 2 * i - 9
            if n2<=64 and n2>57:
                n2 = n2 - 2 * i - 10
        while n2<=47:
            n2+= 2 * i + 9
            if n2>57 and n2<=64:
                n2= n2 - 2 * i - 10
        hex(n2)
        output_string+=chr(n2)

    print(output_string)
