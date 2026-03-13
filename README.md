# API de Registro de Estudiantes - Flask & SQLite

Este proyecto es una API RESTful desarrollada con Python y Flask que permite registrar y consultar estudiantes en una base de datos local SQLite utilizando SQLAlchemy.

## 📌 Evidencias de Ejecución (Postman)

A continuación se muestran las pruebas de funcionamiento de los endpoints solicitados, ejecutadas a través de Postman.

### 1. Creación de un registro (POST `/estudiantes`)
Se envía un objeto JSON con los datos del estudiante (nombre, carrera y semestre). La API lo guarda en la base de datos y retorna un código `201 Created`.

![Evidencia POST Estudiantes](ruta/a/tu/captura_post_aqui.png)
<img width="904" height="921" alt="image" src="https://github.com/user-attachments/assets/e9669e04-d499-4620-b8ff-6d00288dac5f" />


### 2. Consulta de registros (GET `/estudiantes`)
Se realiza una petición GET para obtener todos los estudiantes almacenados en la base de datos SQLite. La API retorna una lista en formato JSON con un código `200 OK`.



---

## 🧠 Comentario de Aprendizaje

**¿Qué aprendí en este ejercicio?**
A través de la implementación de esta API, aprendí a conectar el microframework Flask con una base de datos real utilizando SQLAlchemy como ORM (Object-Relational Mapping). Esto me permitió entender cómo traducir modelos de Python directamente a tablas de una base de datos SQLite sin necesidad de escribir sentencias SQL manualmente. 

Además, reforcé mis conocimientos sobre la creación de endpoints, comprendiendo el flujo completo: desde recibir un *payload* en formato JSON a través de una petición POST para persistir datos (almacenamiento), hasta consultar la base de datos mediante una petición GET para devolver esos registros al cliente. Finalmente, logré validar todo el ciclo de vida de los datos utilizando Postman.

---

## 🚀 Cómo ejecutar este proyecto localmente

1. Clonar el repositorio.
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   Instalar las dependencias:

Bash
pip install Flask Flask-SQLAlchemy
Ejecutar el servidor:

Bash
python app.py
El servidor se iniciará en http://127.0.0.1:5000 y creará automáticamente el archivo de la base de datos universidad.db.
