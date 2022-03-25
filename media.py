notaA=float(input("Informe a primeiroa nota: "))
notaB=float(input("informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2


#Verificação
if mediafinal >= 7.0:
    print(" A media : %.1f - Aprovado " % mediafinal);
else:
    print("A Media: %.1f - Reprovado " %mediafinal)