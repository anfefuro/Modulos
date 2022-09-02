class tools08:
    def __init__(self, list07) :
        if type(list07) == list:
            self.list07 = list07
        else:
            self.list07 = [0]
            raise ValueError ('Elemento valido: LIsta de enteros')

    def verificaPrimo(self):
        list071 = [self.__verificaPrimo(i) for i in self.list07]
        return(list(zip(self.list07, list071)))

    def __conversorList(self, origen, destino):
        list072 = [round((self.__conversor(i, origen, destino)), 2) for i in self.list07]
        return(list(zip(self.list07, list072)))

    def factorial(self):
        list073 = [self.__factorial(i) for i in self.list07]
        return(list(zip(self.list07, list073)))
#Verificar Primo<br>
    def __verificaPrimo(self, var01):
        esPrimo = True
        for i in range(2, var01):
            if var01 % i == 0 :
                esPrimo = False
        return(esPrimo)

#Valor modal<br>
    def masRepetido(self, var04) :
        var03 = self.list07
        var031 = {}
        var033 = {}
        if len(var03) == 0 : return None
        for i in sorted(var03) : 
            if i not in var031 :
                var031[i]=1
            else:
                var031[i] += 1
        for k, v in var031.items() :
            var033[v] = k
        if var04 == True :
            return(var033[max(var033)], max(var033))
        else: 
            return(var033[min(var033)], min(var033))

#Conversión grados<br>
    def __conversor(self, valor, origen, destino) :
        if origen == 'cel' and destino == 'far' :
            retorno = ((valor * 9)/5) + 32
        elif origen == 'cel' and destino == 'kel' :
            retorno = valor + 273.15
        elif origen == 'cel' and destino == 'cel':
            retorno = valor
        elif origen == 'far' and destino == 'cel' :
            retorno = ((valor - 32) * 5) / 9
        elif origen == 'far' and destino == 'kel' :
            retorno = (((valor - 32) * 5) / 9) + 273.15
        elif origen == 'far' and destino == 'far':
            retorno = valor
        elif origen == 'kel' and destino == 'cel' :
            retorno = (valor - 273.15)
        elif origen == 'kel' and destino == 'far' :
            retorno= (((valor - 273.15) * 9)/5) + 32
        elif origen == 'kel' and destino == 'kel':
            retorno = valor
        else:
            print('Valor invalido')
        return(retorno)  
#Factorial<br>
    def __factorial(self, var07):
        if type(var07) != int :
            return('Debe ser entero')
        elif var07 < 0 :
            return('Debe ser positivo') 
        elif var07 > 1 :
            var07 *= self.__factorial(var07 - 1)
        elif var07 == 0 :
            return(None)
        return(var07)

    #def conversor(self, valor, origen, destino):
    #    expectingValues = ['cel', 'far', 'kel']
    #    if (valor != False) :
    #        if (type(valor) == int) :
    #            if origen not in expectingValues : 
    #                return('Valores esperados de origen: cel, far o kel, Entregado:', origen)
    #            if destino not in expectingValues :
    #                return('Valores esperado de destino: cel, far o kel, Entregado:', destino)
    #            return(self.__conversor(valor, origen, destino))
    #        return('Ingrese un entero o False, para uso de lista de origen, valor de tipo:', type(valor), 'valor:', valor)

    #    if (type(valor) != int) :    
    #        if (valor == False) :
    #            if origen not in expectingValues : 
    #                return('Valores esperados de origen: cel, far o kel, Entregado:', origen)
    #            if destino not in expectingValues :
    #                return('Valores esperado de destino: cel, far o kel, Entregado:', destino)
    #            return(self.__conversorList(origen, destino))
    #        return('Ingrese un entero o False, para uso de lista de origen, valor de tipo:', type(valor), 'valor:', valor)    

    def conversor(self, origen, destino):
        expectingValues = ['cel', 'far', 'kel']
        if origen not in expectingValues : 
            return('Valores esperados de origen: cel, far o kel, Entregado:', origen)
        if destino not in expectingValues :
            return('Valores esperado de destino: cel, far o kel, Entregado:', destino)
        return(self.__conversorList(origen, destino))

var01 = tools08([3,2,2,3,4,5,2])
