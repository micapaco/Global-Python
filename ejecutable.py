from clases import Detector, Mutador, Virus, Radiación, Sanador

def mostrar_adn(adn_matriz):
    for fila in adn_matriz:
        print(" ".join(fila))

def main():
    while True:
        try:
            adn_input = input("Ingrese el ADN 6 caracteres separando cada fila por espacios: \n")
            adn_input = adn_input.strip().upper()
            adn_matriz = [list(fila) for fila in adn_input.split()]

            if len(adn_matriz) != 6 or any(len(fila) != 6 for fila in adn_matriz):
                raise ValueError("Ingrese una cadena de 6 caracteres separadas por espacios. \n")
            if any(set(fila) - set("ATCG") for fila in adn_matriz):
                raise ValueError("El ADN debe contener solo los caracteres: A, T, C, G.\n")

            detector = Detector(adn_matriz)
            sanador = Sanador(adn_matriz)
            break  

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

    while True:
        print("\nOpciones disponibles:")
        print("1. Detectar mutaciones")
        print("2. Mutar")
        print("3. Sanar")
        print("4. Salir")
        
        while True:
            opcion = input("Seleccione una opción (1-4): ")
            if opcion in ['1', '2', '3', '4']:
                break
            else:
                print("Opción no válida, intente nuevamente.")

        if opcion == '1':
            if detector.detectar_mutantes() == False:
                print("\nNo se encontraron mutaciones")
        elif opcion == '2':
            print("Seleccione el tipo de mutacion a realizar")
            print("1. Radiacion")
            print("2. Virus")
            
            while True:
                opcion = input("Opcion: ")
                if opcion in ['1', '2']:
                    opcion = int(opcion)
                    break
                else:
                    print("Opción no válida, intente nuevamente.")

            if opcion == 1:
                while True:
                    base_nitrogenada_input = input("Ingrese la base nitrogenada para la mutación (A/T/C/G): ")
                    base_nitrogenada = base_nitrogenada_input.strip().upper()
                    if base_nitrogenada in ['A', 'T', 'C', 'G']:
                        break
                    else:
                        print("Entrada inválida.")

                while True:
                    try:
                        fila = int(input("Ingrese la fila para la mutación (0-5): "))
                        if 0 <= fila <= 5:
                            break
                        else:
                            print("Entrada inválida. La fila debe estar entre 0 y 5.")
                    except ValueError:
                        print("Entrada inválida. Debe ingresar un número entero para la fila.")

                while True:
                    try:
                        columna = int(input("Ingrese la columna para la mutación (0-5): "))
                        if 0 <= columna <= 5:
                            break
                        else:
                            print("Entrada inválida. La columna debe estar entre 0 y 5.")
                    except ValueError:
                        print("Entrada inválida. Debe ingresar un número entero para la columna.")

                posicion_inicial = (fila, columna)
                while True:
                    orientacion_de_la_mutacion_input = input("Ingrese la orientación de la mutación (H/V): ")
                    orientacion_de_la_mutacion = orientacion_de_la_mutacion_input.strip().upper()
                    if orientacion_de_la_mutacion in ['H', 'V']:
                        if orientacion_de_la_mutacion == 'H' and columna > 2:
                            print("La orientación horizontal excede los límites. Intente nuevamente.")
                            break  
                        elif orientacion_de_la_mutacion == 'V' and fila > 2:
                            print("La orientación vertical excede los límites. Intente nuevamente.")
                            break  
                        else:
                            mutador_radiacion = Radiación(base_nitrogenada)
                            adn_matriz = mutador_radiacion.crear_mutante(adn_matriz, posicion_inicial, orientacion_de_la_mutacion)
                            print("\nADN después de la mutación por radiación:")
                            mostrar_adn(adn_matriz)
                            break  
                    else:
                        print("Entrada no valida")

            elif opcion == 2:
                print("Se ingresó a Virus")
                while True:
                    try:
                        fila = int(input("Ingrese la fila para la mutación (0-5): "))
                        if 0 <= fila <= 5:
                            break
                        else:
                            print("Entrada inválida. La fila debe estar entre 0 y 5.")
                    except ValueError:
                        print("Entrada inválida. Debe ingresar un número entero para la fila.")

                while True:
                    try:
                        columna = int(input("Ingrese la columna para la mutación (0-5): "))
                        if 0 <= columna <= 5:
                            break
                        else:
                            print("Entrada inválida. La columna debe estar entre 0 y 5.")
                    except ValueError:
                        print("Entrada inválida. Debe ingresar un número entero para la columna.")

                posicion_inicial = (fila, columna)

                mutador_virus = Virus(None, posicion_inicial)
                adn_matriz = mutador_virus.crear_mutante(adn_matriz, posicion_inicial, None)
                mostrar_adn(adn_matriz)

        elif opcion == '3':
            nueva_matriz = sanador.sanar_mutantes(detector)
            if nueva_matriz != adn_matriz:
                print("\nADN después de sanar mutaciones:")
                mostrar_adn(nueva_matriz)
                adn_matriz = nueva_matriz
            else:
                print("\nEl ADN ya estaba sano, no se realizaron cambios.")
        elif opcion == '4':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()