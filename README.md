# QA Automation Project - SauceDemo

Proyecto de automatización web desarrollado con Python, Selenium WebDriver y Pytest utilizando el sitio de práctica:

https://www.saucedemo.com/

----------------------------------------------------------

## 📌 Propósito del Proyecto

El objetivo de este proyecto es automatizar flujos básicos de navegación web y validaciones funcionales utilizando herramientas de automatización QA.

El proyecto incluye:

- Automatización de login
- Validación de catálogo de productos
- Interacción con carrito de compras
- Uso de esperas explícitas
- Generación de reportes HTML
- Organización modular del código

----------------------------------------------------------

## 🚀 Tecnologías Utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Git & GitHub
- Visual Studio Code

----------------------------------------------------------

## 🧪 Casos de Prueba Automatizados

1. Login Exitoso 💻
Validaciones:
Navegación a SauceDemo
Ingreso de credenciales válidas
Espera explícita hasta redirección
Validación de /inventory.html
Validación de título "Swag Labs"
Validación de texto "Products"
Credenciales utilizadas:
Usuario: standard_user
Contraseña: secret_sauce

2. Navegación y Verificación del Catálogo 📋
Validaciones:
Verificación del título de inventario
Validación de productos visibles
Validación de elementos importantes:
menú lateral
filtro de productos
Obtención de:
nombre del primer producto
precio del primer producto

3. Interacción con Carrito de Compras 🛒
Validaciones:
Agregar primer producto al carrito
Verificar incremento del contador
Navegar al carrito
Verificar presencia correcta del producto agregado

----------------------------------------------------------

## ⚙️ Instalación del Proyecto
1. Clonar el repositorio:
git clone <url-del-repositorio>

2. Crear entorno virtual:
python -m venv .venv

3. Activar entorno virtual
Windows PowerShell:
.\.venv\Scripts\Activate.ps1

4. Instalar dependencias
python -m pip install -r requirements.txt

----------------------------------------------------------

## ▶️ Ejecución de Tests:
Ejecutar todos los casos de prueba:
pytest -v

----------------------------------------------------------

## 📊 Generación de Reporte HTML:
pytest --html=reporte.html --self-contained-html

El reporte se genera automáticamente en la raíz del proyecto.

----------------------------------------------------------

## 📌Objetivo Académico:

Este proyecto fue desarrollado como práctica de automatización QA para reforzar conocimientos en:
-Selenium WebDriver
-Testing automatizado
-Automatización funcional web
-Estructuración de proyectos QA
-Manejo de Git y GitHub
-Uso de Pytest y fixtures

----------------------------------------------------------

### 👩‍💻 Autor
Maria R. Narvaez

Estudiante de QA Automation.



