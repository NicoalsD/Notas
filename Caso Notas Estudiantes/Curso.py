__author__ = "Nicolas Alejandro Diaz Acosta"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "nicolas.diazacost@campusucc.edu.co"

import random
class Curso:
    
    TOTAL_EST = 12
    
    def __init__(self):
        
        self.__notas=[]
        self.__notas[0] = 2
        self.__notas[1] = 1
        self.__notas[2] = 2
        self.__notas[3] = 1
        self.__notas[4] = 2.4
        self.__notas[5] = 2.6
        self.__notas[6] = 3
    
    def noHaceNadaUtil(self, valor:float):
        
        indice:int = 10
        self.__notas[0] = 3.5
        if valor < 2.5 and len(self.__notas) == self.TOTAL_EST:
            self.__notas[indice] = self.__notas[0]
            self.__notas[0] = valor + 1.0
        else:
            self.__notas[indice] = self.__notas[0]-valor
        
    def LlenarNotas(self):
        est_Cont=0
        while est_Cont < self.TOTAL_ESTUDIANTES:
            self.__notas[est_Cont]= random.uniform(1, 0, 5, 0)
            est_Cont += 1

    def Promedio(self):
        promedio = 0
        est = 0
        while est < self.TOTAL_ESTUDIANTES:
            promedio += self.__notas[est]
            est += 1
        return promedio/self.TOTAL_ESTUDIANTES
    
    def promedioFor(self):
        promedio = 0
        for nota in self.__notas:
            promedio += nota


        return promedio/self.TOTAL_ESTUDIANTES
    

    def notaMasRecurrente(self):
        notaRecurrente:float = 0.0
        cantidadOcurrencias = 0
        for i in range (len(self.TOTAL_ESTUDIANTES)):
            notaBuscada = self.__notas[i]
            contador = 0
            for j in range (len(self.TOTAL_ESTUDIANTES)):
                if self.__notas[j] == notaBuscada:
                    contador += 1
                if contador > cantidadOcurrencias:
                    cantidadOcurrencias = contador
                    notaRecurrente = notaBuscada
        return notaRecurrente
    

    def mayorNota(self):
        mayor:float = 0.0
        
        for i in range(self.TOTAL_EST):
            if self.__notas[i] > mayor:
                mayor = self.__notas[i]
        return mayor
    
    
    def HacerCurva(self):
        for i in range (len(self.TOTAL_EST)):
            nuevaNota = self.__notas[i] * 1.05
            if nuevaNota > 5.0:
                nuevaNota = 5.0
            self.__notas[i] = nuevaNota
            return self.__notas[i]
    
    # Taller clase: Entrega 1 de mayo hasta las 11:59pm
    #1
    def numeroIguales(self):
        contador = 0
        for i in range(len(self.__notas)):
            if self.__notas[i] == 1.5 and contador < 3:
                self.__notas[i] = 2.5
                contador += 1
        return self.__notas
    
    #2
    def terceraNota50(self):
        contador = 0
        for i in range(len(self.__notas)):
            if self.__notas[i] == 5.0:
                contador += 1
                if contador == 3:
                    return i
        return -1
    
    #3
    def reemplazarHasta30(self):
        for i in range(len(self.__notas)):
            if self.__notas[i] > 3.0:
                break
            else:
                self.__notas[i] = 0.0
        return self.__notas

    #4
    def minNotasSuma30(self):
        suma = 0
        for i in range(len(self.__notas)):
            suma += self.__notas[i]
            if suma > 30:
                return i + 1
        return -1
    
    # Tarea Jueves: Entrega 1 de mayo hasta las 2pm

    #1
    def cambiarNotas(self):
        for i in range(len(self.__notas)):
            if self.__notas[i] > 4.0:
                self.__notas[i] -= 0.5  # Resta 0.5 a notas mayores que 4.0
            elif self.__notas[i] < 2.0:
                self.__notas[i] += 0.5  # Suma 0.5 a notas menores que 2.0
        return self.__notas

    #2
    def darMenorNota(self):
        menor = 5.0  # Iniciamos con el valor máximo posible
        for i in range(len(self.__notas)):
            if self.__notas[i] < menor:
                menor = self.__notas[i]  # Actualizamos la nota menor
        return menor

    #3
    def darRangoConMasNotas(self):
        rango1 = 0  # notas de 0.0 a 1.99
        rango2 = 0  # notas de 2.0 a 3.49
        rango3 = 0  # notas de 3.5 a 5.0
        
        for i in range(len(self.__notas)):
            nota = self.__notas[i]
            if nota < 2.0:
                rango1 += 1
            elif nota < 3.5:
                rango2 += 1
            else:  # nota >= 3.5
                rango3 += 1
        
        if rango1 >= rango2 and rango1 >= rango3:
            return 1
        elif rango2 >= rango1 and rango2 >= rango3:
            return 2
        else:
            return 3
        
    # Taller Fin de semana
# no empiezo asjajkas
    
