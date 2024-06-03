import streamlit as st
import datetime
import numpy as np

st.title("Welcome to Popeye Gym")
st.markdown("---")

c1, c2 = st.columns(2)
name = c1.text_input("Nombre")
apellidos = c2.text_input("Apellidos")
c3, c4 = st.columns(2)
fecha_de_nacimiento = c3.date_input("Fecha de Nacimiento")
edad = datetime.datetime.now().year - fecha_de_nacimiento.year
if edad == 0:
    st.error("No haz introducido la edad!")
elif edad < 15:
    st.error("No tienes suficiente edad para ser como Popeye")
else:
    st.text("A comer Espinaca!!!")
municipio = c4.selectbox("Municipio", [" ""Guanabacoa", "Boyeros", "Centro Habana", "Vedado", "Playa", "Plaza", "La Habana Vieja", "Marianao", "La Lisa", "Otro"])
sexo = st.radio("Sexo",["Masculino","Femenino"])

razones = st.text_input("Porque quieres empezar el gym?")
frecuencia = st.radio("Cual es el horario en el que acudes al gimnasio?", ["8-10 am","10-12 am","2-4 pm","4-6 pm","6-8 pm"])

st.markdown(">Resumiendo :)")
st.text("Te llamas:") 
st.text(name)
st.text("Tienes:")
st.text(edad)
st.text("Y vives en:")
st.text(municipio)

st.button("Enviar")

