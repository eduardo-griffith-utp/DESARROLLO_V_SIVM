# Frontend del Sistema de Identificación Visual Multimedia (SIVM)

Esta carpeta contiene la aplicación frontend del proyecto SIVM, responsable de la interfaz de usuario, captura/carga de imágenes y presentación de información multimedia.

## Tecnologías Utilizadas

- **Framework:** Ionic-Angular
- **Biblioteca UI:** Boostrap o Tailwind
- **Gestión de Estado:** NgRx
- **Routing:** Angular Router
- **Peticiones HTTP:** Postman o HttpClientModule 
- **Herramientas de Desarrollo:** Visual Studio Code, Git-GitHub

## Configuración del Entorno

### Requisitos Previos

Antes de empezar a trabajar con este proyecto, asegúrate de tener instalados los siguientes programas:

1. **Node.js** (Versión 20.19.0 o superior)
   - Puedes verificar la instalación de Node.js ejecutando:
     ```bash
     node -v
     ```

2. **NPM** (Versión 10.8.2 o superior)
   - Puedes verificar la instalación de NPM ejecutando:
     ```bash
     npm -v
     ```

3. **Ionic CLI** (Versión 7.2.1 o superior)
   - Para verificar la versión de Ionic CLI instalada, ejecuta:
     ```bash
     ionic -v
     ```

4. **Angular CLI** (Versión 19.2.6 o superior)
   - Verifica la versión de Angular CLI ejecutando:
     ```bash
     ng v
     ```

### Instalación
-  **NVM**: (Version 1.2.2 nvm-setup.exe)    https://github.com/coreybutler/nvm-windows/releases
1. **Node.js** 
     ```bash
     nvm install 20
     ```
2. **NPM** 
     ```bash
     npm install -g npm@10.8.2
     ```
3. **Ionic CLI** 
     ```bash
     npm install -g @ionic/cli@7.2.1
     ```
4. **Angular CLI** 
     ```bash
     npm install -g @angular/cli@19.2.6
     ```

### Ejecución
* Dirigirse a la carpeta frontend 
  ```bash
     cd frontend 
     ```

* Navegar al directorio del proyecto 
     ```bash
    cd app
     ```

* Instalar los modulos node
     ```bash
     npm install
     ```
* Ejecutar la aplicacion localmente 
     ```bash
     ionic serve
     ```
* Nota
     Si el terminal no tiene los permisos asignados, debe ejecutar powershell como administrador Error SecurityError PSSecurityException
     ```bash
          Set-ExecutionPolicy Unrestricted
     ```
## Convenciones de Código

- **Componentes:** Los componentes deben ser modulares y reutilizables, y su lógica debe estar claramente separada de la interfaz.
- **Estilos:** Tailwind o Boostrap
- **Nombres de archivos:** kebab-case
- **Organización de imports:**
    Los **imports** deben organizarse de la siguiente manera:
    1. **Angular imports**: Primero se deben importar los módulos estándar de Angular.
    2. **Terceros**: Luego, importar las bibliotecas de terceros como **NgRx**, **Ionic**, etc.
    3. **Componentes, servicios y módulos internos**: Finalmente, los módulos, servicios y componentes personalizados del proyecto.


## Guías de Estilo UI/UX

- [A completar por el equipo de Diseño UX/UI]

## Equipo de Frontend

- Jonathan Page
- Daniel Pimentel
- Isaac Pomares
- Arturo  Phillips

## Recursos Adicionales

- Documentación de Ionic: https://ionicframework.com/docs

- Documentación de Angular: https://angular.io/docs

- Documentación de NgRx: https://ngrx.io/docs

- Postman para pruebas de API: https://www.postman.com/