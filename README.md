# Módulo de gestión de tickets de soporte

Este módulo permite gestionar tickets de soporte en Odoo. Se pueden crear tickets con los siguientes campos:
- **Nombre del ticket**: Para ayudar al usuario a saber qué ticket es.
- **Cliente**: Cliente asociado al ticket.
- **Estado**: Puede ser "nuevo", "en progreso" o "resuelto".
- **Descripción**: Una descripción complementaria al nombre por si necesita más información.
- **Fecha de creación**: Se rellena automáticamente con la fecha del momento en que se crea el ticket.
- **Usuario asignado**: Usuario asociado al ticket.

### Características especiales

El módulo contiene un botón para cambiar el estado del ticket. Si el estado es "nuevo" permite marcarlo como "en progreso" y si el estado es "en progreso", permite marcarlo como "resuelto".

## Instrucciones de instalación con docker

### **1. Prerequisitos**
Tener docker instalado.

### **2. Descargar el repositorio**
Se puede clonar también con alguno de estos comandos:

- Si tienes SSH:

`git clone https://github.com/Nico-Pardo-Medina/Odoo_test.git`
  
- Si no:

`git clone git@github.com:Nico-Pardo-Medina/Odoo_test.git`

### **3. Navegar a la carpeta del repositorio**
Se puede hacer con este comando:

`cd <carpeta-del-repositorio>`

### **4. Iniciar Odoo con el archivo docker compose**
En la carpeta raíz del repositorio donde se encuentra el archivo 'docker-compose.yml' escribe el siguiente comando:

`docker-compose up -d`

### **5. Acceder a Odoo con el navegador**
Abre un navegador y escribe la siguiente URL:

`http://localhost:8069`

### **6. Buscar el módulo e instalarlo**
Ve a la pestaña aplicaciones de Odoo y busca Helpdesk tickets, puedes usar el buscador para ello. Haz clic en instalar.

## Instrucciones de instalación para agregar el módulo a tu odoo
Si ya tienes Odoo funcionando sin Docker puedes seguir estos pasos:

### **1. Descargar el módulo**
Descarga o clona el módulo y colócalo en la carpeta  `addons` de tu Odoo.

### **2. Actualizar lista de aplicaciones de Odoo**
En la pestaña de aplicaciones de Odoo haz clic en "Actualizar lista de aplicaciones" ("Update Apps List" en inglés).

### **3. Instalar el módulo**
Busca el módulo helpdesk tickets y haz clic en instalar.

## Instrucciones de uso para crear un ticket nuevo

En la vista de lista se verán los tickets existentes. Se puede crear uno nuevo pulsando el botón "Nuevo" ("New" en inglés) y rellenando todos los campos.

## Para modificar un ticket existente

Haz clic en uno de los tickets y modifica el campo que desees. Para modificar el estado debes pulsar en el botón correspondiente.
