class Calculadora():

    def __init__(self):
        self.total = 0
        # Bucle infinito
        while True:
            # Gestionamos las exceptions
            try:
                # Introducimos datos y mostramos el menu
                print ("===========Calculadora===========")
                try:
                    o = raw_input("Introduce un numero por pantalla: ")
                    if o == "Salir" or o == "salir" or o == "Exit" or o == "exit":
                        print "Saliendo del menu"
                        break
                    numero1 = float(o)
                except:
                    numero1 = self.total
                numero2 = float(input("Intoduce otro numero por panralla: "))
                print("""\n=========Menu=========
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir""")
                opcion = int(input("Que quieres realizar ? "))
                # Si la opcion es correcta invoca el metodo
                if opcion >= 1 and opcion <= 4:
                    self.__Opciones(opcion, numero1, numero2)
                # Solo salimos del menu si la opcion es salir
                elif opcion == 5:
                    print ("Saliendo del menu")
                    break
                # Mostramos exceptions
                else:
                    print("La opcion {}, no es correcta, inserta una opcion que este entre 1 y 4\n".format(opcion))
            # Mostramos exceptions
            except:
                print("El caracter introducido no es valido.\n")

    # Comprueba lo que tiene que hacer segun la ocpion insertada
    def __Opciones(self, opcion, numero1, numero2):
        if opcion == 1:
            total = numero1+numero2
            print numero1, "+", numero2, "= ", self.__Integer(total)
        elif opcion == 2:
            total = numero1-numero2
            print numero1, "-", numero2, "=", self.__Integer(total)
        elif opcion == 3:
            total = numero1*numero2
            print numero1, "*", numero2, "=", self.__Integer(total)
        elif opcion == 4:
            total = numero1/numero2
            print numero1, "/", numero2, "=", self.__Integer(total)

    # Pasa el total a integer si es posible
    def __Integer(self, total):
        if total.is_integer():
            self.total = total
            return int(self.total)
        else:
            self.total = total
            return self.total



p = Calculadora()