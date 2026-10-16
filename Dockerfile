# Usamos una imagen oficial ligera de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para compilación y drivers
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente completo del proyecto
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la API con Uvicorn escuchando en todas las interfaces
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]