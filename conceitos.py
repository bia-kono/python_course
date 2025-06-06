print("Hello, World!")

if 5>2:
    print("Five is greater than two") # É crucial o uso do recuo (identation) - block of code
    print("Five is greater than two")

"""
tudo que estiver dentro esta sendo ignorado porque
essas strings nao estao alocados para uma variavel
"""

# declare variables - simple and easy - '' or ""
x=5
y="Jhon"
print(x)
print(y)

# roda os dois mas fixa no ultimo
x=8
x="Salt"
print(x) # o output será somente Salt

# case sensitive - age, Age, AGE - diferente
a=4
A="Sally"
print(A)

# casting - identificar o tipo de variável
x=str(3)
y=int(3)
z=float(3)
print(x, y, z) # output: '3' 3 3.0

# to know what type of variable - function type()
x=5
y="Jhon"
print(type(x))
print(type(y))

# vários valores para varias variáveis
x,y,z="Orange","Banana","Cherry"
print(x)
print(y)
print(z)

# um valor para varias variáveis
x=y=z="Orange"
print(x)
print(y)
print(z)
print(x,y,z)

# unpack collection - precisa ter a mesma quantidade de valores para variáveis
letter = ["A","B","C"]
x,y,z=letter
print(x)
print(y)
print(z)
print(x,',',y,',',z,'.')

x="Python"
y="is"
z="awesome"
print(x,y,z)

x="Python"
y="is"
z="awesome"
print(x+y+z)

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x=5
y=55
z=-55
print(type(x))
print(type(y))
print(type(z))

x = 35e2
y = 12E4
z = -87.7e100
print(type(x))
print(x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex
#converting
a = float(x)
b = int(x)
c = complex(x)
d = complex(y)
#e = int(z) = Não se pode converter complex em outro tipo!
print(a)
print(b)
print(c)
print(d)
#print(e) Não se pode converter complex em outro tipo!
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#print(type(e)) Não se pode converter complex em outro tipo!

#to random numbers from 1 to 9
import random
print(random.randrange(1,10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int(3.3)
print(z)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello Bia"
print(a[6])

for x in "banana":
  print(x)
  
ban = "The best things in life are free!"
print("free" in ban)

ban = "The best things in life are free!"
if "free" in ban:
  print("Yes, 'free' is present.")

boba = "The best things in life are free!"
print("free" not in boba)

boba = "The best things in life are free!"
if "free" not in boba:
  print("Yes, 'free' is not present.")

b = "Hello, World!"
print(b[-3:])

b = "Hello, World!"
print(b[0:4])

b = "Hello, World!"
print(b[:8])

minha_string = "olá mundo"
string_maiuscula = minha_string.upper()
print(string_maiuscula)
palavras = minha_string.split()
print(palavras)

a="Olá João" 
print(a)
print(a.upper())
print(a.lower())

def cumprimentar(nome):
  return f"Olá, {nome}!"
mensagem = cumprimentar("Alice")
print(mensagem)

g = "Olá mundo"
print(g.replace("O", "K"))

x = "Oi mundo"
y = "da Bia"
z = x + " " + y
print(z)

idade = 31
Xbia = f"Minha idade é {idade}"
print(Xbia)

valor_venda = f"O preço é {20 * 59:.2f} reais" # adição do modificador após ":" .2f = 2 casas decimais
print(valor_venda)

x = "Meu \nnomw \té Bianca \bmas você pode me \tchamar \fde \"Bia\""
print(x)