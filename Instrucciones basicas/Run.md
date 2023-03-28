### Construcción y ejecución de un contenedor

Una vez implementado el **********Dockerfile**********, es hora de generar el contenedor. Para ello, emplearmos dos comandos:

********************************************Construir el contenedor********************************************

```bash
docker build -t myflaskapp .
```

Este comando construirá una imagen de Docker a partir del Dockerfile en el directorio actual y la etiquetará con el nombre "myflaskapp". 

- **docker build** : Es el comando para construir una imagen de Docker.
- **-t myflaskapp** : La opción "-t" se utiliza para etiquetar la imagen con un nombre personalizado. En este caso, la imagen se etiquetará con el nombre "myflaskapp".
- **".” :** El punto indica el contexto de construcción. Es el directorio local en el que se encuentra el Dockerfile. En este caso, se asume que el Dockerfile se encuentra en el directorio actual.

********************************************Ejecutar el contenedor********************************************

```bash
docker run -p 5000:5000 myflaskapp
```

Este comando creará y ejecutará un contenedor de Docker a partir de la imagen "myflaskapp". El contenedor tendrá su puerto 5000 expuesto y mapeado al puerto 5000 del host local, lo que permitirá acceder a la aplicación Flask que se ejecuta en el contenedor a través de un navegador web visitando la dirección "localhost:5000/bluetabers".

- **docker run**: Es el comando para crear y ejecutar un contenedor de Docker.
- **-p 5000:5000**: La opción "-p" se utiliza para exponer el puerto 5000 del contenedor y mapearlo al puerto 5000 del host local. Esto permite que la aplicación Flask que se ejecuta en el contenedor sea accesible desde un navegador web en el host local.
- **myflaskapp**: Es el nombre de la imagen de Docker que se utilizará para crear el contenedor.
