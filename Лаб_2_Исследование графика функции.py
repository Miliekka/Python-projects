import matplotlib.pyplot as plt
import numpy as np


#Явный интерфейс " Axes "
import matplotlib.pyplot as plt
fig = plt.figure(); ax = fig.subplots()
ax.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])
plt.show()

#Неявный интерфейс "pyplot"
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])

plt.show()

#1.4 Начало работы. построение графика линейной функции f(x) = ax +b
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], 'o-b')
#(формат  (круги 'o'), стиль линии (сплошная линия '-') и цвет (красный 'r').
plt.ylabel('some numbers')
plt.show()

#1.5 Построение графика линейной функции f(x) = ax +b
x = list(range(-4,5));x
#[-4, -3, -2, -1, 0, 1, 2, 3, 4]
a = 1; b = 1
f = [a*xi + b for xi in x]; f
#[-3, -2, -1, 0, 1, 2, 3, 4, 5]
plt.plot(x, f, '*--b')
#[<matplotlib.lines.Line2D object at 0x000001C3D5976CB0>]
plt.xlabel('x'); plt.ylabel('f(x)')
#Text(0.5, 0, 'x')
#Text(0, 0.5, 'f(x)')
plt.title("Точечный график функции f(x) = ax + b")
plt.plot(x, f, 'ob')

plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(color='gray', linestyle='--')
plt.title("Точечный график функции f(x) = ax + b")
plt.show()

#----------------------------------------------2
import matplotlib.pyplot as plt
a = 3; b = -3; c = -3
x = [xi for xi in range(-3,4)]
f = [a*xi + b for xi in x]
g = [a*xi**2 + b*xi + c for xi in x]

h = list(map(lambda fi, gi: abs(fi-gi),f, g))
plt.plot(x, h,'r', linewidth=1, label=f'h= (f(x) - g(x))')
i = h.index(0, 0); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')
i = h.index(0, i+1); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')

# В подписи меток легенды используем f-строку
plt.plot(x, f,'b',linewidth=1, label=f'f={a}x + {b}')
plt.plot(x, g,'g',linewidth=2, label=f'g={a}x^2 + {b}x + {c}')

# Добавляем подписи и легенду
plt.title("Графики двух функций f(x), g(х)")
plt.xlabel('x')
plt.ylabel('f(x), g(x)')
plt.legend()
# Добавляем оси и сетку
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(color='gray', linestyle='--')
plt.axline((0,3), (2,3), color='r',linestyle=':')
plt.scatter(2,3, color='r')
plt.axline((0,-3), (3, -3), color='r', linestyle=':')
plt.scatter (0,-3, color='r')

plt.show()

#----------------------------------------------3
import matplotlib.pyplot as plt
a = 3; b = -3; c = -3
x = [xi for xi in range(-3,4)]
f = [a*xi + b for xi in x]
g = [a*xi**2 + b*xi + c for xi in x]

h = list(map(lambda fi, gi: abs(fi-gi),f, g))
plt.plot(x, h,'r', linewidth=1, label=f'h= (f(x) - g(x))')
i = h.index(0, 0); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')
i = h.index(0, i+1); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')

# В подписи меток легенды используем f-строку
plt.plot(x, f,'b',linewidth=1, label=f'f={a}x + {b}')
plt.plot(x, g,'g',linewidth=2, label=f'g={a}x^2 + {b}x + {c}')

# Добавляем подписи и легенду
plt.title("Графики двух функций f(x), g(х)")
plt.xlabel('x')
plt.ylabel('f(x), g(x)')
plt.legend()
# Добавляем оси и сетку
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(color='gray', linestyle='--')
plt.axline((0,3), (2,3), color='r',linestyle=':')
plt.scatter(2,3, color='r')
plt.axline((0,-3), (3, -3), color='r', linestyle=':')
plt.scatter (0,-3, color='r')


y0 = -4; yn = 10
plt.ylim(y0, yn)
plt.yticks(list(range(y0, yn)), minor=True)
plt.grid(which='minor', linestyle=':')

y0 = -6; yn = 10; plt.ylim(y0, yn)
plt.yticks(list(range(y0, yn)), minor=True)
plt.grid(which='minor', linestyle=':')

n = 100; x0 = -3; xn = 3
dx = (xn-x0)/n
x = [x0 +xi*dx for xi in range(n)]
plt.show()

