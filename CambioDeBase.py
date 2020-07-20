numOrigen = input("Ingrese el numero de origen: ")
baseOrigen = int(input("Ingrese la base de origen: "))
baseDestino = int(input("Ingrese la base de destino: "))
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
abc = list(abc) #Convertimos el abcedario en una lista de strings
def Letra_A_Decimal(digito): 
    return abc.index(digito) + 10
def Decimal_A_Letra(digito):
    digito = digito - 10
    return abc[digito]
def baseEspecifica_A_decimal(numOrigen, baseOrigen):
    acumulador = 0
    numOrigen = list(numOrigen)

    for i in range(len(numOrigen)): # i = 0,1,...,n-1
        digito = numOrigen[len(numOrigen)-i-1] # n-1,n-2,...,1,0
        if digito.isnumeric():
            digito = int(digito)
        else:
            digito = Letra_A_Decimal(digito)

        acumulador += digito * (baseOrigen**i)
    return acumulador
def Decimal_a_baseEspecifica(numDecimal, baseDestino):
    restos = []
    resto = 0
    separador=""
    while True:
        if numDecimal < baseDestino:
            if numDecimal>=10:
                numDecimal = Decimal_A_Letra(numDecimal)
            restos.append(str(numDecimal))
            restos.reverse()
            return separador.join(restos)
        else:
            resto = numDecimal % baseDestino
            if resto >= 10:
                resto = Decimal_A_Letra(resto)
            restos.append(str(resto))
            numDecimal = numDecimal // baseDestino
            
def cambioDeBase(numOrigen, baseOrigen, baseDestino):
    numOrigen = str(numOrigen)
    return Decimal_a_baseEspecifica(baseEspecifica_A_decimal(numOrigen,baseOrigen),baseDestino)

print(cambioDeBase(numOrigen,baseOrigen,baseDestino))

