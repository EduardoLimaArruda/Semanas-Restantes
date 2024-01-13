#Transformar idade em semanas e depois fazer uma conta de menos
print("Quantas semanas faltam para você fazer 90 anos\n")
age = int(input("Quantos anos você tem?\n"))
NoveAnos = float(4696.07)
UmAno = float(52.1786)
Calculate = age * UmAno
Resultado = NoveAnos - Calculate
print("Faltam " + str(round(Resultado,1)) +" semanas para você fazer 90 anos")

enter = input("\nAperte Enter para fechar")