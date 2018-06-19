# Nome: Mateus Pinto da Silva
# Matrícula: 3489
# Ciência da Computação - UFV-Campus Florestal
# Trabalho Prático de Matemática Discreta: Copa de Robôs

def fatorial(n):
    a=1
    while(n!=0):
        a*=n
        n-=1
    return a

def combinatoria(n,p):
    return fatorial(n)/(fatorial(n-p)*fatorial(p))


qntTimes=len(input("Insira o nome dos times separados por vírgula: ").split((',')))
k=int(input("Insira o número total de grupos do torneio (K): "))
s=int(input("Insira o número de times em cada grupo (S): "))


resultado=1
exist=0
while(qntTimes>=s):
    resultado*=combinatoria(qntTimes,s)
    qntTimes-=s
    exist=1
resultado*=fatorial(k)

if exist==0:
    resultado=0


print(resultado)