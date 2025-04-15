import streamlit as st
import pandas as pd
import io
import csv

# Configuración de la página
st.set_page_config(   
    page_icon="📖",
    layout="wide"
)

st.title("Momento 2 ° Actividad 2")

st.header("･ﾟ✧．Filtrar .✧･ﾟ")
st.subheader("Descripción de la actividad")
st.markdown("""
    Esta actividad utilizaremos un dataset de estudiantes en colombia donde el usurio podra visualizar:
    - las primeras 5 filas y las últimas 5 filas del dataset.
    - Se muestra un resumen 
    - Seleccion de nombre, edad y promedio     
    - Filtrar estudiantes con promedio mayor a un valor definido por el usuario           
""")


st.markdown(""" """)

#Aquí es donde se carga al data y se muestra
st.subheader("･ﾟ✧📊 Dataset 📊✧･ﾟ")
dataframe_estudiantes_colombia = pd.read_csv('static/datasets/estudiantes_colombia.csv')
st.dataframe(dataframe_estudiantes_colombia)

st.markdown(""" """)
#Acá solo se pide que muestre las primeras 5 filas
st.subheader("･ﾟ✧．👀 Ver las primeras 5 filas 👀.✧･ﾟ")
st.write(dataframe_estudiantes_colombia.head())

st.markdown(""" """)
#Acá solo se pide que muetsre las últimas 5 filas
st.subheader(".✧･ﾟ🔚 Ver las últimas 5 filas 🔚･ﾟ✧")
st.write(dataframe_estudiantes_colombia.tail())

st.markdown(""" """)
#Esto muestra características especificas de las columnas numéricas.
st.header("📌Resumen📌")
st.subheader(".✧･ﾟ🧮Resumen con 'Describe'🧮･ﾟ✧")
descripcion = dataframe_estudiantes_colombia.describe()
st.write(descripcion)

st.markdown(""" """)
#Este nos muestra la información del dataframe, cuantas columnas tiene, su tipo, la cantidad de datos que hay en cada una y así.
st.subheader(".✧･ﾟ🧾Resumen con 'Info'🧾.･ﾟ✧")
info = dataframe_estudiantes_colombia.info()
buffer = io.StringIO()
dataframe_estudiantes_colombia.info(buf=buffer)
info_string = buffer.getvalue()
st.code(info_string)

st.markdown(""" """)
#Acá solo se pide mostrar 3 columnas puntuales de las que hay en el dataframe.
st.subheader(".✧･ﾟ🎯 Selección de columnas: Nombre, Edad y Promedio 🎯.･ﾟ✧")
st.write(dataframe_estudiantes_colombia[['Nombre', 'Edad', 'Promedio']])

st.markdown(""" """)
#Este nos filtra por medio de una barra, donde se puede buscar el promedio a filtrar y nos muestra los estudiantes que corresponden al promedio selecciondo.
st.subheader(".✧･ﾟ📉 Filtrar estudiantes por promedio 📉.･ﾟ✧")
promedio = st.slider("Selecciona el promedio:", 0.0, 5.0, 3.0)

filtrado_de_promedio = dataframe_estudiantes_colombia[dataframe_estudiantes_colombia['Promedio'] >= promedio]

st.write("🎚️ Estudiantes con promedio mayor o igual a: ", promedio, "🎚️")
st.dataframe(filtrado_de_promedio) 