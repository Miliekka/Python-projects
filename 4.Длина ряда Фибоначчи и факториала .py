
#ЗАДАЧА 1.1.1
def fib_list():
    n = int(input("Введите длину ряда Фибоначчи: "))
    n -= 2
    f = [1,1]
    print(f"Ряд Фибоначчи из {len(f)} чисел: {f}")
    for i in range(n):
        f.append(f[-2]+f[-1])
        print(f"Ряд Фибоначчи из {len(f)} чисел: {f}")
fib_list()

#ЗАДАЧА 1.1.2
def fact():
    n = int(input("Введите длину ряда последовательности факториала: "))
    f = 1
    for i in range(1, n + 1):
        f *= i
        print(f"Факториал {i}! = {f}")
fact()

#ЗАДАЧА 1.1.3
def sum_num_eq_m():
    nums = input("Введите список числовых значений: ").split()
    m = int(input("Введите число m: "))
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    num = []
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == m:
                num.append(nums[i])
                num.append(nums[j])
    print(num)
    return num
sum_num_eq_m()
