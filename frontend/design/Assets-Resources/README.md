## El sistema de diseño (con enlaces a los archivos) 

- Pantalla de inicio/splash( imagen de carga) 

[ 1. Pantalla de Inicio splash ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/1.%20Pantalla%20de%20Inicio%20splash.pdf)

Elementos de interfaz con diseño finalizado 

Fondo: #FAFAFA (blanco suave), según guía de color. 

Logotipo: Logotipo oficial de VisioAI centrado, como elemento principal de identidad visual. 

Texto del nombre: “VisioAI” en fuente Poppins Bold, color #212121 (texto principal). 

Subtítulo: “Identificación Visual de Materiales” en Poppins Regular, color #757575 (texto secundario). 

Indicador de carga: Barra horizontal en la parte inferior de color gris claro, simulando el proceso de carga. 

Distribución centrada verticalmente: todo el contenido está alineado al centro de la pantalla para claridad visual. 

 

Navegación clara entre pantallas 

Esta pantalla es de presentación (splash): 

No tiene navegación interactiva. 

Su única función es presentar la marca mientras la app carga. 

Tras unos segundos (controlado por la lógica de la app), navegará automáticamente a la pantalla principal (dashboard). 

 

Estados de componentes (donde sea relevante) 

Barra de carga: aunque es estática en el wireframe, representa un estado animado que indica al usuario que la app está iniciando. 

(En diseño funcional, esta barra puede tener un efecto de progreso o animación de carga suave). 

 

 

Adaptaciones para diferentes tamaños de pantalla (responsive design) 

Versión móvil (vertical): Diseño optimizado para centrado en pantallas pequeñas. 

Versión tablet: El logo y los textos escalan proporcionalmente y mantienen el alineamiento vertical. 

Margen y paddings: Suficientes para evitar saturación en pantallas pequeñas, y bien distribuidos para pantallas más amplias. 

 

- Pantalla principal/dashboard 

[ 2. Pantalla principal ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/2.%20Pantalla%20principal.pdf)

 

Todos los elementos de interfaz con diseño finalizado 

Fondo: Color #FAFAFA (blanco suave), según la guía visual. 

Logo VisioAI: Centrado en la parte superior para mantener identidad visual consistente. 

 

Texto de bienvenida: 

Título: “¡Bienvenido!” – fuente Poppins Bold, tamaño H1 (1.6rem – 2rem), color #212121. 

Subtítulo: “Identifica materiales mediante imágenes” – fuente Poppins Regular, tamaño texto normal (1rem – 1.23rem), color #757575. 

 

Botón principal ("ESCANEAR"): 

 

Color de fondo: negro sólido #000000 

 

Texto blanco y en mayúsculas (fuente Poppins 0.85rem) 

Ícono integrado de cámara en blanco 

Bordes redondeados: border-radius: 1.23rem 

Sombra suave (representa estado normal) 

 

Navegación inferior (Bottom Nav Bar): 

Íconos: Inicio, Escanear (activo), Historial, Ajustes 

Etiquetas debajo de cada ícono 

Ícono activo: color magenta #E91E63 

Íconos inactivos: gris medio #757575 

 

 

Navegación clara entre pantallas 

Menú inferior: navegación intuitiva entre las 4 secciones: 

Inicio 

Escáner (pantalla activa actual) 

Historial 

Ajustes 

 

Botón "ESCANEAR": lleva a la pantalla de captura de imagen 

Iconos + etiquetas: apoyan el entendimiento visual del destino de cada sección 

 

Estados de componentes (donde sea relevante): 

 

Botón "ESCANEAR": 

Estado normal: fondo negro, ícono blanco, sombra leve 

Estado presionado (interacción): puede aplicar un fondo #1a1a1a con sombra interna 

