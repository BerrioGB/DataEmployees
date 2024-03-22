import pyodbc
connection_string = 'Driver={SQL Server};Server=tcp:empresa1.database.windows.net,1433;Database=Empresa 1;Uid=adminsql;Pwd=Gomezio23.;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

###Query para crear la tabla cargos

query = f"""
CREATE TABLE cargos (
    job_id VARCHAR(50) PRIMARY KEY,
    cargo VARCHAR(50)
);
"""

cursor.execute(query)
connection.commit()  

###Query para crear la tabla departamentos

query_departamentos = f"""
CREATE TABLE departamentos (
    Departamento_id VARCHAR(50) PRIMARY KEY,
    Departamento VARCHAR(50)
);
"""
cursor.execute(query_departamentos)
connection.commit()  

###Query para crear la tabla empleados

query_empleados = f"""
CREATE TABLE empleados (
    empleado_id VARCHAR(50) PRIMARY KEY,
    Nombre_Empleado VARCHAR(50),
    job_id VARCHAR(50),
    Departamento_id VARCHAR(50)

);
"""
cursor.execute(query_empleados)
connection.commit() 

connection.close()
