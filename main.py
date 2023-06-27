from fastapi import FastAPI
from funciones import simular_pelea
from starlette.responses import RedirectResponse
from models.data import Pelea
import json

app = FastAPI(root_path="")

@app.get("/", include_in_schema=False)
def index():
    response = RedirectResponse(url="" + '/docs')
    return response
    
@app.post("/simular-pelea")
async def sim_fight(data: Pelea):
    """
# Simular Pelea
    """
    ganador = simular_pelea(data.dict())
    if (not ganador):
        raise HTTPException(
            status_code=404, detail="No hay ganador")
    else:
        print(f"{ganador.nombre} {ganador.apellido} gana la pelea y aun le queda {ganador.energia} de energía!")
        return ganador
