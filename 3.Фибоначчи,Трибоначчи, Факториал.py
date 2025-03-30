import math
"""
Числа Фибоначчи - последовательность Фибоначчи
f0=0
f1=1
f2=f0=f1
...
fn = fn-2 + fn-1
В окне командного интерпретатора Shell среды разработки IDLE Python
создайте командные строки для вычисления значений последовательности чисел Фибоначчи
>>>i=2;fi_2=0;fi_1=1;fi=fi_2+fi_1; print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
Число f2 = 0 + 1 = 1
>>>i=i+1;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1; print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
Число f3 = 1 + 1 = 2
>>>i=i+1;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1; print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
Число f4 = 1 + 2 = 35
>>>i=i+1;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1; print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
Число f5 = 2 + 3 = 5
>>>i=i+1;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1; print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
Число f6 = 3 + 5 = 8

"""

#задача 1.2.1
def fibonach():
    n = int(input("Введите порядковый номер fn Фибоначчи: "))
    i=2;fi_2=0;fi_1=1;fi=fi_2+fi_1;
    print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
    for i in range(2,n):
        i=i;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1;
        print("Число f"+str(i),"=",fi_2," + ",fi_1," = ",fi)
fibonach()

#задача 1.2.2
def fib_funct(n):
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers

n = 10
fib_sequence = fib_funct(n)
print(f"Последовательность Фибоначчи для n = {n}: {fib_sequence}")

#задача 1.2.3
def fib_funct_trib(n):
    trib_numbers = [0, 0, 1]
    for i in range(3, n):
        trib_numbers.append(trib_numbers[-1] + trib_numbers[-2] + trib_numbers[-3])
    return trib_numbers

n = 10
trib_sequence = fib_funct_trib(n)
print(f"Последовательность Трибоначчи для n = {n}: {trib_sequence}")

#задача 1.2.4
def fib_proc_step():
    n = int(input("Введите порядковый номер fn Фибоначчи: "))
    x = 0
    y = ""
    i=2;fi_2=0;fi_1=1;fi=fi_2+fi_1;
    print(str(x) + ": ",fi_2," + ",fi_1," = ",fi)
    x = 1
    for i in range(2,n):
        i=i;fi_2=fi_1;fi_1=fi;fi=fi_2+fi_1;
        print(str(x) + ": " + y ,fi_2," + ",fi_1," = ",fi)
        x = x + 1
        y = y + 6*" "
fib_proc_step()

"""
Факториал числа n###############
(лат. factorialis - действующий, производящий, умножающий;
обозначающий n!, произносится эн факториал)
n! = 1 * 2 * 3 * 4 ... (n-1) * n

Для вычисления значений факториала n! в окне командного интерпритатора Shell
среды разработки IDLE Python 
построить вычислительную схему с использованием командной строки 

>>> i=1; f=1;   print("Число n!({}) = {}".format(i,f))
Число n! (1) = 1
>>> i=1; f=1*i;   print("Число n!({}) = {}".format(i,f))
Число n! (2) = 2
>>> i=1; f=1*i;   print("Число n!({}) = {}".format(i,f))
Число n! (3) = 6
>>> i=1; f=1*i;   print("Число n!({}) = {}".format(i,f))
Число n! (4) = 24
>>> i=1; f=1*i;   print("Число n!({}) = {}".format(i,f))
Число n! (5) = 120

"""
def factorial():
    n = int(input("Введите факториал n: "))
    i=1; f=1
    for i in range(1,n):
        i; f=i*f;   print("Число n!({}) = {}".format(i,f))
factorial()

def geometry1():
    n = int(input("Введите последний квадрат геометрической прогрессии: "))
    a = int(input("Введите знаменатель: "))
    b = 1
    sum = 1
    for i in range(1,n):
        b = b * a
        sum += b
    print(sum)
geometry1()


def leibnic_funct(n):
    spi=1
    znak=-1
    for i in range (3,n+1,2):
        spi = spi +znak * 1/ i
        znak = -znak
    return spi*4

n = 100000
print(leibnic_funct(n))

def leibnic_funct(n):
    spi=1
    znak=-1
    for i in range (3,n+1,2):
        spi = spi +znak * 1/ i
        znak = -znak
    return spi*4
    n = 100000
    f = open('leibnic.csv','w')
    for i in range (30):
        if i % 10 == 0:
            print(file=f)
            print(f" group#{i}", file=f, flush=True)
        else:
            print(f"{i:3},", file=f)
    f.close()


def piandzetta():
    x = 2
    n = int(input("Введите значение ряда n: "))
    y = 0
    for i in range(1,n+1):
        y = y + 1/i**x
        print("Расчетное пи = {}, точное пи = {}, шаг i = {}".format((6*y)**(1/2),math.pi,i))
        if (6*y)**(1/2) > 3.14:
            break
piandzetta()