#----------------------------------------------4
import matplotlib.pyplot as plt
a = 3; b = -3; c = -3
x = [xi for xi in range(-3,4)]
f = [a*xi + b for xi in x]
g = [a*xi**2 + b*xi + c for xi in x]

h = list(map(lambda fi, gi: abs(fi-gi),f, g))
plt.plot(x, h,'r', linewidth=1, label=f'h= (f(x) - g(x))')
i = h.index(0, 0); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')
i = h.index(0, i+1); i
print(f'Точка с индексом {i}: (x,f)={x[i],f[i]}; (x,g)={x[i],g[i]}')

# В подписи меток легенды используем f-строку
plt.plot(x, f,'b',linewidth=1, label=f'f={a}x + {b}')
plt.plot(x, g,'g',linewidth=2, label=f'g={a}x^2 + {b}x + {c}')

# Добавляем подписи и легенду
plt.title("Графики двух функций f(x), g(х)")
plt.xlabel('x')
plt.ylabel('f(x), g(x)')
plt.legend()
# Добавляем оси и сетку
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(color='gray', linestyle='--')
plt.axline((0,3), (2,3), color='r',linestyle=':')
plt.scatter(2,3, color='r')
plt.axline((0,-3), (3, -3), color='r', linestyle=':')
plt.scatter (0,-3, color='r')

y0 = -4; yn = 10
plt.ylim(y0, yn)
plt.yticks(list(range(y0, yn)), minor=True)
plt.grid(which='minor', linestyle=':')

y0 = -6; yn = 10; plt.ylim(y0, yn)
plt.yticks(list(range(y0, yn)), minor=True)
plt.grid(which='minor', linestyle=':')
n = 100; x0 = -3; xn = 3
dx = (xn-x0)/n
x = [x0 +xi*dx for xi in range(n)]


print(f'{x[:10]=}\n...\n{x[-10:]=}')

print(f'{f[:10]=}\n...\n{f[-10:]=}')

print(f'{g[:10]=}\n...\n{g[-10:]=}')

print(f'{h[:10]=}\n...\n{h[-10:]=}')

plt.show()

#----------------------------------------------СР
import matplotlib.pyplot as plt
a = 1; b = 5; 
x = np.linspace(-4,4)
y1 =[xi for xi in x]
y2 = [xi**2 - b for xi in x]
y3 = [b* np.sin(xi) for xi in x]

# В подписи меток легенды используем f-строку
plt.plot(x, y1,'b',linewidth=1, label=f'y1= x')
plt.plot(x, y2,'orange',linewidth=2, label=f'y2= x**2 - {b}')
plt.plot(x, y3,'g',linewidth=3, label=f'y3= {b}*sin(x)')
#доб-м точки
plt.scatter(2.5258,2.528, color='r')
plt.scatter (2.75,2.75, color='r')
plt.scatter(0,0, color='r')
plt.scatter (-1.75,-1.75, color='r')
plt.scatter(-2.52,-2.51, color='r')
# Добавляем подписи и легенду
plt.title("Графики функций")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# Добавляем оси и сетку
plt.axhline(0, color='black', linestyle='-')
plt.axvline(0, color='black', linestyle='-')
plt.grid(color='gray', linestyle='--')

plt.show()

#----------------------------------------------Уравнение касательной к графику функции
import numpy as np
import matplotlib.pyplot as plt
# Исходная функция
def f(x):
    return x**2
# Определяем производную исходной функции
def df(x):
    return 2*x
# Определяем независимую переменную
x = np.linspace(-5, 5, 100)
# Выбираем точку для построения касательной линии
x1 = -3
y1 = f(x1)
# Уравнение касательной линии
def line(x, x1, y1):
    return df(x1) * (x - x1) + y1
# Ограничиваем пространство касательной
xr = np.linspace(x1 - 1, x1 + 1, 10)
yr = line(xr, x1, y1)
# Строим график
plt.figure()
# График исходной функции
plt.plot(x, f(x))
# Точка касательной
plt.scatter(x1, y1, color='C1', s=50)
# График касательной
plt.plot(xr, yr, 'C1--', linewidth=2)
# Добавление осей
plt.axvline(x=0, color="black", linestyle="--")
plt.axhline(y=0, color="black", linestyle="--")
# Настройка графика
plt.grid(linestyle='--')
plt.title('График функции и касательной')
plt.show()
