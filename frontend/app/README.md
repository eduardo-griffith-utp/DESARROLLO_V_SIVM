# Frontend - Sistema de Identificación Visual Multimedia (SIVM)

Este archivo **README.md** proporciona una descripción general de la **estructura del proyecto** en el directorio `frontend/`, detallando las principales carpetas y archivos, y proporcionando directrices sobre cómo **añadir nuevos componentes** o **funcionalidades** al sistema.

---

## Estructura General del Proyecto

La estructura de carpetas está organizada de manera **modular y clara**, lo que facilita la reutilización de componentes y la escalabilidad del código. A continuación se describe la estructura de carpetas recomendada para este proyecto:

```plaintext
frontend/
├── app/
│   ├── core/                  # Servicios y funcionalidades centrales
│   │   ├── services/          # Servicios compartidos (API, almacenamiento, etc.)
│   │   ├── guards/            # Guards para rutas (si aplica)
│   │   ├── interceptors/      # Interceptores HTTP (si aplica)
│   │   └── models/            # Interfaces y tipos globales
│   ├── shared/                # Elementos compartidos en toda la app
│   │   ├── components/        # Componentes reutilizables
│   │   ├── directives/        # Directivas personalizadas
│   │   ├── pipes/             # Pipes personalizados
│   │   └── utils/             # Utilidades y helpers
│   ├── pages/                 # Páginas de la aplicación
│   │   ├── home/              # Página de inicio
│   │   ├── image-capture/     # Página de captura de imagen
│   │   ├── recognition-results/ # Página de resultados
│   │   └── item-details/      # Página de detalle del item
│   ├── theme/                 # Estilos globales y variables
│   │   ├── variables.scss     # Variables globales
│   │   └── global.scss        # Estilos globales
│   ├── app-routing.module.ts  # Configuración de rutas principal
│   ├── app.module.ts          # Módulo principal de la app
│   ├── assets/                # Recursos estáticos
│   │   ├── icons/             # Iconos
│   │   └── shapes.svg         # Otras imágenes
│   ├── environments/          # Configuraciones por entorno
│   │   ├── environment.prod.ts# Configuración para producción
│   │   └── environment.ts     # Configuración para desarrollo
│   ├── global.scss            # Estilos globales
│   ├── index.html             # HTML principal
│   ├── main.ts                # Entrada principal
│   ├── polyfills.ts           # Compatibilidad para navegadores
│   ├── test.ts                # Configuración para pruebas
│   └── zone-flags.ts          # Configuración de zona
├── .browserslistrc            # Configuración de navegadores soportados
├── .editorconfig              # Configuración de editor
├── .eslintrc.json             # Configuración de ESLint
├── .gitignore                 # Archivos ignorados por Git
├── angular.json               # Configuración de Angular CLI
├── capacitor.config.ts        # Configuración de Capacitor
├── ionic.config.json          # Configuración de Ionic
├── karma.conf.js             # Configuración de Karma para pruebas
├── package-lock.json          # Bloqueo de versiones de paquetes
├── package.json               # Configuración de NPM
├── README.md                  # Documentación del proyecto
├── tsconfig.app.json          # Configuración de TypeScript para la app
├── tsconfig.json              # Configuración de TypeScript
└── tsconfig.spec.json         # Configuración de TypeScript para pruebas
```

---

## Propósito de las Principales Carpetas y Componentes

### 1. **`core/`**
   Contiene los **servicios centrales** que gestionan la lógica de la aplicación, como llamadas a APIs, autenticación, almacenamiento y más. También incluye **guards** para controlar el acceso a las rutas, **interceptores HTTP** y **modelos** para definir interfaces y tipos globales.

### 2. **`shared/`**
   Esta carpeta alberga **elementos reutilizables** que pueden ser utilizados en diferentes partes de la aplicación:
   - **Componentes reutilizables** como botones, formularios, tarjetas, etc.
   - **Directivas personalizadas** para manipular el DOM de forma específica.
   - **Pipes personalizados** para transformar datos en la vista (fechas, monedas, etc.).
   - **Utilidades y helpers** con funciones generales para el proyecto.

