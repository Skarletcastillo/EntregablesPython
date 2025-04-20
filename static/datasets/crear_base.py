import sqlite3

# Conexión a base de datos 
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

# Crear la tabla personas
cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    Nombre TEXT,
    Edad INTEGER,
    Ciudad TEXT
)
""")

# Insertar datos 
cursor.execute("SELECT COUNT(*) FROM personas")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO personas VALUES (?, ?, ?)", [
        ("Ana", 25, "Madrid"),
        ("Juan", 30, "Barcelona"),
        ("Pedro", 35, "Sevilla")
    ])

conn.commit()
conn.close()

#comando para que la tabla se cree --> python crear_base.py
