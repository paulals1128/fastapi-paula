from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel

app = FastAPI()

ARCHIVO = "films.json"

class Film(BaseModel):
    titulo: str
    director: str
    anio: int


def leer():
    with open(ARCHIVO, encoding="utf-8") as f:
        return json.load(f)


def guardar(films):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(films, f, indent=2, ensure_ascii=False)

@app.get("/")
def inicio():
    return {"mensaje": "FastAPI de Paula"}

@app.get("/films")
def listar():
    return leer()

@app.get("/films/{id}")
def buscar(id: int):
    for film in leer():
        if film["id"] == id:
            return film
    raise HTTPException(status_code=404, detail="Esta película no existe")

@app.post("/films")
def agregar(film: Film):
    films = leer()
    id_mas_alto = 0
    for f in films:
        if f["id"] > id_mas_alto:
            id_mas_alto = f["id"]
    nuevo = {
        "id": id_mas_alto + 1,
        "titulo": film.titulo,
        "director": film.director,
        "anio": film.anio,
    }
    films.append(nuevo)
    guardar(films)
    return nuevo

@app.put("/films/{id}")
def editar(id: int, datos: Film):
    films = leer()
    for film in films:
        if film["id"] == id:
            film["titulo"] = datos.titulo
            film["director"] = datos.director
            film["anio"] = datos.anio
            guardar(films)
            return film
    raise HTTPException(status_code=404, detail="Esta película no existe")

@app.delete("/films/{id}")
def borrar(id: int):
    films = leer()
    for film in films:
        if film["id"] == id:
            films.remove(film)
            guardar(films)
            return {"mensaje": "Película borrada"}
    raise HTTPException(status_code=404, detail="Esta película no existe")