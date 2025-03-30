#Листинг 1.1
def proc_dec2bin():
    while True:
        dec = int(input('Введите десятичное число - '))
        tmp = dec;b2 = "";q = 2
        while tmp > 0:
            b2 += str(tmp % 2)
            tmp //= 2
        b2 = "0" if b2 == "" else b2[::-1]
        print("dec =",dec,"\nbin =", b2)
        if input("Press 1 + Enter for continue:")!= "1":
            exit()
proc_dec2bin()
#Листинг 1.2
def funct_dec2bin(tmp):
    b2 = ""
    while tmp > 0:
        b2 += str(tmp % 2)
        tmp //= 2
    b2 = "0" if b2 == "" else b2[::-1]
    return b2
dec = int(input("Введите десятичное число - "))
b = funct_dec2bin(dec)
print("dec =",dec,"\nbin-",b)
#dec_to_bq_ver1
title =  '''
Задача: перевод а10 --> bq
где
b - 'число (строковая переменная) в q-ой сист/сч,
q -  число в пределах 2<= q <= 10 - основание сист/ сч,
'''
def dec_2_bq(tmp, q):
    bq = ""
    while tmp > 0:
        bq = str (tmp % q) +bq
        tmp = tmp// q
    return bq
print(title)
dec = int (input ("Введите десятичное число - а= ?"))
flag = True
while flag:
    q = int (input ("Введите 2 <= q <= 10   q = ?"))
    if 2<= q and q <= 10: flag = False
    else:
        print ("Повторите ввод q")
bq = dec_2_bq(dec,q)

if bq == "" : bq = "0"
print("a10 = ",dec, "\nbq("+str(q)+")=",bq)
#dec_to_bq_ver2
def proc_start():
    title = '''
    Задача: перевод a10 --> bq
    где
    b - 'число'(строковая переменная) в q-ой сист/сч,
    q - число в пределах 2<= q <= 10 - основание сист/сч.
    '''
    def dec_2_bq(tmp,q):
        bq = ""
        print("dec | q | mod")
        print("-"*13)
        while tmp > 0 :
            bin = tmp % q
            bq = str(bin)+bq
            print("{:3} % {:1} = {:1}".format(tmp,q,bin))
            tmp = tmp//q
        return bq
    print(title)
    dec = int(input("Введите десятичное число - а=?"))
    flag = True
    while flag:
        q = int(input("Введите 2<= q <= 10    q =?"))
        if 2<= q and q <= 10: flag = False
        else:
            print("Повторите ввод q")
    bq = dec_2_bq(dec,q)
    if bq == "": bq = "0"
    print("a10 = ",dec, "\nbq("+str(q)+")=",bq)
proc_start()
#Листинг 1.3
promt = '''\n
Школьный алгоритм по схеме "табличка"
1022 |2
----------
0 |511 | 2
------------(tire = 10)
0 |255 | 2 ......

О - индекс параметра
3 - кол-во знакомест числа.
.......................
'''
import math
dec = 123
q = 2
bq = ""
len_bq = int(math.log(dec, q)) +1
sp = len(str(dec))
tire = sp+1+3
print("dec =" ,dec, "q = ", q)
print("{0:4}|{1:1}".format(dec,q))
print("-" * tire)
for p in range(len_bq):
    bp = str(dec % q)
    bq = bp  + bq
    dec = dec // q
    str_frm = " " * sp + "{0:1} | {1:3} | {2:1}"
    print(str_frm.format(bp, dec , q))
    print(" " * tire)
print("bq =" , bq)
#Самостоятельная dec_to_bq_ver3
prompt = '''\n
Школьный алгоритм по схеме "табличка"

1022 |2
----------
0 |511 | 2
------------(tire = 10)
0 |255 | 2 ......

0 - индекс параметра
3 - кол-во знакомест числа.
.....................
'''
import math
dec = 21
q = 2
bq = ""
len_bq = int(math.log(dec, q)) +1
sp = len(str(dec))
tire = 10
print("dec =" ,dec, "q = ", q)
print("{0:3}|{1:1}".format(dec,q))
print("-" * tire)
for p in range(len_bq):
    bp = str(dec % q)
    bq = bp  + bq
    dec = dec // q
    str_frm = " " * int(p*sp+2) + "{0:1} | {1:3} | {2:1}"
    print(str_frm.format(bp, dec , q))
    print(" "* int(p*sp+5) + "-" * tire)
print("bq =" , bq)
#Самостоятельная dec_to_bq_ver4
prompt = '''\n
Школьный алгоритм по схеме "табличка"

1022 |2
----------
0 |511 | 2
------------(tire = 10)
0 |255 | 2 ......

0 - индекс параметра
3 - кол-во знакомест числа.
.....................
'''
import math
dec = 9999
q = 16
b = dec % q
len_bq = int(math.log(dec, q)) +1
bq = ""
sp = len(str(dec))-1
tire = 10
print('dec = ',dec, 'q = ',q)
print("{0:4} | {1:1}".format(dec,q))
print("-" * tire)
if b >9:
    b= chr(55 + b)
else:
    b = str(b)
    bq = bq+b
for i in range(len_bq):
    bit = str(dec % q)
    bq = bit + bq
    dec = dec // q
    str_frm = " "*int(i*sp+3) + "{0:1} | {1:3} | {2:1}"
    print(str_frm.format(bit, dec, q))
    print(" "* int(i*sp+6) + "-" * tire)
print('bin = ',bq)
#Самостоятельная dec_to_bq_ver5
import math
dec = 9999
q = 16
bq = ""
len_bq = int(math.log(dec, q)) + 1
sp = len(str(dec)) - 1
tire = sp + 10
print("dec =", dec, "q =", q)
print("{0:4} |({1:1})".format(dec, q))
print("-" * tire)
for p in range(len_bq - 1, -1, -1):
    bp = dec % q
    if bp > 9:
        bp = chr(55 + bp)
    else:
        bp = str(bp)
    bq = bq + bp 
    dec = dec // q
    str_frm = " " * sp + "{0:1} |{1:3} |{2:1}"
    print("     " * (len_bq - 1 - p) + str_frm.format(bp, dec, q))
    print("     " * (len_bq  - p) + "-" * tire)
bq = bq[::-1]
print("bq =", bq)
#Самостоятельная dec_to_bq_ver6
import math
dec =   170
q = 2
bq = ""
len_bq = int(math.log(dec, q)) + 1
sp = len(str(dec)) - 1
tire = sp + 10
print("dec =", dec, "q =", q)
print(" " * 2 +"{0:1} | {1:3} | {2:1}  | {3:3}".format('p', 'bp', 'qp' , dec))
print("-" *2* tire)
str_frm = " " * sp + "{0:1} | {1:3} | {2:1}  | {3:3}"
for p in range(len_bq - 1, -1, -1):
    count = p
    bp = dec % q
    if bp > 9:
        bp = chr(55 + bp)
    else:
        bp = str(bp)
    bq = bq + bp
    qp = q**p
    chis = int(dec) % int(qp)
    bp = int(chis / qp)
    str_frm = " " * sp + "{0:1} | {1:3} | {2:1}  | {3:3}"
    print(str_frm.format(count, bp, qp , chis))
    print(" " * tire)
bq = bq[::-1]
print("bq =", bq)