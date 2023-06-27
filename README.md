# Talana Kombat

Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte. Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

## Instalación y ejecución
### Usando línea de comandos
1. Se instalan los requerimientos
```bash
pip install -r requirements.txt
```
2. Se ejecuta el servidor
```bash
uvicorn main:app --reload
```

### Usando docker
1. "Pullear" la imagen de docker
```bash
docker pull elav95/talana-kombat:latest
```
2. Se ejecuta la imagen recién pulleada de docker
```bash
docker run --rm --network host talana-kombat
```

## Uso
La aplicación se ejecuta en un [servidor local](http://127.0.0.1:8000) donde se despliega la función POST para simular pelea. Los datos se entregan como un json con botones de movimiento y golpe que se correlacionan para cada jugada. La app muestra una plantilla del formato json soportado por la app.

A continuación se muestran tres ejemplos de posibles json para probar la app:

```json
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
```
```json
{"player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]}, "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "K"]}}
```
```json
{"player1":{"movimientos":["DSD", "S"], "golpes":["P", ""]}, "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}}
```

### Consideraciones generales
Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes), en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1 (total el player 2 siempre es del hermano chico) 

La secuencia completa del combate de cada jugador se entrega de una vez (consolidada en un json) 
Cada personaje tiene 6 Puntos de energía 

Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea
Tony es el player 1, siempre ataca hacia la derecha (y no cambia de lado)
 Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado)
Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es 
derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos.  