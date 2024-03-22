import pandas as pd
import numpy as np

# Definir los departamentos
departamentos_data = {
 "Departamento_id": ["1", "2", "3"],
 "Departamento": ["TI", "Marketing", "RRHH"]
}

# Definir los Jobs o cargos 
jobs_data = {
 "job_id": ["101", "102", "201", "202", "301", "302"],
 "cargo": ["Analista desarrollo", "Lider tecnico desarrollo", 
           "Community manager", "Gerente de marca",
           "Director de recursos humanos", "Tecnico de seleccion"]
}

# Empleados
np.random.seed(0)
empleados_data = {
 "empleado_id": np.arange(1, 101),
 "Nombre_Empleado": [f"Nombre {i}" for i in range(1, 101)],
 "job_id": np.random.choice(["101", "102", "201", "202", "301", "302"],100)
 }

# Conversion a dataframe
departamentos_df = pd.DataFrame(departamentos_data)
jobs_df = pd.DataFrame(jobs_data)
empleados_df = pd.DataFrame(empleados_data)

empleados_df["Departamento_id"] = empleados_df["job_id"].str[0]

#impresiones
print("Departamentos DataFrame:")
print(departamentos_df)

print("\nCargos DataFrame:")
print(jobs_df)

print("\nEmpleados DataFrame:")
print(empleados_df)

#Exportando los datos a csv
departamentos_df.to_csv("./datasets/departamentos.csv",index=False)
jobs_df.to_csv("./datasets/cargos.csv",index=False)
empleados_df.to_csv("./datasets/empleados.csv",index=False)

###inyeccion de los datos
import pyodbc

connection_string = 'Driver={SQL Server};Server=tcp:empresa1.database.windows.net,1433;Database=Empresa 1;Uid=adminsql;Pwd=pass.;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;'

connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

###Insertar Jobs o cargos
insert_query = """INSERT INTO cargos (job_id, cargo) VALUES (?, ?)"""

for index, row in jobs_df.iterrows():
    job_id = row['job_id']
    cargo = row['cargo']
    cursor.execute(insert_query, (job_id, cargo))


###Insertar Departamentos
insert_query = """INSERT INTO departamentos (Departamento_id, Departamento) VALUES (?, ?)"""

for index, row in departamentos_df.iterrows():
    Departamento_id = row['Departamento_id']
    Departamento = row['Departamento']
    cursor.execute(insert_query, (Departamento_id, Departamento))

###Insertar Empleados
insert_query = """INSERT INTO empleados (empleado_id, Nombre_Empleado, job_id, Departamento_id) VALUES (?, ?, ?, ?)"""

for index, row in empleados_df.iterrows():
    empleado_id = row['empleado_id']
    Nombre_Empleado = row['Nombre_Empleado']
    job_id = row['job_id']
    Departamento_id = row['Departamento_id']

    cursor.execute(insert_query, (empleado_id, Nombre_Empleado, job_id, Departamento_id))

### Cerrar la conexion para evitar el consumo de recursos
connection.commit()
cursor.close()
connection.close()
