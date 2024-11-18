import random

class Detector:
    def __init__(self, adn):
        self.adn_matriz = [list(fila) for fila in adn]
        self.num = len(adn)

    def detectar_mutantes(self, imprimir=True):
        mutacion_horizontal = self.detector_horizontal()
        mutacion_vertical = self.detector_vertical()
        mutacion_diagonal = self.detector_diagonal()
        hay_mutaciones = mutacion_horizontal or mutacion_vertical or mutacion_diagonal      
        if imprimir and hay_mutaciones:
            print("Se detectaron mutaciones")
            if mutacion_horizontal:
                print("Hemos encontrado mutaciones horizontales.")
            if mutacion_vertical:
                print("Hemos encontrado mutaciones verticales.")
            if mutacion_diagonal:
                print("Hemos encontrado mutaciones diagonales.")
        return hay_mutaciones

    def detector_horizontal(self):
        for fila in self.adn_matriz:
            for i in range(self.num - 3):
                if fila[i] == fila[i + 1] == fila[i + 2] == fila[i + 3]:
                    return True
        return False

    def detector_vertical(self):
        for columna in range(self.num):
            for fila in range(self.num - 3):
                if (self.adn_matriz[fila][columna] == self.adn_matriz[fila + 1][columna] == 
                        self.adn_matriz[fila + 2][columna] == self.adn_matriz[fila + 3][columna]):
                    return True
        return False

    def detector_diagonal(self):
        for columna in range(self.num - 3):
            for fila in range(self.num - 3):
                if (self.adn_matriz[fila][columna] == self.adn_matriz[fila + 1][columna + 1] == 
                        self.adn_matriz[fila + 2][columna + 2] == self.adn_matriz[fila + 3][columna + 3]):
                    return True
        for fila in range(self.num - 3):
            for columna in range(3, self.num):
                if (self.adn_matriz[fila][columna] == self.adn_matriz[fila + 1][columna - 1] == 
                        self.adn_matriz[fila + 2][columna - 2] == self.adn_matriz[fila + 3][columna - 3]):
                    return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada, posicion_inicial): 
        self.base_nitrogenada = base_nitrogenada
        self.posicion_inicial = posicion_inicial

    def crear_mutante(self):
        pass


class Radiación(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada, None) 

    def crear_mutante(self, ADN, posicion_inicial, orientacion_de_la_mutacion):
        try:
            if orientacion_de_la_mutacion not in ["H", "V"]:
                raise ValueError("La orientación debe ser 'H' (horizontal) o 'V' (vertical).")

            base_repetida = self.base_nitrogenada
            fila, columna = posicion_inicial

            filas = len(ADN)
            columnas = len(ADN[0])

            if orientacion_de_la_mutacion == "H":
                if columna + 4 > columnas:
                    raise IndexError("La mutación horizontal excede los límites de la matriz.")
                for i in range(4):
                    ADN[fila][columna + i] = base_repetida 

            elif orientacion_de_la_mutacion == "V":
                if fila + 4 > filas:
                    raise IndexError("La mutación vertical excede los límites de la matriz.")
                for i in range(4):
                    ADN[fila + i][columna] = base_repetida  
                
            return ADN

        except IndexError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return ADN




class Virus(Mutador):
    def __init__(self, base_nitrogenada, posicion_inicial):
        super().__init__(base_nitrogenada, posicion_inicial)

    def crear_mutante(self, adn_matriz, posicion_inicial, base_nitrogenada):
        try:
            fila, columna = posicion_inicial

            if len(adn_matriz) != 6 or len(adn_matriz[0]) != 6:
                print("Error: La matriz de ADN debe ser al menos de 6x6 para realizar la mutación.")
                return adn_matriz

            print("Seleccione la base con la que desea mutar la diagonal:")
            print("1. A")
            print("2. C")
            print("3. T")
            print("4. G")
            seleccion = input("Seleccione una opción (1-4): ")
            if seleccion == '1':
                nueva_base = "A"
            elif seleccion == '2':
                nueva_base = "C"
            elif seleccion == '3':
                nueva_base = "T"
            elif seleccion == '4':
                nueva_base = "G"
            else:
                print("Selección no válida. Usando 'A' por defecto.")
                nueva_base = "A"
            for i in range(4): 
                if isinstance(adn_matriz[i], str):
                    adn_matriz[i] = list(adn_matriz[i])
                adn_matriz[i][i] = nueva_base
                
            print("ADN después de la mutación por Virus:")

            return adn_matriz

        except IndexError:
            print("Error al mutar el ADN en la diagonal principal")
            return adn_matriz
class Sanador:
    def __init__(self, adn):
        self.adn_matriz = [list(fila) for fila in adn]
        self.num = len(adn)

    def sanar_mutantes(self, detector):
        letras = "ATCG"
        print("Curando mutaciones...")
        if detector.detectar_mutantes(imprimir=False):
            while detector.detectar_mutantes(imprimir=False):
                self.adn_matriz = [[random.choice(letras) for _ in range(6)] for _ in range(6)]
                detector = Detector(self.adn_matriz)

        return self.adn_matriz