class Character():
    def __init__(self):
        self.energia = 6
        self.nombre = None
        self.apellido = None 
        self.tipo = None

    def recibir_dano(self, dano):
        self.energia -= dano
        print(f"{self.nombre} pierde {dano} puntos de energía. Energía restante: {self.energia}")
        return

    def dar_golpe(self, golpe):
        dano = 1
        if (golpe == "K"):
            print(f"{self.nombre} da una patada")
        else:
            print(f"{self.nombre} da un puñetazo")
        return dano


    def taladoken(self):
        # Método vacío
        pass

    def remuyuken(self):
        # Método vacío
        pass

class Player1(Character):
    def __init__(self):
        self.energia = 6
        self.tipo = "player1"
        self.nombre = "Tonyn"
        self.apellido = "Stallone"

    def mover(self, movimiento):
        if (movimiento == "D"):
            print(f"{self.nombre} avanza")
        elif(movimiento == "A"):
            print(f"{self.nombre} retrocede")
        elif (movimiento == "S"):
            print(f"{self.nombre} se agacha")
        elif (movimiento == "W"):
            print(f"{self.nombre} salta")
        else:
            pass
        return

    def taladoken(self):
        print(f"{self.nombre} ejecuta un Taladoken!")
        dano = 3
        return dano
    def remuyuken(self):
        print(f"{self.nombre} ejecuta un Remuyuken!")
        dano = 2
        return dano

class Player2(Character):
    def __init__(self):
        self.energia = 6
        self.tipo = "player2"
        self.nombre = "Arnaldor"
        self.apellido = "Shuatseneguer"

    def mover(self, movimiento):
        if (movimiento == "A"):
            print(f"{self.nombre} avanza")
        elif(movimiento == "D"):
            print(f"{self.nombre} retrocede")
        elif (movimiento == "S"):
            print(f"{self.nombre} se agacha")
        elif (movimiento == "W"):
            print(f"{self.nombre} salta")
        else:
            pass
        return

    def taladoken(self):
        print(f"{self.nombre} ejecuta un Taladoken!")
        dano = 2
        return dano
    def remuyuken(self):
        print(f"{self.nombre} ejecuta un Remuyuken!")
        dano = 3
        return dano