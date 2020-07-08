import random
a = 97 #a
b = 122 #z
def test(password):
    print(password[0] + password[4] + password[8] + password[12])
    print(password[1] + password[5] + password[9] + password[13])
    print(password[2] + password[6] + password[10] + password[14])
    print(password[3] + password[7] + password[11] + password[15])
    print(password[0] + password[1] + password[2] + password[3])
    print(password[4] + password[5] + password[6] + password[7])
    print(password[8] + password[9] + password[10] + password[11])
    print(password[12] + password[13] + password[14] + password[15])
    print(password[0] + password[5] + password[10] + password[15])
    print(password[3] + password[6] + password[9] + password[12])

def keygen():
    while True:
        key = []
        for i in range(0, 16):
            key.append(0)

        key[7] = random.randint(a, b)
        key[9] = random.randint(a, b)
        key[10] = random.randint(a, b)
        key[11] = random.randint(a, b)
        key[13] = random.randint(a, b)
        key[14] = random.randint(a, b)
        key[15] = random.randint(a, b)

        key[0] = -450 + key[7] + key[11] + key[13] + key[14] + key[15]
        key[1] = -450 + key[7] - key[9] + key[10] + key[11] + key[14] + (2 * key[15])
        key[2] = 900 - key[7] + key[9] - key[10] - key[11] - key[13] - (2 * key[14]) - (2 * key[15])
        key[3] = 450 - key[7] - key[11] - key[15]
        key[4] = -key[7] + key[9] + key[10]
        key[5] = 900 - key[7] - key[10] - key[11] - key[13] - key[14] - (2 * key[15])
        key[6] = -450 + key[7] - key[9] + key[11] + key[13] + key[14] + (2 * key[15])
        key[8] = 450 - key[9] - key[10] - key[11]
        key[12] = 450 - key[13] - key[14] - key[15]

        ex = False
        for k in key:
            if k > b or k <= a:
                ex = True
                break
        if ex:
            continue
        key = [chr(k) for k in key]
        password = "".join(key)

        return password
print(keygen())
