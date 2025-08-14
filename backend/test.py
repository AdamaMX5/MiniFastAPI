from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # Neu
from fastapi.responses import FileResponse  # Neu

app = FastAPI()

# Statische Dateien servieren
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Favicon-Endpunkt hinzufügen
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")
