# Despliegue continuo en Render desde GitHub (usando GitHub Actions)

Este documento describe cómo configurar Render y los secrets en GitHub para que el workflow `.github/workflows/deploy-render.yml` dispare despliegues al servicio gratuito de Render.

Pasos:

1. Crear una cuenta en Render
   - Ir a https://render.com y registrarse o iniciar sesión.

2. Crear el servicio en Render
   - En el Dashboard, pulsa **New** → **Web Service**.
   - Conecta tu repositorio de GitHub o elige la opción de Docker (Render soporta `Dockerfile`).
   - Si tu proyecto usa Docker (hay un `Dockerfile` en la raíz), selecciona **Docker** como tipo de entorno.
   - Configura `Build Command` y `Start Command` si no usas Docker. Para FastAPI con Uvicorn por ejemplo:
     - `Build Command`: `pip install -r requirements.txt`
     - `Start Command`: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Completa la creación del servicio.

3. Obtener `RENDER_SERVICE_ID`
   - En el Dashboard abre la página del servicio recién creado.
   - El ID del servicio aparece en la URL o en la API: la URL suele tener el formato `https://dashboard.render.com/services/<SERVICE_ID>`.
   - También puedes listar servicios vía API (requiere API key) y obtener el `id` del servicio.

4. Crear una API Key en Render
   - En Render ve a **Account** → **API Keys** → **Generate Key**.
   - Copia el valor generado (será `RENDER_API_KEY`).

5. Registrar secrets en GitHub
   - En tu repositorio GitHub ve a **Settings** → **Secrets and variables** → **Actions** → **New repository secret**.
   - Añade dos secrets:
     - `RENDER_API_KEY` = (tu API Key de Render)
     - `RENDER_SERVICE_ID` = (el ID del servicio)

6. Qué hace el workflow
   - El archivo `.github/workflows/deploy-render.yml` que añadiste:
     - Se ejecuta en `push` a `main`.
     - Instala dependencias y (opcionalmente) ejecuta tests.
     - Llama a la API de Render para crear un nuevo deploy: `POST /v1/services/{serviceId}/deploys` con Authorization Bearer.

7. Opciones alternativas
   - Render puede auto-desplegarse directamente desde GitHub sin acciones adicionales si conectas el repo desde el panel de Render y habilitas Auto-Deploy. En ese caso no necesitas el trigger por API.
   - Si prefieres ver el resultado del deploy desde Actions, mantiene el enfoque actual con la llamada a la API.

8. Pruebas locales del trigger (opcional)
   - Puedes probar el endpoint de deploy localmente con curl (reemplaza valores):

```bash
curl -X POST "https://api.render.com/v1/services/<SERVICE_ID>/deploys" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <RENDER_API_KEY>" \
  -d '{}'
```

9. Notas y recomendaciones
   - Asegúrate de que tu `Dockerfile` y/o comandos de arranque funcionen en el entorno Linux de Render.
   - Revisa los logs del servicio en Render para diagnosticar fallos de build o runtime.
   - Si tu app requiere variables de entorno, añádelas en Render (Dashboard → Environment → Add Environment Variable) y/o en GitHub Actions según corresponda.

Si quieres, puedo:
- Ajustar el workflow para desplegar en una rama distinta o ante `pull_request`.
- Añadir notificaciones (Slack/Email) tras el deploy.
- Probar el curl de trigger si me das `RENDER_SERVICE_ID` y una API key temporal.
