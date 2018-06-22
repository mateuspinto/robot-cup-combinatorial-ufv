# Nome: Mateus Pinto da Silva
# Matrícula: 3489
# Ciência da Computação - UFV-Campus Florestal
# Trabalho Prático de Matemática Discreta: Copa de Robôs

def fatorial(n):
    a=1
    while(n!=0):
        a*=n
        n-=1
    return int(a)

qntTimes=len(input().split((',')))
k=int(input())
s=int(input())

if qntTimes>=k*s:
    resultado=(fatorial(qntTimes)/((pow(fatorial(s),k))*fatorial(qntTimes-k*s)))*fatorial(k)
else:
    resultado=0

print(int(resultado))