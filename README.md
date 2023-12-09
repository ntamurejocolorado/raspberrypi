# Proyectos con Raspberry Pi

Este repositorio tiene código en Python, para interactuar con una placa [Raspberry Pi Zero 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/).

Los proyectos se clasificarán según el nivel de dificultad:

- Iniciacion
- Nivel Medio
- Nivel Avanzado

## Instalación

Para la instalación, seguimos las instrucciones de la página oficial de [Raspberry](https://www.raspberrypi.com/software/). 

La Raspberry Pi Zero 2W tiene una entrada para tarjetas microsd, en esta tarjeta se instala el sistema operativo elegido. Para ello, nos ayudamos de un adaptador de tarjetas sd a microsd, y la conectamos a nuestro ordenador.

En mi caso, instalé el sistema operativo [Raspberry Pi OS Lite de 64bit](https://www.raspberrypi.com/software/operating-systems/) sin escritorio porque quiero conectarme por SSH.

Trabajo con Fedora, aunque para la generación de la imagen, tuve que utilizar Windows porque tuve varios problemas. No obstante, desde el terminal podrías:
- Instalar el sistema operativo elegido.
- Crear el usuario y password.
- Conexión ssh

En mi caso, tuve problemas para que la raspberry apareciera dentro de los devices de mi red local cuando lo hacía con terminal.

## Conexión ssh 

En este caso, para la conexión ssh, utilizo Visual Studio Code.

[Pasos 1 y 2 SSH conexion VSCode](https://www.digitalocean.com/community/tutorials/how-to-use-visual-studio-code-for-remote-development-via-the-remote-ssh-plugin-es)

## Crear entorno virtual

Instalo pip y pyenv para crear entornos virtuales.
Creo el entorno virtual con

```
python3 -m venv myenv
```

Activamos el entorno virtual: 
```
source /myenv/bin/activate
```

Aqui instalar las dependencias/librerias necesarias.

## Links

- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [gpiozero](https://gpiozero.readthedocs.io/en/latest/)
- [micropython](https://micropython.org/)
- [instalacion](https://www.seeedstudio.com/blog/2021/01/25/three-methods-to-configure-raspberry-pi-wifi/)
- [Foro Raspberry](https://forums.raspberrypi.com/)
