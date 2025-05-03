import sqlite3
import numpy as np
import pandas as pd
import firebase_admin
import streamlit as st
from pymongo import MongoClient
from firebase_admin import credentials
from firebase_admin import firestore
from sqlalchemy import create_engine

#Crea una aplicación básica en Streamlit:
st.set_page_config(   
    page_icon="📖",
    layout="wide"
)

st.title("Momento 2 ° Actividad 1")

st.markdown(""" """)

st.header("･ﾟ✧．Creación de DataFrames .✧･ﾟ")
st.subheader("Descripción de la actividad")
# Descripción general
st.write("""
    En esta actividad, vamos a explorar diferentes formas de crear **DataFrames** en Pandas
    y mostrarlos utilizando Streamlit. A continuación, se presentan varios tipos de DataFrames:
    - Diccionario de libros
    - Lista de diccionarios con información de ciudades
    - Lista de listas con productos
    - Series combinadas para personas
    - Datos cargados desde un archivo CSV como:
        - CSV (local)
        - Excel (local)
        - Archivo JSON
        - URL
    - Base de datos SQLite
    - Array de NumPy
    - Firebase
    - MongoDB
         
""")

#----------------------------------------------------------------------
st.markdown(""" """)
#Crea DataFrames desde diferentes fuentes:

# Diccionario de libros
libros = {
    "título": ["Cien años de soledad", "Don Quijote de la Mancha", "1984", "El amor en los tiempos del cólera"],
    "autor": ["Gabriel García Márquez", "Miguel de Cervantes", "George Orwell", "Gabriel García Márquez"],
    "año de publicación": [1967, 1605, 1949, 1985],
    "género": ["Realismo mágico", "Novela de caballería", "Distopía", "Romántico"]
}

df_libros = pd.DataFrame(libros)

st.subheader(".✧･ﾟ 📚 DataFrame de Libros 📚 ･ﾟ✧．")
st.write("A continuación se muestra un DataFrame con información sobre algunos libros.")
st.dataframe(df_libros)


#----------------------------------------------------------------------
st.markdown(""" """)
# Lista de diccionarios
ciudades = [
    {"nombre": "Bogotá", "población": 8000000, "país": "Colombia"},
    {"nombre": "Lima", "población": 9000000, "país": "Perú"},
    {"nombre": "Madrid", "población": 3200000, "país": "España"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"}
]

df_ciudades = pd.DataFrame(ciudades)

st.subheader(".✧･ﾟ🌍Información de Ciudades 🌍･ﾟ✧．")
st.write("Este es un DataFrame que muestra algunas ciudades, su población y el país al que pertenecen.")
st.dataframe(df_ciudades)

#----------------------------------------------------------------------
st.markdown(""" """)
# Lista de listas de productos
productos = [
    ["Tablet", 350.00, 12],
    ["Auriculares", 80.50, 40],
    ["Cargador", 25.00, 100],
    ["Smartwatch", 200.00, 15]
]

df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])

st.subheader(".✧･ﾟ🛍️ Productos en Inventario 🛍️･ﾟ✧．")
st.write("Aquí mostramos algunos productos, su precio y la cantidad disponible en stock.")
st.dataframe(df_productos)


#----------------------------------------------------------------------
st.markdown(""" """)
# Series de personas
nombres = pd.Series(["Ana", "Luis", "María", "Carlos"])
edades = pd.Series([28, 34, 22, 30])
ciudades = pd.Series(["Bogotá", "Lima", "Madrid", "Buenos Aires"])

# Combinar en un diccionario
personas = {
    "nombre": nombres,
    "edad": edades,
    "ciudad": ciudades
}

df_personas = pd.DataFrame(personas)

st.subheader(".✧･ﾟ👥 Datos de Personas 👥･ﾟ✧．")
st.write("A continuación se muestra información sobre varias personas, incluyendo su nombre, edad y ciudad.")
st.dataframe(df_personas)


