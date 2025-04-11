import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")


st.markdown("""

""")

st.header("Actividad #1 - Creación de DataFrames")
st.subheader("Descripción de la actividad")
st.markdown("""
En esta actividad realizaré 2 Dataframes, uno de un diccionario y otro de una lista de diccionarios.
El primer DataFrame contendrá información sobre libros, incluyendo el título, autor, año de publicación y género, sobre el segundo mostrará información sobre ciudades, incluyendo el nombre, población y país.
""")

libros = {
    "Título del libro": ["El Principito", "Don Quijote de la Mancha", "Cien años de soledad", "Los Juegos del Hambre"],
    "Autor": ["Antoine de Saint-Exupéry", "Miguel de Cervantes", "Gabriel García Márquez", "Suzanne Collins"],
    "Año de publicación": [1943, 1605, 1967, 2008],
    "Género": ["Fábula, Fantasía", "Novela", "Realismo mágico", "Ciencia ficción"],
}

dataframe_libros = pd.DataFrame(libros)

st.write("DataFrame de libros:")
st.dataframe(dataframe_libros)


st.expander("Mostrar DataFrame de ciudades", expanded=True)


ciudades =[
    {"Nombre": "Medellín", "Población": 58964852, "País": "Colombia"},
    {"Nombre": "Madrid", "Población": 6589745, "País": "España"},
    {"Nombre": "Seul", "Población": 35621000, "País": "Corea del Sur"},
]

dataframe_ciudades = pd.DataFrame(ciudades)

st.write("DataFrame de ciudades:")
st.dataframe(dataframe_ciudades)
