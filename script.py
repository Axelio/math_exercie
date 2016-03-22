LIMITE = int(input("Ingrese el límite de la evaluación: "))

result = []
resultado = 0
stop = False
archivo = open('resultados.txt', 'w')

for q in range(0, LIMITE):
    # Si no es par
    if not (q % 2 == 0) and not (q % 3 == 0):
        resultado = ((q**2)-1)/3
        result.append(resultado)
        if not str(resultado).split('.')[1] == '0':
            print("El ciclo se rompe con q={}".format(q))
            stop = True
        archivo.write("(({}^2)-1)/3 = {}\n".format(q, resultado))
    if stop == True:
        pass
archivo.close()

if stop == False:
    print("Se evaluó desde 0 hasta {} y no se encontró falla".format(LIMITE))
