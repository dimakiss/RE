
# checks if there repeating character
def different_char(string):
    d=[]
    for i,char in enumerate(string):
        if char in d:
            return False
        d.append(char)
    return True
    
# returns the serial for the name
def find_serial(name):
    d=[]
    for i,char in enumerate(name):
        if char in d:
            print("bad input all the chars mast be different")
            return None
        d.append(i)


    serial=""
    v7=ord(name[0])
    v8 = (v7 & 1) + 5
    v53 = ((v7 >> 1) & 1) + 5
    v55 = ((v7 >> 2) & 1) + 5
    v57 = ((v7 >> 3) & 1) + 5
    v59 = ((v7 >> 4) & 1) + 5

    v9 = ord(name[1])
    v45 = (v9 & 1) + 1
    v47 = ((v9 >> 1) & 1) + 1
    v10 = ((v9 >> 2) & 1) + 1
    v49 = ((v9 >> 3) & 1) + 1
    v51 = ((v9 >> 4) & 1) + 1

    v11=str(v8+v10)
    serial+=v11
    v14=str(v57+v49)
    serial+=v14
    v17=str(v53+v51)
    serial+=v17
    v20=str(v55 + v45)
    serial+=v20
    v23=str(v59 + v47)
    serial+=v23
    serial+='-'
    v26=ord(name[2])
    v27 = (v26 & 1) + 5
    v54 = ((v26 >> 1) & 1) + 5
    v56 = ((v26 >> 2) & 1) + 5
    v58 = ((v26 >> 3) & 1) + 5
    v60 = ((v26 >> 4) & 1) + 5

    v28 = ord(name[3])
    v46 = (v28 & 1) + 1
    v48 = ((v28 >> 1) & 1) + 1
    v29 = ((v28 >> 2) & 1) + 1
    v50 = ((v28 >> 3) & 1) + 1
    v52 = ((v28 >> 4) & 1) + 1
    v30=str(v27 + v29)
    serial+=v30
    v33=str(v58 + v50)
    serial+=v33
    v36=str(v54 + v52)
    serial+=v36
    v39=str(v56 + v46)
    serial+=v39
    v42=str(v60 + v48)
    serial+=v42
    return serial
    
# returns the name for serial
def find_str(serial):
    lst_1=[]
    name2 = ""

    for a in range(ord('a'),ord('z')+1):
        for b in range(ord('a'),ord('z')+1):
            for c in range(ord('a'),ord('z')+1):
                for d in range(ord('a'),ord('z')+1):
                    v7 = a
                    v8 = (v7 & 1) + 5
                    v53 = ((v7 >> 1) & 1) + 5
                    v55 = ((v7 >> 2) & 1) + 5
                    v57 = ((v7 >> 3) & 1) + 5
                    v59 = ((v7 >> 4) & 1) + 5

                    v9 = b
                    v45 = (v9 & 1) + 1
                    v47 = ((v9 >> 1) & 1) + 1
                    v10 = ((v9 >> 2) & 1) + 1
                    v49 = ((v9 >> 3) & 1) + 1
                    v51 = ((v9 >> 4) & 1) + 1
                    if  str(v8 + v10) == serial[0] and str(v57 + v49) ==serial[1] and str(v53 + v51) == serial[2] and str(v55 + v45) == serial[3] and str(v59 + v47) == serial[4]:
                        v26 = c
                        v27 = (v26 & 1) + 5
                        v54 = ((v26 >> 1) & 1) + 5
                        v56 = ((v26 >> 2) & 1) + 5
                        v58 = ((v26 >> 3) & 1) + 5
                        v60 = ((v26 >> 4) & 1) + 5

                        v28 = d
                        v46 = (v28 & 1) + 1
                        v48 = ((v28 >> 1) & 1) + 1
                        v29 = ((v28 >> 2) & 1) + 1
                        v50 = ((v28 >> 3) & 1) + 1
                        v52 = ((v28 >> 4) & 1) + 1
                        if  str(v27 + v29) == serial[6] and str(v58 + v50) == serial[7] and str(v54 + v52) == serial[8] and str(v56 + v46) == serial[9] and str(v60 + v48) == serial[10]:
                            temp_str=str(chr(a))+str(chr(b)) +str(chr(c)) +str(chr(d))
                            #print(temp_str)
                            if temp_str[-1]=="p" and different_char(temp_str):
                                return temp_str
    return name2

if __name__ == '__main__':
        print(find_str("76876-77776"))
