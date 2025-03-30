def build_domik(n,m,simb):
  global build
  build = build + (n * ' ' + m * simb + (n+1) * ' ')*x +'\n'
def block_krysha():
  for i in range(k):
      build_domik(k-i,i*2+1, simb)
def block_potolok():
    build_domik(0,d,simb)
def block_stena():
  for i in range(s):
      build_domik(1, d-2, simb)
def block_pol():
    build_domik(0,d,simb)
def build_domik_block():
    block_krysha()
    block_potolok()
    block_stena()
    block_pol()
build=''
simb='A'
kod =ord(simb)
simbol = chr(kod)
x=int(input('Сколько хотите домиков? '))
simb=input("Введите символ:")
d=int(input("Введите высоту домика:"))
k=int(d/2)
p=1
s=d-k-2*p

build_domik_block()
print(build)
input("Нажмите клавишу <Enter> для выхода")