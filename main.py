from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI(title="Generador de cédula")


@app.get("/obtenercedula")
def obtener_cedula() -> dict:
    numero = random.randint(1000000000, 9999999999)
    return {"cedula": numero}


@app.get("/doblar")
def doblar_numero(n: int) -> dict:
    """Recibe un número entero `n` y devuelve el número multiplicado por 2."""
    return {"resultado": n * 2}


class NumberPayload(BaseModel):
    n: int


@app.post("/doblar_json")
def doblar_numero_json(payload: NumberPayload) -> dict:
    """Recibe JSON `{ "n": <int> }` y devuelve `{ "resultado": n*2 }`."""
    return {"resultado": payload.n * 2}


def int_to_roman(num: int) -> str:
    """Convierte un entero (1..3999) a numeral romano."""
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


@app.get("/romano_aleatorio")
def romano_aleatorio() -> dict:
    """Devuelve aleatoriamente un número entre 50 y 100 y su representación en romano."""
    n = random.randint(50, 100)
    return {"numero": n, "romano": int_to_roman(n)}
