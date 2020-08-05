import random

def generate_password():
    s_1=""
    for i in range(6):
        s_1+=str(random.randrange(2,10))

    temp=random.randrange(76,91)
    s_1+=str(chr(temp))+str(chr((256-temp)//2))+str(chr(256-(256-temp)//2-temp))
    s_1+='@'

    for i in range(6):
            s_1+=chr(3*random.randrange(ord('B')//3,ord('Z')//3))
    return s_1
if __name__ == '__main__':
    print(generate_password())
