import pymysql
import pandas as pd

#* CONEXIÓN A LA BASE DE DATOS
conn = pymysql.connect(
    host="mysql",
    user="root",
    password="password01",
    database="prueba_tecnica_db"
)

query = "SELECT * FROM empresas"
df = pd.read_sql(query, conn)
df.to_csv("/app/output/empresas.csv", index=False)
conn.close()
print("Datos extraídos exitosamente")