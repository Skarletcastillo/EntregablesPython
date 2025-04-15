#Importa las bibliotecas necesarias:
import streamlit as st
import pandas as pd

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

st.markdown(""" """)
#Crea DataFrames desde diferentes fuentes:

# Diccionario de libros
libros = {
    "título": ["Cien años de soledad", "Don Quijote de la Mancha", "1984", "El amor en los tiempos del cólera"],
    "autor": ["Gabriel García Márquez", "Miguel de Cervantes", "George Orwell", "Gabriel García Márquez"],
    "año de publicación": [1967, 1605, 1949, 1985],
    "género": ["Realismo mágico", "Novela de caballería", "Distopía", "Romántico"]
}

# Crear DataFrame
df_libros = pd.DataFrame(libros)

# Mostrar en Streamlit
st.subheader(".✧･ﾟ 📚 DataFrame de Libros 📚 ･ﾟ✧．")
st.write("A continuación se muestra un DataFrame con información sobre algunos libros.")
st.dataframe(df_libros)



st.markdown(""" """)
# Lista de diccionarios de ciudades
ciudades = [
    {"nombre": "Bogotá", "población": 8000000, "país": "Colombia"},
    {"nombre": "Lima", "población": 9000000, "país": "Perú"},
    {"nombre": "Madrid", "población": 3200000, "país": "España"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"}
]

# Crear DataFrame
df_ciudades = pd.DataFrame(ciudades)

# Mostrar en Streamlit
st.subheader(".✧･ﾟ🌍Información de Ciudades 🌍･ﾟ✧．")
st.write("Este es un DataFrame que muestra algunas ciudades, su población y el país al que pertenecen.")
st.dataframe(df_ciudades)


st.markdown(""" """)
# Lista de listas de productos
productos = [
    ["Tablet", 350.00, 12],
    ["Auriculares", 80.50, 40],
    ["Cargador", 25.00, 100],
    ["Smartwatch", 200.00, 15]
]

# Crear DataFrame
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])

# Mostrar en Streamlit
st.subheader(".✧･ﾟ🛍️ Productos en Inventario 🛍️･ﾟ✧．")
st.write("Aquí mostramos algunos productos, su precio y la cantidad disponible en stock.")
st.dataframe(df_productos)



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

# Crear DataFrame
df_personas = pd.DataFrame(personas)

# Mostrar en Streamlit
st.subheader(".✧･ﾟ👥 Datos de Personas 👥･ﾟ✧．")
st.write("A continuación se muestra información sobre varias personas, incluyendo su nombre, edad y ciudad.")
st.dataframe(df_personas)


st.markdown(""" """)
# Leer CSV local
df_csv = pd.read_csv('static/datasets/data.csv')

# Mostrar en Streamlit
st.subheader(".✧･ﾟ📄 Datos desde CSV 📄･ﾟ✧．")
st.write("Aquí están los datos cargados desde un archivo CSV.")
st.dataframe(df_csv)


st.markdown(""" """)
# Archivo Excel (local):
st.subheader(".✧･ﾟ📗 Datos desde un archivo excel 📗.✧･ﾟ")
st.write("Aquí están los datos cargados desde un archivo de excel, muestra el id, nombre y apellido de personas")
df_excel = pd.read_excel('static\datasets\Alumnos.xlsx')
st.dataframe(df_excel)


st.markdown(""" """)
# Archivo JSON
st.subheader(".✧･ﾟ🗂️ Datos desde un json 🗂️✧･ﾟ")
st.write("Aquí están los datos cargados desde un json, muestra los nombres, la edad y la cuidad a la que pertenecen")
df_json = pd.read_json("static\datasets\data.json")
st.dataframe(df_json)

st.markdown(""" """)
# URL:
st.subheader(".✧･ﾟ🌐 Datos desde una URL 🌐✧･ﾟ")
st.write("A continuación se muestra información sobre usuarios")
df_Url = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
st.dataframe(df_Url)



#------------------------
st.markdown(""" """)
#Base de datos SQLite:


st.markdown(""" """)
#Array de NumPy:


st.markdown(""" """)
#Firebase:


st.markdown(""" """)
# MongoDB


