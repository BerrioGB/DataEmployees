import pandas as pd
import numpy as np
# Course Categories Data
departamentos_data = {
 "Departamento_id": ["1", "2", "3"],
 "Departamento": ["TI", "Marketing", "RRHH"]
}
# Course Levels Data
jobs_data = {
 "job_id": ["101", "102", "201", "202", "301", "302"],
 "cargo": ["Analista desarrollo", "Lider tecnico desarrollo", 
           "Community manager", "Gerente de marca",
           "Director de recursos humanos", "Tecnico de seleccion"]
}


# Courses Data
np.random.seed(0)
empleados_data = {
 "empleado_id": np.arange(1, 101),
 "Nombre_Empleado": [f"Nombre {i}" for i in range(1, 101)],
 "job_id": np.random.choice(["101", "102", "201", "202", "301", "302"],100)
 }

 #"departamento_id": np.random.choice([1, 2, 3], 100),

# Convert to DataFrame
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

#Exportando los datos a csv, debido a que csv es el formato mas reconocido mundialmente y es mas accesible para trabajar con bajos volumenes de datos
departamentos_df.to_csv("./datasets/departamentos.csv",index=False)
jobs_df.to_csv("./datasets/cargos.csv",index=False)
empleados_df.to_csv("./datasets/empleados.csv",index=False)