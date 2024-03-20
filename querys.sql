/*Consulta que muestra el nombre del empleado, su cargo y el departamento al que pertenece*/
SELECT
	E.Nombre_Empleado,
	C.cargo,
    D.Departamento
FROM empleados AS E
JOIN departamentos AS D
ON E.departamento_id = D.departamento_id
JOIN cargos as C
ON E.job_id = C.job_id;
GO

/*Consulta que muestra todos los datos de todas las tablas*/
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
ON E.job_id = C.job_id;
GO

/*Consulta que muestra solo los id de todas las tablas*/
SELECT
	E.empleado_id,
	C.job_id,
    D.Departamento_id
FROM empleados AS E
JOIN departamentos AS D
ON E.departamento_id = D.departamento_id
JOIN cargos as C
ON E.job_id = C.job_id;
GO
