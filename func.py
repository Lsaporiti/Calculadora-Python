#solução do lukyanh
#def calculo(num1,operador,num2):
#    return eval(f'{num1} {operador} {num2}')

# 1
def soma(num1):
    num2 = float(input())
    return num1+num2
# 2
def subt(num1):
    num2 = float(input())
    return num1-num2
# 3
def mult(num1):
    num2 = float(input())
    return num1*num2
# 4
def div(num1):
    num2 = float(input())
    return num1/num2
# 5
def poten(num1):
    num2 = float(input())
    return num1**num2
# 6
def raiz(num1):
    num2 = float(input())
    num3 = 1/num2
    return num1**num3


while True:
    x = int(input('Numero: '))
    op = int(input('Operação: '))
    if op == 1:
        print(soma(x))
    elif op == 2:
        print(subt(x))
    elif op == 3:
        print(mult(x))
    elif op == 4:
        print(div(x))
    elif op == 5:
        print(poten(x))
    elif op == 6:
        print(raiz(x))