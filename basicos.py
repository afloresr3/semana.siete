class Basicos:
    def __init__(self):

        pass

    def par(self,numero):
        rec = numero % 2
        return rec

    def perfecto(self,numero):
        acu=0
        for divisor in range (1,numero):
            rec= numero%divisor
            if rec == 0:
                acu=acu+divisor
        return acu

    def divisoresNumero(self,numero):
        divisores = []
        for divisor in range(1,numero):
            rec = numero%divisor
            if rec == 0 :
                divisores.append(divisor)
        return divisores
        

ejer = Basicos()

valores=6
print(ejer.divisoresNumero(valores))

# valor=int(input("Ingrese el valor a analizar: "))
# if valor == ejer.perfecto(valor):
#     print(valor,"es perfecto")


#num = numero = int(input("Ingrese un numero: "))
# numeros=[1,3,8,4,5,10]
# pares=[]
# impares = {}
# for num in numeros:
#     if ejer.par(num) == 0:
#         pares.append(num)
#     else:
#         impares[num]="Impar"
# print(pares)
# print(impares)