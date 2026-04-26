import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
app.title = "Aliados API"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def cargar_datos():
    with open("aliados.json", "r", encoding="utf-8") as file:
        return json.load(file)

Personajes = cargar_datos()

@app.get("/aliados/info")
async def info():
    return {"mensaje" : "Hola! Desde la API de Aliados (2013) mi primera API hecha con FASTApi! <3"}


@app.get("/aliados")
async def mostrar_personajes():
    return Personajes

@app.get('/aliados/{p_id}')
def obtener_personaje(p_id: str):
    personaje = next((p for p in Personajes if p['id'] == p_id), None)
    if personaje:
        return personaje
    raise HTTPException(status_code=404, detail="No encontrado")
    
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT",8000))
    uvicorn.run(app, host="0.0.0.0",port=port)