# La ultima version de python era 3.14, pero usé 3.13 porque no es buena practica usar la ultima version de python.
# Se usa la imagen slim-bookworm para reducir el tamaño de la imagen.
FROM python:3.13-slim-bookworm
# Se establece el directorio de trabajo en /app
WORKDIR /app
# Se copian los archivos necesarios al directorio de trabajo
COPY data_prueba_técnica.csv data_prueba_técnica.csv
COPY requirements.txt requirements.txt
COPY load.py load.py
COPY extract.py extract.py
COPY transform.py transform.py
COPY dispertion.py dispertion.py
COPY view_sql.py view_sql.py
# Se instalan las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Esperar a que MySQL esté listo antes de ejecutar la inicialización
CMD ["sh", "-c", "sleep 10 && python load.py"]