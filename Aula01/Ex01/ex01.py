from func import calvalor
from func import calvalorpg

preço = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valdesc = calvalor(preço, desconto)
valpg = calvalorpg(preço, valdesc)


print("Um desconto de %5.2f %% em mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valdesc)
print("O valor a pagar é de R$ %7.2f" % valpg) 