### 3. **`pages/`**
   Aquí se encuentran las **páginas principales** de la aplicación, cada una con su propio componente. Las páginas se agrupan por funcionalidad y cada una tiene su lógica, plantilla y estilos asociados:
   - **`home/`**: Página de inicio.
   - **`image-capture/`**: Página para capturar imágenes.
   - **`recognition-results/`**: Página para mostrar los resultados del reconocimiento.
   - **`item-details/`**: Página para ver el detalle de un item.

### 4. **`theme/`**
   Contiene los **estilos globales** y las **variables** que definen la apariencia general de la aplicación. Este es el lugar donde se configuran los colores, tipografía, márgenes y otros estilos globales.

### 5. **`assets/`**
   Aquí se almacenan los **archivos estáticos** como imágenes e iconos que se utilizan en la aplicación. Estos archivos pueden ser referenciados desde cualquier lugar de la app.

### 6. **`environments/`**
   Contiene los archivos de configuración que definen los entornos de desarrollo y producción. Aquí se gestionan las variables de entorno para cada uno.

### 7. **`app.module.ts`**
   Es el **módulo raíz** de la aplicación donde se importan los módulos necesarios y se definen las rutas, componentes y dependencias de la aplicación.

---

## Guía para Añadir Nuevos Componentes o Funcionalidades

### Para **Páginas** y **Componentes**:

1. **Crear un nuevo componente**:
   Utiliza el comando de Angular CLI para generar un nuevo componente:
   ```bash
   ng generate component pages/new-page
   ```
   Esto creará los siguientes archivos:
   - `new-page.component.ts`: Lógica del componente.
   - `new-page.component.html`: Plantilla HTML del componente.
   - `new-page.component.scss`: Estilos específicos.
   - `new-page.component.spec.ts`: Pruebas (opcional, pero recomendado).

2. **Organización de archivos**:
   - Los **componentes** deben ser modulares y reutilizables.
   - Los **nombres de archivos** deben seguir el formato `kebab-case`.

3. **Añadir nuevas funcionalidades**:
   Si estás añadiendo nuevas **funcionalidades de servicio**, utiliza el siguiente comando para crear un servicio:
   ```bash
   ng generate service core/services/new-service
   ```

4. **Configurar rutas**:
   - Para configurar rutas, abre el archivo `app-routing.module.ts` y añade la nueva ruta para la página o componente.

5. **Declarar NgModule la pagina**:
   - para declarar como dependiente de NgModule, abre el archivo `nombre.page.ts` y declara dentro del componente como dependiente `standalone: false`.
   
### Para **Servicios**:

1. **Crear un nuevo servicio**:
   Utiliza el siguiente comando:
   ```bash
   ng generate service core/services/new-service
   ```

2. **Agregar lógica al servicio**:
   Los servicios deben encargarse de la **gestión de datos** (llamadas a API, almacenamiento local, etc.).

3. **Pruebas**:
   Añadir pruebas unitarias para asegurarte de que el servicio funciona correctamente.

---

## Convenciones de Código

- **Modularidad**: Cada componente y servicio debe ser independiente y reutilizable.
- **Nombres de archivos**: Utiliza **kebab-case** para los nombres de archivos.
- **Imports**: Los imports deben organizarse de la siguiente manera:
  - **Angular imports**: Primero los imports de Angular.
  - **Terceros**: Luego los imports de librerías de terceros (NgRx, Ionic).
  - **Componentes, servicios y módulos internos**: Finalmente, los imports internos del proyecto.

---

## Recursos Adicionales

- [Documentación de Ionic](https://ionicframework.com/docs)
- [Documentación de Angular](https://angular.io/docs)
- [Documentación de NgRx](https://ngrx.io/docs)
- [Postman para pruebas de API](https://www.postman.com/)
