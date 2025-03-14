import pandas as pd
import pymysql

#* DATAFRAME: Creamos el dataframe de la transformación
df = pd.read_csv('/app/output/empresas_transformed.csv')

#* CONEXIÓN A LA BASE DE DATOS
conn = pymysql.connect(
    host="mysql",
    user="root",
    password="password01",
    database="prueba_tecnica_db"
)
cursor = conn.cursor()

#* CAMBIO DE ESQUEMA: Se cambia el esquema debido a la longitud de los valores de las columnas 'id' y 'company_id'
# Se cambia la longitud de las columnas 'id' y 'company_id' a VARCHAR(40)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id VARCHAR(40) PRIMARY KEY,
        company_name VARCHAR(130)
    );
""")
# Se cambia la longitud de las columnas 'id' y 'company_id' a VARCHAR(40)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS charges (
        id VARCHAR(40) PRIMARY KEY,
        company_id VARCHAR(40),
        amount DECIMAL(16,2) NOT NULL,
        company_status VARCHAR(30) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        paid_at TIMESTAMP NULL,
        FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
    );
""")

#* CARGA DE DATOS: Se cargan los datos transformados en la base de datos
# Unicas dos compañias
companies = df[["company_id", "company_name"]].drop_duplicates()
# Carga de los datos de la tabla 'companies'
for index, row in companies.iterrows():
    sql = """
    INSERT INTO companies (id, company_name)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (row['company_id'], row['company_name']))
# Carga de los datos de la tabla 'charges'
for index, row in df.iterrows():
    paid_at = None if pd.isna(row['paid_at']) else row['paid_at']  # Convertir NaT a NULL
    sql = """
    INSERT INTO charges (id, company_id, amount, company_status, created_at, paid_at)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (row['id'], row['company_id'], row['amount'], row['company_status'], row['created_at'], paid_at))

#* CERRAMOS CONECCION 
conn.commit()
cursor.close()
conn.close()
print("Datos dispersados exitosamente")