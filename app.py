from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# -----------------------------------------
# 1. CONFIGURACIÓN DE LA BASE DE DATOS
# -----------------------------------------
# Le decimos a Flask que use SQLite y que el archivo se llamará "universidad.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///universidad.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos
db = SQLAlchemy(app)

# -----------------------------------------
# 2. DEFINIR EL MODELO (La Tabla)
# -----------------------------------------
# Esto define cómo se verá nuestra tabla en la base de datos
class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)

    # Una función de ayuda para convertir el objeto a un diccionario (JSON)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "carrera": self.carrera,
            "semestre": self.semestre
        }

# Crear la base de datos y las tablas automáticamente si no existen
with app.app_context():
    db.create_all()

# -----------------------------------------
# 3. ENDPOINT: POST /estudiantes (Crear)
# -----------------------------------------
@app.route('/estudiantes', methods=['POST'])
def registrar_estudiante():
    datos = request.json
    
    # Validar que nos envíen todos los datos
    if not datos or 'nombre' not in datos or 'carrera' not in datos or 'semestre' not in datos:
        return jsonify({"error": "Faltan datos obligatorios (nombre, carrera, semestre)"}), 400
    
    # Crear un nuevo objeto Estudiante
    nuevo_estudiante = Estudiante(
        nombre=datos['nombre'],
        carrera=datos['carrera'],
        semestre=datos['semestre']
    )
    
    # Guardarlo en la base de datos
    db.session.add(nuevo_estudiante)
    db.session.commit() # Confirma los cambios
    
    return jsonify({"mensaje": "Estudiante registrado exitosamente", "estudiante": nuevo_estudiante.to_dict()}), 201

# -----------------------------------------
# 4. ENDPOINT: GET /estudiantes (Consultar)
# -----------------------------------------
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    # Consultar todos los registros en la tabla Estudiante
    estudiantes_db = Estudiante.query.all()
    
    # Convertir la lista de objetos a una lista de diccionarios
    lista_estudiantes = [estudiante.to_dict() for estudiante in estudiantes_db]
    
    return jsonify(lista_estudiantes), 200

# -----------------------------------------
# INICIAR EL SERVIDOR
# -----------------------------------------
if __name__ == '__main__':
    app.run(debug=True)