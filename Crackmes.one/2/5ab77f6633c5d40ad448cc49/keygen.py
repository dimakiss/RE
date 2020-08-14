
user_string=input("Name:")
output_string= ""
for i in range(user_string.__len__()):
    n1=ord(user_string[i])
    n2= (i >> 2) + (2 * n1 >> 2) + 56
    output_string+=chr(n2)

print(output_string)
