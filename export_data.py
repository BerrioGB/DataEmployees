from azure.storage.blob import BlobServiceClient, BlobClient

# Credenciales y nombre del contenedor
connection_string = "DefaultEndpointsProtocol=https;AccountName=empleados;AccountKey=EPv5yuQqWRdfBT6OvC6h5f54PgCdPaok3S6dbfET3h2cIxDQfA6Uk6ZVaX7bKHO8g6S8iJ1d6jdr+ASt/JaQWw==;EndpointSuffix=core.windows.net"
container_name = "empleadoscontainer"

# Crear BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Cargar archivo CSV 
archivos_csv = ["create_data/datasets/cargos.csv", "create_data/datasets/departamentos.csv", "create_data/datasets/empleados.csv"]

#Cargar archivos
for archivo in archivos_csv:
    with open(archivo, "rb") as data:
        blob_client = blob_service_client.get_blob_client(container_name, archivo)
        blob_client.upload_blob(data)
        
print("Archivo CSV cargado en Azure Blob Storage.")
