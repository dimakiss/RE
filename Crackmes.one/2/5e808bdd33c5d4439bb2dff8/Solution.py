import random

max_bits=32
ROR4 = lambda val, r_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

final=4140118835
current=0
string=""
rand=0
while True:

    current=ROR4(current, 13)
    if final-current<150 and final-current>20 and str.isprintable(chr(final - current)):
        print(string + chr(final - current))
    if string.__len__()>20:
        string=""
        current=0
    if rand==0:
        rand=1
        t = chr(random.randrange(ord('A'),ord('Z')+1))
    else:
        rand=0
        t = chr(random.randrange(ord('a'), ord('z')+1))

    current+=ord(t)
    string+=t
