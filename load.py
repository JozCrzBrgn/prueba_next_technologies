import pymysql
import pandas as pd
import numpy as np

# Conectar con MySQL
conn = pymysql.connect(
    host="mysql",
    user="root",
    password="password01",
    database="prueba_tecnica_db"
)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS empresas (
    id VARCHAR(40) PRIMARY KEY NOT NULL,
    company_name VARCHAR(130),
    company_id VARCHAR(40) NOT NULL,
    amount DECIMAL(16, 2) NOT NULL,
    company_status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    paid_at TIMESTAMP
);
""")

# Cargar datos desde CSV
df = pd.read_csv("data_prueba_técnica.csv")

# Reeemplazar NaN por None
df = df.replace({np.nan: None})

# Insertar en la base de datos
for _, row in df.iterrows():
    cursor.execute(
        "INSERT IGNORE INTO empresas (id, company_name, company_id, amount, company_status, created_at, paid_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (row["id"], row["name"], row["company_id"], row["amount"], row["status"], row["created_at"], row["paid_at"])
    )
conn.commit()
cursor.close()
conn.close()
print("Datos cargados exitosamente")