# Para definir las clases se recomienda utilizar Pascal Case
#class Futbolista():
    #posicion = "Delantero"
    #equipo = "FC Barcelona"
    #edad = 30
    #region = "Caribeña"
# Cuando instanciamos la clase, se crean objetos
# Cada objeto es una instancia de la clase
#Jugador1 = Futbolista()
#Jugador2 = Futbolista()
#Jugador3 = Futbolista()
class Futbolista:
    # El método __init__ es el constructor de la clase
    # Se ejecuta automáticamente al crear una instancia de la clase
    def __init__(self, posicion, equipo, edad, region):
        self.posicion = posicion
        self.equipo = equipo
        self.edad = edad
        self.region = region

    def jugar_partido(self):
        print (f"El {self.posicion} del {self.equipo} está jugando un partido.")
        
jugador1 = Futbolista("Delantero", "Atletico Nacional", 30, "Caribeña")
jugador2 = Futbolista("Portero", "America de Cali", 28, "Andina")
jugador3 = Futbolista("Defensa", "Deportivo Pereira", 25, "Europea")
jugador2.jugar_partido()
jugador1.jugar_partido()
ugador2.jugar_partido()
jugador1.jugar_partido()