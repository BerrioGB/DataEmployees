from collections import OrderedDict
from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)


#Conexion a la base de datos

connection_string = 'Driver={SQL Server};Server=tcp:empresa1.database.windows.net,1433;Database=Empresa 1;Uid=adminsql;Pwd=Gomezio23.;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

#Ruta Principal: Consulta core que trae todos los campos de todas las tablas en la BD
@app.route('/')
def root():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
            SELECT
                E.empleado_id,
                E.Nombre_Empleado,
                C.job_id,
                C.cargo,
                D.Departamento_id,
                D.Departamento
            FROM empleados AS E
            JOIN departamentos AS D
            ON E.departamento_id = D.departamento_id
            JOIN cargos as C
            ON E.job_id = C.job_id
        """

        cursor.execute(query)
        rows = cursor.fetchall()

#La data que se recibe se convierte en diccionario
        data = []
        for row in rows:
            new_dict = {
                'empleado_id': row[0],
                'Nombre_Empleado': row[1],
                'job_id': row[2],
                'cargo': row[3],
                'Departamento_id': row[4],
                'Departamento': row[5]
            }

            data.append(new_dict)

        return jsonify(data)

    except pyodbc.Error as ex:
        print("Database connection error:", ex)
        return jsonify({'error': 'Error connecting to database'}), 500  

    finally:
        if conn:
            conn.close()

#Ruta de empleadoas que trae solo los nombres del empleado, cargo y departamento
@app.route('/empleados')
def get_empleados():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
            SELECT
                E.Nombre_Empleado,
                C.cargo,
                D.Departamento
            FROM empleados AS E
            JOIN departamentos AS D
            ON E.departamento_id = D.departamento_id
            JOIN cargos as C
            ON E.job_id = C.job_id
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        data = [{'Nombre_Empleado': row[0], 'Cargo': row[1], 'Departamento': row[2]} for row in rows]

        return jsonify(data)

    except pyodbc.Error as ex:
        print("Database connection error:", ex)
        return jsonify({'error': 'Error connecting to database'}), 500  

    finally:
        if conn:
            conn.close()

#Ruta de ids que trae los ids de las tres tablas
@app.route('/ids')
def get_ids():
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        query = """
            SELECT
                E.empleado_id,
                C.job_id,
                D.Departamento_id
            FROM empleados AS E
            JOIN departamentos AS D
            ON E.departamento_id = D.departamento_id
            JOIN cargos as C
            ON E.job_id = C.job_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        data = [{'empleado_id': row[0], 'job_id': row[1], 'Departamento_id': row[2]} for row in rows]

        return jsonify(data)

    except pyodbc.Error as ex:
        print("Database connection error:", ex)
        return jsonify({'error': 'Error connecting to database'}), 500  # Internal server error

#bloque para asegurarnos de cerrar la conexion a la base de datos
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)