from models.personaje import Player1, Player2

def ejecutar_golpe(jugador, movimiento, golpe, oponente):
    """Función que ejecuta un golpe de un jugador sobre el oponente."""
    dano = 0
    # Tonyn ataca hacia la derecha, Arnaldor hacia la izquierda
    if (isinstance(jugador, Player1)):
        # Evaluar el tipo de movimiento
        if ("DSD" in movimiento and golpe == "P"):
            if (movimiento == "DSD" and golpe == "P"):
                dano = jugador.taladoken()
                oponente.recibir_dano(dano)   
            else:
                submov = list(movimiento.partition("DSD"))
                submov = list(filter(None, submov))
                for mov in submov:
                    if (mov == "DSD"):
                        dano = jugador.taladoken()
                        oponente.recibir_dano(dano)   
                    else:
                        jugador.mover(mov)
                        return
        elif ("SD" in movimiento and golpe == "K"):
            if (movimiento == "SD" and golpe == "K"):
                dano = jugador.remuyuken()
                oponente.recibir_dano(dano)   
            else:
                submov = list(movimiento.partition("SD"))
                submov = list(filter(None, submov))
                for mov in submov:
                    if (mov == "SD"):
                        dano = jugador.taladoken()
                        oponente.recibir_dano(dano)   
                    else:
                        jugador.mover(mov)
                        return
        else:
            if (movimiento and golpe):
                jugador.mover(movimiento)
                dano = jugador.dar_golpe(golpe)
                oponente.recibir_dano(dano)   
            elif (movimiento and not golpe):
                jugador.mover(movimiento)
            elif (not movimiento and golpe):
                dano = jugador.dar_golpe(golpe)
                oponente.recibir_dano(dano)   
    else:
        # Evaluar el tipo de movimiento
        if ("ASA" in movimiento and golpe == "P"):
            if (movimiento == "ASA" and golpe == "P"):
                dano = jugador.taladoken()
                oponente.recibir_dano(dano)   
            else:
                submov = list(movimiento.partition("ASA"))
                submov = list(filter(None, submov))
                for mov in submov:
                    if (mov == "ASA"):
                        dano = jugador.taladoken()
                        oponente.recibir_dano(dano)   
                    else:
                        jugador.mover(mov)
                        return
        elif ("SA" in movimiento and golpe == "K"):
            if (movimiento == "SA" and golpe == "K"):
                dano = jugador.remuyuken()
                oponente.recibir_dano(dano)   
            else:
                submov = list(movimiento.partition("SA"))
                submov = list(filter(None, submov))
                for mov in submov:
                    if (mov == "SA"):
                        dano = jugador.taladoken()
                        oponente.recibir_dano(dano)   
                    else:
                        jugador.mover(mov)
                        return
        else:
            if (movimiento and golpe):
                jugador.mover(movimiento)
                dano = jugador.dar_golpe(golpe)
                oponente.recibir_dano(dano)   
            elif (movimiento and not golpe):
                jugador.mover(movimiento)
                return
            elif (not movimiento and golpe):
                dano = jugador.dar_golpe(golpe)
                oponente.recibir_dano(dano)   
            else:
                return 
    return 

def det_inicio(datos_p1, datos_p2):
    """Función que determina el jugador que comienza la pelea."""
    mov1 = datos_p1["movimientos"]
    golpes1 = datos_p1["golpes"]
    mov2 = datos_p2["movimientos"]
    golpes2 = datos_p2["golpes"]
    if (len(mov1[0]) + len(golpes1[0]) < len(mov2[0]) + len(golpes2[0])):
        return True #True Jugador 1
    elif (len(mov1[0]) + len(golpes1[0]) > len(mov2[0]) + len(golpes2[0])):
        return False #False Jugador 2
    else:
        if (len(mov1) < len(mov2)):
            return True #True Jugador 1
        elif (len(mov1) > len(mov2)):
            return False #False Jugador 2
        else:
            if (len(golpes1) <= len(golpes2)):
                return True #True Jugador
            else:
                return False #False Jugador 2
            

def simular_pelea(json_pelea):
    """Función que simula la pelea entre dos personajes."""
    # Instanciar cada jugador
    jugador1 = Player1()
    jugador2 = Player2()
    
    # Determinar el jugador que inicia
    inicio = det_inicio(json_pelea["player1"], json_pelea["player2"])
    if (inicio):
        jugador_actual = jugador1
        jugador_siguiente = jugador2
    else:
        jugador_actual = jugador2
        jugador_siguiente = jugador1
    
    # Iniciar el juego
    print(f"Comienza la pelea entre {jugador_actual.nombre} {jugador_actual.apellido} y {jugador_siguiente.nombre} {jugador_siguiente.apellido}!")
    while True:
        # Obtener los datos del jugador actual y el oponente
        jugador = json_pelea[jugador_actual.tipo]
        oponente = json_pelea[jugador_siguiente.tipo]
        
        # Verificar si el jugador actual se quedó sin movimientos o golpes
        if (not jugador["movimientos"] and not jugador["golpes"]):
            print(f"{jugador_actual.nombre} {jugador_actual.apellido} se quedó sin movimientos y golpes. Pierde la pelea!")
            ganador = jugador_siguiente
            break
        
        # Obtener el siguiente golpe del jugador actual
        if (jugador["movimientos"]):
            siguiente_movimiento = jugador["movimientos"].pop(0)
        else:
            siguiente_movimiento = ""
        if (jugador["golpes"]):
            siguiente_golpe = jugador["golpes"].pop(0)
        else:
            siguiente_golpe = ""
            
        # Ejecutar el golpe del jugador actual
        ejecutar_golpe(jugador_actual, siguiente_movimiento, siguiente_golpe, jugador_siguiente)
        
        # Verificar si el oponente se quedó sin energía
        if (jugador_siguiente.energia <= 0):
            print(f"{jugador_siguiente.nombre} {jugador_siguiente.apellido} se ha quedado sin energía.")
            ganador = jugador_actual
            break
        
        # Cambiar al siguiente jugador
        temp = jugador_actual
        jugador_actual = jugador_siguiente
        jugador_siguiente = temp
        
    # Retornar al jugador ganador
    return ganador