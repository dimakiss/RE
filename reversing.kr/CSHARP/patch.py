def create_patch(name):
    with open(str(name),'rb') as f:
        buff=f.read()
    f.close()
    base=0x538
    b=54
    with open("CSharp_patched.exe",'w+b') as f:
        f.write(buff)
        f.close()
    d={18 : b - 38,35:b - 3,52:(b ^ 39),69:b - 21,87:71 - b,124:(b ^ 114),141:(b ^ 80),159: 235 - b,179:106 + b,200 :238,220:b - 3}

    with open('CSharp_patched.exe', 'r+b') as fh:
        for i in range(0xea):
            fh.seek(base+i)
            if buff[i+base]+1==256:
                byte_arr = [0]
            else:
                byte_arr = [buff[i+base]+1]
            if i in d:
                byte_arr=[d[i]]
            binary_format = bytearray(byte_arr)
            fh.write(binary_format)

    fh.close()

if __name__ == '__main__':
    try:
        create_patch(sys.argv[1])
        print('CSharp_patched was created')
    except:
        print('Error occured')
