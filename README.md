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

### ¿Qué es un secreto en GitHub Actions y para qué se usa? ¿Cómo lo usarías en tu workflow?

### Reflexiona sobre el uso de GitHub Actions en tu flujo de trabajo diario. ¿Qué tareas automatizarías? ¿Por qué?

## Enlace ejecucion exitosa

https://github.com/alejoriosm04/entregable-1-cicd/actions/runs/42390234424