#----------------------------------------------------------------------
st.markdown(""" """)
df_csv = pd.read_csv('static/datasets/data.csv')
st.subheader(".✧･ﾟ📄 Datos desde CSV 📄･ﾟ✧．")
st.write("Aquí están los datos cargados desde un archivo CSV.")
st.dataframe(df_csv)

#----------------------------------------------------------------------
st.markdown(""" """)
# Archivo Excel (local):
st.subheader(".✧･ﾟ📗 Datos desde un archivo excel 📗.✧･ﾟ")
st.write("Aquí están los datos cargados desde un archivo de excel, muestra el id, nombre y apellido de personas")
df_excel = pd.read_excel('static\datasets\Alumnos.xlsx')
st.dataframe(df_excel)


#----------------------------------------------------------------------
st.markdown(""" """)
# Archivo JSON
st.subheader(".✧･ﾟ🗂️ Datos desde un json 🗂️✧･ﾟ")
st.write("Aquí están los datos cargados desde un json, muestra los nombres, la edad y la cuidad a la que pertenecen")
df_json = pd.read_json("static\datasets\data.json")
st.dataframe(df_json)

#----------------------------------------------------------------------
st.markdown(""" """)
# URL:
st.subheader(".✧･ﾟ🌐 Datos desde una URL 🌐✧･ﾟ")
st.write("A continuación se muestra información sobre usuarios")
df_Url = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
st.dataframe(df_Url)


#----------------------------------------------------------------------
st.markdown(""" """)
# Conectar a la base de datos SQLite
conn = sqlite3.connect("estudiantes.db")
df = pd.read_sql("SELECT * FROM notas", conn)
conn.close()

# Mostrar los datos
st.subheader(".✧･ﾟ🧮 Datos desde SQLite 🧮.･ﾟ✧")
st.dataframe(df)


#----------------------------------------------------------------------
st.markdown(""" """)
#Array de NumPy:
st.subheader(".✧･ﾟ🟦 Datos desde NumPy 🟦.･ﾟ✧")

# Creamos una matriz de 3 filas y 2 columnas
datos = np.array([
    ["Ana", 85, "desarrollo de software" ],
    ["Luis", 92, "desarrollo de software"],
    ["Carlos", 78, "desarrollo de software"]
])

# Convertimos a DataFrame y ponemos los nombres de columnas
df_NumPy = pd.DataFrame(datos, columns=["Nombre", "Calificacion", "Curso"])

st.dataframe(df_NumPy)

#----------------------------------------------------------------------
st.markdown(""" """)
#Firebase --> IMPORTANTE (antes de subir algun commit se debe colocar en gitignore --> static/datasets/key.json)
# consola > pip install firebase-admin pandas
# configurar API https://console.cloud.google.com/apis/api/firestore.googleapis.com/metrics?project=entregables-python-a6527
#configurar iniciar BD https://console.cloud.google.com/datastore/create-database?project=entregables-python-a6527
st.subheader(".✧･ﾟ🍂 Datos desde Firebase🍂.･ﾟ✧")

# Inicializar solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate('static\datasets\key.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Obtener datos (llamar una coleccion)
users = db.collection('Univercidad').stream()
users_data = [doc.to_dict() for doc in users]
df = pd.DataFrame(users_data)

st.dataframe(df)

#----------------------------------------------------------------------
# Conectar a MongoDB Atlas
# consola --> pip install pymongo
client = MongoClient("mongodb+srv://SkarletUser:genessiskarlet@mi-cluster.r5118qf.mongodb.net/")
db = client["sample_mflix"]             
coleccion = db["comments"]                

# Traer documentos (limitamos a 100)
documentos = list(coleccion.find().limit(100))

# Convertir a DataFrame 
df = pd.DataFrame(documentos)

# Mostrar en Streamlit
st.subheader(".✧･ﾟ🍃 Datos desde MongoDB 🍃.･ﾟ✧")
st.dataframe(df)    