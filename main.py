from fastapi import FastAPI
import random

app = FastAPI(title="Generador de cédula")


@app.get("/obtenercedula")
def obtener_cedula() -> dict:
    numero = random.randint(1000000000, 9999999999)
    return {"cedula": numero}


@app.get("/doblar")
def doblar_numero(n: int) -> dict:
    """Recibe un número entero `n` y devuelve el número multiplicado por 2."""
    return {"resultado": n * 2}
