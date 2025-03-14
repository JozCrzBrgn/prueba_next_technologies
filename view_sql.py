import pymysql

# Conectar con MySQL
conn = pymysql.connect(
    host="mysql",
    user="root",
    password="password01",
    database="prueba_tecnica_db"
)
cursor = conn.cursor()

#* Crear la vista => SELECT * FROM total_transacciones_por_dia;
cursor.execute("""
    CREATE VIEW total_transacciones_por_dia AS
    SELECT 
        DATE(ch.created_at) AS fecha, 
        ch.company_id, 
        comp.company_name, 
        SUM(ch.amount) AS total_monto
    FROM charges ch
    JOIN companies comp ON ch.company_id = comp.id
    GROUP BY DATE(ch.created_at), ch.company_id, comp.company_name
    ORDER BY fecha ASC;
""")
conn.commit()
cursor.close()
conn.close()
print("Vista creada exitosamente")