class tools08:
    def __init__(self, list07) :
        if type(list07) == list:
            self.list07 = list07
        else:
            self.list07 = [0]
            raise ValueError ('Elemento valido: LIsta de enteros')

    def __verificaPrimo__(self):
        list071 = [self.verificaPrimo(i) for i in self.list07]
        return(list(zip(self.list07, list071)))

    def __conversor__(self, origen, destino):
        list072 = [round((self.conversor(i, origen, destino)), 2) for i in self.list07]
        return(list(zip(self.list07, list072)))
        
    def __factorial__(self):
        list073 = [self.factorial(i) for i in self.list07]
        return(list(zip(self.list07, list073)))
#Verificar Primo<br>
    def verificaPrimo(self, var01):
        esPrimo = True
        for i in range(2, var01):
            if var01 % i == 0 :
                esPrimo = False
        return(esPrimo)
#Valor modal<br>
    def masRepetido(self, var04) :
        var031 = {}
        var033 = {}
        var034 = {}
        listVer = self.list07
        for i in sorted(listVer) : 
            if i not in var031 :
                var031[i]=1
            else:
                var031[i] += 1
        for k, v in var031.items() :
            var033[v] = k
        if var04 == True :
            var034['Valor Modal'] = var033[max(var033)]
            var034['Repeticiones'] = max(var033)
            return(var034)
        else:
            var034['Valor Anti-Modal'] = var033[min(var033)]
            var034['Repeticiones'] = min(var033) 
            return(var034)
#Conversión grados<br>
    def conversor(self, valor, origen, destino) :
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
    def factorial(self, var07):
        if type(var07) != int :
            return('Debe ser entero')
        elif var07 < 0 :
            return('Debe ser positivo') 
        elif var07 > 1 :
            var07 *= self.factorial(var07 - 1)
        elif var07 == 0 :
            return(None)
        return(var07)