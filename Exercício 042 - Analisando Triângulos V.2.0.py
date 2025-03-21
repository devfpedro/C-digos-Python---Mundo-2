#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de ângulo será formado:
#Equilátero: Todos os lados iguais;
#Isóceles: Dois lados iguais;
#Escaleno: Todos os lados diferentes.

reta1= float(input("Informe o compprimento da primeira reta: ").strip())
reta2= float(input("Informe o comprimento da segunda reta: ").strip())
reta3= float(input("Informe o comprimento da terceira reta: ").strip())

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2:
    print(f"As retas {reta1} {reta2} e {reta3} podem formar um triângulo.")
    if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo equilátero, pois todos os lados são iguais.")
    elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta3 == reta1 and reta3 != reta2):
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo isóceles, pois dois lados, dos três, são iguais.")
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print(f"As retas {reta1}, {reta2} e {reta3} formam um triângulo escaleno, pois todos os três lados são diferentes.")
else:
    print(f"As retas {reta1}, {reta2} e {reta3} não podem formar um triângulo.")
