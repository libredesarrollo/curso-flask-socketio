# Curso Flask-SocketIO

Repositorio de una aplicación de ejemplo para aprender a usar **Flask** junto con **SocketIO** para construir aplicaciones web en tiempo real.

---

## Descripción

Este proyecto es una aplicación web de chat en tiempo real que demuestra la integración entre el framework Flask y la librería Flask-SocketIO.

Las características principales incluyen:
- Envío y recepción de mensajes en tiempo real sin recargar la página.
- Rutas HTTP convencionales para la estructura básica de la web.
- Persistencia de datos de mensajes o usuarios usando una base de datos.
- Gestión de la base de datos a través de migraciones.

---

## Tecnologías

- **Backend**: Python 3, Flask, Flask-SocketIO
- **Base de Datos**: SQLAlchemy, Flask-Migrate
- **Frontend**: HTML5, JavaScript, Socket.IO Client, Jinja2

---

## Requisitos

- Python 3.8+
- pip
- Un entorno virtual (recomendado)

---

## Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Uso

1.  **Aplica las migraciones de la base de datos (si es la primera vez):**
    ```bash
    flask db upgrade
    o
    python -m flask --app run db upgrade
    ```

2.  **Inicia la aplicación:**
    ```bash
    flask run
    o
    python -m flask --app run
    ```

3.  Abre tu navegador y ve a `http://127.0.0.1:5000`.

---

## Estructura del proyecto
