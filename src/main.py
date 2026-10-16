from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.core.database import engine, Base
from src.models import patient  # Importamos el modelo para que SQLAlchemy lo reconozca
from src.api.routes import patients, simulators

# Crea las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ClínicaRed Backend API",
    description="API central para la gestión de citas, pacientes y admisiones.",
    version="1.0.0"
)

# Configuración básica de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers
app.include_router(patients.router)
app.include_router(simulators.router)

@app.get("/", include_in_schema=False)
def read_root():
    """Redirige la raíz principal a la documentación interactiva."""
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["Health"])
def health_check():
    """Endpoint de estado para verificar que la API está viva."""
    return {"status": "ok", "message": "ClínicaRed API running smoothly"}