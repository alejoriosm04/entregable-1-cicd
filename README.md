# entregable-1-cicd
Primer entregable del curso de CI/CD

## Integrantes

- Lina Sofia Ballesteros (@linaballesteros) | Alejandro Rios Muñoz (@alejoriosm04)

## Preguntas

### ¿Qué eventos configuraste para disparar tu workflow y por qué?

Los eventos que configuramos fueron 3: 

- `push` con rama `main`: con el objetivo de ejecutar las verificaciones al hacer push o merge en la rama `main`.
- `pull_request` a la rama `main`: para realizar la verificacion antes de hacer un merge a la rama `main`.
- `workflow_dispatch`: activar manualmente la verificacion nosotros cuando lo necesitemos.

Se realizan 3 steps, imprimir un mensaje, configurar python y ejecutar un script de python que muestra información en un mensaje.

### ¿Qué sistema operativo utiliza el runner ubuntu-latest y por qué puede ejecutar tu workflow aunque tu computadora sea Windows o macOS? ¿Qué relación tiene el runner con el shell de los pasos run?

- Utiliza Linux en una distro Ubuntu Latest, al ser el S.O de la maquina virtual de un entorno en la nube, que esta aislado del ambiente local de nosotros.

- Es la linea de comandos que se utiliza del S.O donde se ejecuta el entorno de Ubuntu.

### Menciona al menos 3 acciones pre-construidas del Marketplace de GitHub Actions no mencionadas en este material. Excluye actions/checkout, actions/setup-python, actions/upload-artifact y aws-actions/configure-aws-credentials, aunque alguna solo aparezca como ejemplo conceptual. Describe qué hacen y para qué sirven.

Elegimos tres acciones que se usan bastante y que no aparecen en el material:

- `actions/cache`: guarda entre ejecuciones archivos que cambian poco, como las dependencias de un proyecto. Sirve para no descargarlas de nuevo en cada ejecución, así el workflow termina más rápido.
- `docker/build-push-action`: construye una imagen de Docker y la sube a un registro como Docker Hub o GitHub Container Registry. Sirve para dejar lista la imagen que después se va a desplegar.
- `github/codeql-action`: revisa el código mientras corre el workflow y busca problemas de seguridad. Sirve para detectar vulnerabilidades antes de que el cambio llegue a `main`.

Las tres se agregan con `uses:` en un step, igual que ya usamos `actions/checkout`.

### ¿Qué es un secreto en GitHub Actions y para qué se usa? ¿Cómo lo usarías en tu workflow?

Un secreto es un valor sensible, como una contraseña, un token o una API key, que se guarda cifrado en la configuración del repositorio y no dentro del código. Se usa para que el workflow pueda conectarse a otros servicios sin que esas credenciales queden visibles en el repositorio ni en los logs.

Los secretos se crean en Settings > Secrets and variables > Actions, y después se llaman con `${{ secrets.NOMBRE_DEL_SECRETO }}`. Por ejemplo, si tuviéramos que desplegar algo al final del workflow:

```yaml
- name: Desplegar
  env:
    TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  run: ./deploy.sh
```

GitHub muestra el valor como `***` en los logs. En nuestro workflow actual no usamos secretos porque solo imprimimos información, pero sería el siguiente paso si tuviéramos que desplegar o avisar a otro servicio.

### Reflexiona sobre el uso de GitHub Actions en tu flujo de trabajo diario. ¿Qué tareas automatizarías? ¿Por qué?

Estas son nuestras respuestas:

**Lina:** automatizaría las pruebas, sobre todo las automatizadas, las revisiones de seguridad, la búsqueda de vulnerabilidades, las validaciones de buenas prácticas y también el cumplimiento de los lineamientos de la empresa. Lo haría porque esas revisiones se repiten en cada cambio y, cuando se hacen a mano, es fácil saltarse alguna o hacerlas distinto cada vez.

**Alejo:** estoy de acuerdo con Lina y le agregaría la automatización dinámica de las tareas que le apliquen a una aplicación dentro de un pipeline o ciclo CI/CD, porque cada aplicación tiene necesidades distintas y así el pipeline se ajusta a lo que realmente necesita.

## Enlace ejecucion exitosa

https://github.com/alejoriosm04/entregable-1-cicd/actions/runs/42390234424