Estado deshabilitado (si aplica en lógica): fondo gris oscuro #333333, texto gris claro, opacidad reducida 

 
Icono de navegación activo: color magenta (#E91E63) 

Iconos inactivos: gris (#757575) 

 

Adaptaciones para diferentes tamaños de pantalla (responsive design): 

 

Diseño vertical (móvil): todos los elementos se alinean al centro, con márgenes adecuados. 

 

Diseño para tablet: el logo, botones y textos escalan proporcionalmente y se conserva el espaciado entre elementos. 

 

Componentes táctiles grandes: botón principal y navegación inferior optimizados para accesibilidad en pantallas táctiles. 

 

 

- Pantalla de captura de imagen (para identificación) 

[ 3. Pantalla de captura de imagen (para identificacion) ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/3.%20Pantalla%20de%20captura%20de%20imagen%20(para%20identificacion).pdf)

Todos los elementos de interfaz con diseño finalizado: 

Encabezado con ícono de cámara y título "Capturar Imagen" 

Vista previa de la cámara ocupando la mayor parte de la pantalla 

Botón central de captura (color negro con borde magenta #E91E63, ícono de cámara blanca) 

Botón para cambiar cámara (frontal/trasera), ícono en la esquina superior derecha 

Botón de ayuda/información, ícono "?" en la parte superior izquierda 

Indicadores visuales de guía para centrar el objeto (líneas guía o marco) 

Feedback visual de carga o procesamiento posterior a la captura (círculo de progreso con animación suave) 

 

 

Navegación clara entre pantallas: 

Tras capturar la imagen, se navega automáticamente a la pantalla de resultados 

Flecha para regresar al dashboard desde el encabezado 

Barra de navegación inferior activa (ícono de escáner en color #E91E63, los demás en #757575) 

 

Estados de componentes: 

Botón de captura: 

Normal: ícono blanco, fondo negro 

Presionado: fondo más oscuro (#1a1a1a), sombra interna 

Deshabilitado: opacidad reducida, sin interacción 

Cámara no disponible o sin permisos: mensaje en texto secundario (#757575) con botón para reintentar 

Cambio de cámara: animación suave al invertir entre cámaras 

 

Adaptaciones para diferentes tamaños de pantalla (responsive design): 

En móviles: disposición vertical, botones centrados en la parte inferior 

En tablets: elementos redimensionados, mayor margen lateral, botones más separados 

Usabilidad táctil: áreas de toque grandes (>48px), botones centrados para fácil acceso con una mano 

Texto y botones: escalables según el tamaño del dispositivo sin perder legibilidad 

 

- Pantalla de resultados de identificación 

[4. Pantalla de Resultados de identificacion](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/4.%20Pantalla%20de%20Resultados%20de%20identificacion.pdf)

Todos los elementos de interfaz con diseño finalizado: 

Encabezado con título "Resultados de Identificación" y botón de retroceso (flecha) 

Lista de resultados identificados: 

Cada ítem tiene: 

Imagen miniatura del objeto identificado 

Nombre o etiqueta del objeto (texto principal, color #212121) 

Descripción breve o categoría (texto secundario, color #757575) 

Botón "Ver más" (botón pequeño con fondo blanco, borde magenta y texto negro) 

 

 

 

Botón principal "Capturar otra vez": 

Fondo negro #000000, texto blanco, bordes redondeados 

Alineado al centro inferior de la pantalla 

 

Separadores o tarjetas para cada resultado con sombra sutil y padding para claridad visual 

 

Navegación clara entre pantallas: 

 

Botón "Capturar otra vez" redirige a la Pantalla 3 (Captura de Imagen) 

Botón de retroceso (encabezado) regresa al dashboard o pantalla anterior 

Botón "Ver más" podría expandir la información del resultado o mostrar una nueva pantalla con detalles 

Navegación inferior visible, con ícono de escáner activo (#E91E63), los demás inactivos (#757575) 

 

Estados de componentes: 

 

Botón "Capturar otra vez": 

Normal: fondo negro, texto blanco 

Hover: sombra más pronunciada 

Presionado: tono más oscuro (#1a1a1a), sombra interna 

Deshabilitado (si aún no ha terminado la identificación): opacidad reducida 

 

Botones "Ver más": 

Activo: borde magenta (#E91E63), texto oscuro 

Presionado: leve oscurecimiento o sombra interna 

Estado vacío o sin resultados: 

Mensaje amigable con ícono informativo y botón para intentar nuevamente 

 

 

Adaptaciones para diferentes tamaños de pantalla (responsive design): 

Móviles: 

Lista de resultados en columna, scroll vertical fluido 

Botón "Capturar otra vez" fijo o flotante al fondo con suficiente separación 

 

 

Tablets: 

Resultados en grilla de 2 columnas (si el espacio lo permite) 

Botones de acción más grandes, mejor aprovechamiento del ancho 

 

 

General: 

Textos escalables según el tamaño de pantalla 

Cards ajustables con padding proporcional 

Touch targets grandes para accesibilidad 

 

- Pantalla: Resultado (post-escaneo) 

[5. Pantalla de detalle del elemento identificado ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/5.%20Pantalla%20de%20detalle%20del%20elemento%20identificado.pdf) 

Fondo: 

Color: #FAFAFA (blanco suave) 

 

Imagen del objeto 

Imagen centrada en un recuadro con bordes redondeados suaves y fondo gris muy claro (probablemente #F5F5F5) 

Espaciado adecuado alrededor de la imagen 

La imagen muestra el resultado de identificación (en este caso, una mochila azul con detalles marrones) 

 

Título del resultado 

Texto: “Mochila” 

Fuente: Poppins Bold 

Tamaño: Aproximadamente H2 (1.4rem – 1.6rem) 

Color: #212121 

Centrado debajo de la imagen 

 

Descripción del objeto 

Texto: 
 “una mochila de color azul con toques marrones, diseño clásico que cuenta con un compartimiento principal y un bolsillo frontal adicional” 

Fuente: Poppins Regular 

Tamaño: texto normal (1rem – 1.23rem) 

Color: #424242 o #212121 (tonalidad oscura para buena legibilidad) 

Justificado o centrado, ubicado dentro del mismo recuadro que la imagen 

 

Botón "Realizar otra vez" 

Texto: “Realizar otra vez” 

Fuente: Poppins Semibold o Medium 

Tamaño: 0.95rem – 1rem 

Texto en blanco 

Fondo: negro sólido #000000 

Bordes redondeados: border-radius: 1.23rem 

Padding amplio para accesibilidad táctil 

Centrado horizontalmente debajo del contenido 

Sombra leve para destacar el botón 

Estado presionado esperado: fondo #1a1a1a 

 

Barra de navegación inferior (Bottom Navigation) 

Fondo: blanco 

Íconos: 

Inicio (izquierda) 

Escanear (centro, activo) 

Historial 

Ajustes 

Ícono activo: Escanear 

Color: magenta #E91E63 

Íconos inactivos: gris medio #757575 

Etiquetas pequeñas debajo de cada ícono 

Íconos tocables con área amplia para interacción 

Diseño optimizado para usabilidad móvil 

 

 

- Pantalla de historial de identificaciones 

[6.1. Pantalla de historial de identificaciones ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/6.1.%20Pantalla%20de%20historial%20de%20identificaciones.pdf)

Imagen 1105881656, Imagen 

 

Pantalla: Historial 

Fondo: 

Color: #FAFAFA (blanco suave) 

 

Encabezado 

Texto: “Historial” 

Fuente: Poppins Bold 

Tamaño: H1 (aproximadamente 1.6rem – 2rem) 

Color: #212121 

Alineado a la izquierda 

Margen superior e inferior adecuados 

 

Filtros superiores 

Botones tipo “pill” (pastilla) para filtrado 

Opción activa: Todos 

Fondo: negro sólido #000000 

Texto: blanco, fuente Poppins Regular 

Opción inactiva: No identificados 

Fondo: blanco o transparente 

Borde fino gris claro 

Texto: color gris oscuro #757575 

Bordes redondeados (border-radius alto) 

Espaciado horizontal entre botones 

 

Lista de resultados históricos 

Cada ítem contiene: 

Imagen de miniatura 

A la izquierda, forma circular 

Tamaño uniforme (aproximadamente 40–50px) 

Imágenes recortadas al centro para mantener proporción 

Texto principal (título del objeto) 

Fuente: Poppins Semibold o Medium 

Tamaño: 1rem – 1.1rem 

Color: #212121 

Texto truncado si excede una línea 

Fecha relativa (por ejemplo: “1d”, “2d”) 

Tamaño pequeño (aprox. 0.85rem) 

Color: gris oscuro #757575 

Ubicado junto al título 

Descripción previa 

Fuente: Poppins Regular 

Tamaño: 0.95rem – 1rem 

Color: gris medio #757575 

Texto truncado con puntos suspensivos (…) 

Separador de ítems 

Línea divisoria muy delgada (probablemente #E0E0E0) entre cada resultado 

Indicador de no identificado 

Punto rojo pequeño al lado izquierdo del ítem correspondiente 

Se usa para destacar elementos con estado “no identificado” 

 

Barra de navegación inferior (Bottom Navigation) 

Fondo: blanco 

Íconos: 

Inicio 

Escanear 

Historial (activo) 

Ajustes 

Ícono activo: Historial 

Color: magenta #E91E63 

Íconos inactivos: gris medio #757575 

Etiquetas pequeñas debajo de cada ícono 

Íconos centrados y fácilmente tocables 

 

 

 

- Pantalla de Configuración  

[7.1. Pantalla de Configuración ](https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Pantallas%20de%20alta%20fidelidad/7.1.%20Pantalla%20de%20Configuraci%C3%B3n.pdf)

Imagen 1336012860, Imagen 

Pantalla: Configuración 

Fondo: 

Color: #FAFAFA (blanco suave) 

 

Encabezado 

Texto: “Configuración” 

Fuente: Poppins Bold 

Tamaño: H1 (aproximadamente 1.6rem – 2rem) 

Color: #212121 

Centrado horizontalmente 

Icono de flecha hacia atrás alineado a la izquierda para navegación 

 

Opciones de configuración 

Cada fila tiene los siguientes elementos: 

Estructura general 

Contenedor con altura estándar para accesibilidad (mínimo 56px) 

Fondo blanco individual por fila 

División sutil entre elementos (líneas divisorias finas en color #E0E0E0) 

Íconos alineados a la izquierda 

Texto principal y texto auxiliar alineados verticalmente 

 

Opción: Lenguaje 

Ícono: globo (idioma) 

Título: Lenguaje 

Texto secundario: “seleccionar el tipo de lenguaje” 

Fuente: Poppins Regular 

Tamaño: aproximadamente 1rem 

Color: texto principal #212121, texto auxiliar #757575 

Indicador de navegación: flecha hacia la derecha (>) 

 

Opción: Notificaciones 

Ícono: campana 

Título: Notificaciones 

Componente: interruptor (switch) 

Switch activado: color verde brillante (iOS-style) 

Texto y diseño alineados a la izquierda, switch a la derecha 

 

Opción: Escaneo automático 

Ícono: cámara o escáner 

Título: Escaneo automático 

Switch activado: color verde brillante 

Misma disposición que la opción anterior 

 

Opción: Tema oscuro 

Ícono: sol/luna 

Título: Tema oscuro 

Switch desactivado: fondo gris claro 

El texto permanece en color oscuro para mantener visibilidad en modo claro 

 

Opción: Privacidad 

Ícono: candado 

Título: Privacidad 

Texto auxiliar: “ajustes de privacidad” 

Flecha hacia la derecha para indicar navegación 

Estilo igual a la fila de “Lenguaje” 

 

Accesibilidad y diseño adaptable 

Tamaño y separación de los ítems optimizados para interacción táctil 

Texto legible con contraste suficiente 

Compatible con navegación por voz o lectores de pantalla 

Adaptado a pantallas móviles (diseño vertical) 

Preparado para escalar a pantalla de tablet manteniendo márgenes y disposición 

 

Navegación inferior (Bottom Navigation) 

Visible y fija en la parte inferior 

Ícono activo: Ajustes 

Color: magenta #E91E63 

Íconos inactivos: gris medio #757575 

Etiquetas debajo de cada ícono 

Fondo blanco 

Interactividad clara con zonas táctiles amplias 

 

## La estructura de navegación 

https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/features/laboratorio-4-ui/frontend/design/Assets-Resources/Estructura%20de%20Navegacion/Flujo%20Visual%20de%20la%20estructura%20de%20navegacion.png 


## Decisiones de diseño importantes 

- Decisiones de diseño importantes para las pantallas de VisioAI 


- Diseño simple y fácil de usar: 

Queríamos que la aplicación fuera clara desde el primer momento. Por eso, cada pantalla muestra solo lo necesario, con un estilo limpio, sin cosas que distraigan. Así, el usuario puede enfocarse en lo que realmente importa: identificar elementos con la cámara. 

 
- Colores que guían al usuario 

Usamos colores bien pensados: 

El rosa fuerte (#E91E63) destaca lo más importante: botones, iconos activos, acciones clave. 

El morado (#9C27B0) acompaña sin quitar protagonismo. 

Grises para los textos, con buen contraste para que se lean bien. 

Esto ayuda a que el usuario sepa rápidamente qué puede tocar y qué está viendo. 

- Navegación que se entiende sola: 

Agregamos una barra con íconos y nombres en la parte de abajo, para que el usuario sepa dónde está y cómo moverse sin perderse. El icono que esté activo cambia de color para que sea muy evidente en qué parte de la app está. 

- Cada pantalla tiene un propósito 

No quisimos hacer pantallas confusas. Cada una tiene una función clara: 

Capturar imagen 

Ver resultados 

Revisar detalles 

Ver historial, etc. 

Esto evita confusión y ayuda a que la persona complete lo que vino a hacer sin dar vueltas innecesarias. 

- Botones grandes y fáciles de tocar: 

Todos los botones son cómodos para usar con el dedo. Además, cambian de apariencia cuando están activos, deshabilitados o presionados, para que el usuario siempre sepa si están disponibles o no. 

- Se adapta a diferentes pantallas: 

La app está pensada para que funcione bien tanto en celulares como en tablets. Todo se ajusta para que no se vea apretado ni desordenado, sin importar el tamaño de la pantalla. 

Flujo natural entre pantallas: Después de tomar una foto, se ve el resultado. Si no es lo que se esperaba, se puede volver a capturar fácilmente. Todo fluye sin interrupciones, para que el usuario no se pierda y pueda usar la app sin complicaciones. 

## Enlaces al prototipo interactivo 

https://www.figma.com/proto/uWHAEIvNdkl8BlV4baSFiU/Untitled--Copia-?node-id=2003-2&p=f&t=4q9JrNOjQZJt4OE8-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=2003%3A2  