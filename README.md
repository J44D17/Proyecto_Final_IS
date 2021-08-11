# Proyecto_Final_IS
# Propósito del proyecto

El propósito del proyecto de presentación de eventos para la escuela de Ciencia de la Computación es implementar una página Web en donde los participantes de Ciencia de la computación puedan ver los distintos ventos próximos que se realizara.
Esta será capaz de dar información de donde ocurrirá dicho evento, el lugar del evento, información sobre el ponente, el tema a tratar y demás información relevante.
Otro de los propósitos para desarrollar esta página web es aplicar los siguientes conceptos aprendidos en clase de Ingeniería de software en el programa

- Estilos de Programación
- Principios SOLID
- Conceptos DDD


## Tipos de programación usados

En el proyecto usamos 3 estilos de programación:

### Programación Orientada a Objetos
Cuando generamos  el Módelo de dominio a partir del diseño de datos, usamos una extensión que permitió crear clases de cada uno de las entidades , en estas clases implementamos atributos y métodos que permitiran la interacción entre clases.

### Programación Modular
Python se caracteriza por trabajar con módulos, entonces al generarse los módelos tambien crea módulos que nos permitirá  trabajar con el código organizadamente, a continuación mostramos algunos de los módulos creados:

- actividad.py
- evento.py
- persona.py
- ponencia.py
- presentacion.py
- programa.py
- sesion.py
- tipoevento.py
- tipousuario.py
- topico.py

## Estilos de programación usados

### Espaciado en clases y funciones: 
La convención en Python indica que despues de cada clase o función se debe dejar por lo menos lineas de espaciado y luego continuar con el código siguiente.

### Indentación: 
A pesar de que Python obliga a usar una indentación, de lo contrario el código fallaría, se debe de usar 4 espacios por nivel de indentación

### Longitud máxima de líneas
Las guias de estilos en python indican que debe de haber una longitd máxima de caracteres por cas línea y es de 79 caracteres por línea.

## Patrones de Arquitectura
### Modelo Vista Controlador - Model View Template
![myimage-alt-tag](https://codigofacilito.com/photo_generales_store/29.jpg)

### Mockups desarrollados

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/mockup_8login.png)

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/mockup_9Reguistro.png)

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/mockup_11_Eventos_proximos.png)

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/mockup_13_eventos.png)

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/mockup_14_participacion.png)

### Interfaces

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/Captura_1.png)

![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/Inicio.png)

### Conceptos DDD aplicados

#### Ubiquitous Language
Es muy importante la comunicación enter el grupo para evitar problemas al desarrollar software, cuando teniamos que hacer el código y usar lenguaje en común , nos dividimos las partes para que no haya problema alguno, com módulos, funciones, templates, etc.

#### Entities
Claramente para desarrollar el diagrama tuvimos que realizar una abstracción .Sabemos que las entidades deben poder ser distinguidas de otros objetos aunque tengan los mismos atributos y que tienen que ser consideradas iguales a otros objetos aún cuando sus atributos difieren.

- actividad
- evento
- persona
- ponencia
- presentacion
- programa
- sesion
- tipoevento
- tipousuario
- topico
- 
![myimage-alt-tag](https://github.com/J44D17/Proyecto_Final_IS/blob/main/Imagenes/Screenshot_1.png)

# Principios SOLID
Es una serie de principios y bunas practicas  que permiten administrar la mayoría de los problemas de diseño de software conseguir el desarrollo de un código más limpio, más mantenible, más escalable a futuro y menos propenso a errores.
Los 3 principios usados son:
- O  Principio de Abierto-Cerrado
      que dice que el código debería estar abierto para extenderlo y para añadirle nuevas funcionalidades, pero en cambio debería estar cerrado a modificaciones, salvo las         modificaciones que se deban realizar si se encuentra algún error.
    
  







#### Values
En este caso sólo nos interesaron los atributos . Al contrario que las entidades sabemos que los value objects representan conceptos que no tienen identidad.

#### Infraestructure
En el documento de requisitos de software se especifican las decisiones tecnológicas que definimos
