# Servicio FastAPI - Generador de cédula

Este servicio expone un endpoint para devolver un número entero aleatorio de 10 dígitos en el rango `1000000000` a `9999999999`.

## Endpoint

### GET /obtenercedula

No requiere body ni parámetros.

#### Ejemplo de respuesta

```json
{
  "cedula": 8020213910
}
```

## Swagger

Puedes consultar la documentación interactiva en dos formas:

- Swagger UI de FastAPI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- Página HTML estática: abre directamente el archivo `swagger.html` en tu navegador para ver la documentación sin depender de la UI de FastAPI.

FastAPI genera automáticamente esta documentación OpenAPI, y la página HTML incluye una versión visual de Swagger para uso directo desde el navegador.

## Docker Compose

### Levantar el servicio

Desde la raíz del proyecto:

```bash
docker compose up --build
```

### Detener el servicio

```bash
docker compose down
```

### Ver logs

```bash
docker compose logs -f
```

## Dockerfile

El proyecto ya incluye el `Dockerfile` y el `docker-compose.yml` para correr la API en un contenedor.

### Requisitos del contenedor

- Puerto expuesto: `8000`
- Comando principal:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Postman

Se incluye una colección de Postman exportable para probar el servicio.

### Importar la colección

Importa el archivo:

- `postman_collection.json`

### Petición sugerida

- Método: `GET`
- URL: `http://localhost:8000/obtenercedula`

## Estructura del proyecto

```text
.
├── app/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── postman_collection.json
└── ...
```

## Payload / ejemplo de prueba

Como el endpoint es de tipo `GET`, no hay payload en el body. Solo se consulta la URL y la API responde con un valor aleatorio.

### Ejemplo con curl

```bash
curl http://localhost:8000/obtenercedula
```

### Respuesta esperada

```json
{"cedula": 8020213910}
```

## Nota

El número generado siempre cumple esta validación:

```python
1000000000 <= numero <= 9999999999
```

Esto evita que el valor inicie con cero y mantiene 10 dígitos.
