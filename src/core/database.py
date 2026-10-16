from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from src.core.config import settings

# Crear el motor de conexión
engine = create_engine(settings.DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para que nuestros modelos de tablas hereden de aquí
Base = declarative_base()

# Dependencia para obtener la sesión de BD en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()