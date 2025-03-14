import pandas as pd
import random
import hashlib

# Creamos el dataframe
df = pd.read_csv('/app/output/empresas.csv')

#* COLUMNA: 'id'
# Aqui no hay forma de obtener los valores faltantes ya que son unicos, así que se toma la decision de crearlos artificialmente
# Función para generar un hash aleatorio con el mismo formato
def generar_id():
    random_str = str(random.getrandbits(256))
    return hashlib.sha1(random_str.encode()).hexdigest()
# Reemplazar valores NaN con un ID aleatorio
df['id'] = df['id'].apply(lambda x: generar_id() if pd.isna(x) else x)

#* COLUMNA: 'company_id'
# Usaremos la columna 'company_name' para encontar los valores faltantes en la columna 'company_id'
# Obtenemos la moda de la columna 'company_id' cuando 'company_name' es igual a 'MiPasajefy'
moda_MiPasajefy = df[df['company_name']=='MiPasajefy']['company_id'].mode()
# Si 'company_name' es igual a 'MiPasajefy' reemplazamos 'company_id' por moda_MiPasajefy
df.loc[df['company_name'] == 'MiPasajefy', 'company_id'] = moda_MiPasajefy
# Reemplazamos los valores faltantes en la columna 'company_id' por la moda solo si 'company_name' es igual 'MiPasajefy'
df.loc[df['company_name']=='MiPasajefy', 'company_id'] = df.loc[df['company_name']=='MiPasajefy', 'company_id'].fillna(moda_MiPasajefy[0])

#* COLUMNA: 'company_name'
# Notamos que al 'company_name'='MiPasajefy' le corresponde el 'company_id'='cbf1c8b09cd5b549416d49d220a40cbd317f952e'
# por lo tanto, sustituimos en la columna 'company_name' el valor 'MiPasajefy' cuando 'company_id' es igual a 'cbf1c8b09cd5b549416d49d220a40cbd317f952e'
df.loc[df['company_id']=='cbf1c8b09cd5b549416d49d220a40cbd317f952e', 'company_name'] = 'MiPasajefy'

#* Ajustar tipo de datos
df["created_at"] = pd.to_datetime(df["created_at"])
df["paid_at"] = pd.to_datetime(df["paid_at"])
df["amount"] = df["amount"].astype(float)

#* Guardamos el dataframe en un archivo CSV
df.to_csv("/app/output/empresas_transformed.csv", index=False)
print("Datos transformados exitosamente")