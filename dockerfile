# Imagen base con Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto de Streamlit
EXPOSE 8501

# Ejecutar la app al iniciar el contenedor
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
