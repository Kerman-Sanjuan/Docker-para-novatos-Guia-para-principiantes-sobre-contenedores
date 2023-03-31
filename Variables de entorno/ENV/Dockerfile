# Utilizar la imagen oficial de Python como imagen base
FROM python:3.10.10-bullseye


ENV APP_HOME=/app \
    APP_PORT=5000 
# Establecer el directorio de trabajo dentro del contenedor
WORKDIR ${APP_HOME}

# Copiar el archivo de requerimientos y la aplicación Flask en el contenedor
COPY requirements.txt .
COPY app.py .

# Instalar las dependencias de Python
RUN pip install -r requirements.txt

# Exponer el puerto 5000 para que pueda ser accedido externamente
EXPOSE ${APP_PORT}

# Iniciar la aplicación Flask cuando el contenedor se inicie
CMD flask run -h 0.0.0.0 -p 5000