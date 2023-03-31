### Variables de entorno y secretos

****************************************Variables de entorno****************************************

Cuando trabajamos con Docker, es necesario distinguir entre dos tipos de variables - ARG y ENV.

********ARG********

La instrucción ARG se emplea para declarar variables de entorno que solo serán accesibles durante el tiempo de construcción de la imagen. Cuando la imagen se encuentre en ejecución, este valor no podrá ser accedido por el contenedor. Sin embargo, los valores ARG pueden ser fácilmente inspeccionados después de que una imagen es construida, viendo el historial docker de una imagen. Por lo tanto, son una mala elección para los datos sensibles.

Esto llevado a la práctica, mostaría lo siguiente:

```bash
FROM busybox
ARG user=UsuarioBluetaber
ARG categoria=Technician

RUN echo "Soy ${user} con la categoria ${categoria}"
```

Ejecutando el comando **`docker build .`** 
  Como vereís, hay una linea donde se muestra el mensaje con las variables de entorno. Además, estos argumentos pueden ser definidos a la hora de lanzar el comando desde la CLI:

`d**ocker build --build-arg user=ExternalIBM --build-arg categoria=EnterpriseArchitect .build .**`



La instrucción ENV se emplean también durante la construcción, pero a diferencia de ARG, si son accesibles por el contenedor una vez construido.