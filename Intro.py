import streamlit as st
from PIL import Image
st.title("Aplicaciones de Daniel.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Intro 1ra App")
 image = Image.open('Marvel.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace encontraremos la primera app de Daniel") 
 url = "https://intro1.streamlit.app//"
 st.write(f"Mi primera app: [Enlace]({url})")

 st.subheader("Reconocimiento de Caracteres")
 image = Image.open('Robot.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan caracteres de una imagen.") 
 url = "https://reconocimiento.streamlit.app/"
 st.write(f"App: [Enlace]({url})")

 st.subheader("Reconocimiento de Caracteres a Audio") 
 image = Image.open('Audifonos.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan caracteres de una imagen y escucharlo .") 
 url = "https://ocr0-audioo.streamlit.app/"
 st.write(f"App: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto (Traductor)")
 image = Image.open('Traductor.png')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que se usa como traductor.") 
 url = "https://voztexto.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")
  
 st.subheader("La Luciernaga y el Sapo")
 image = Image.open('Princesa.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que convierte el texto a voz.") 
 url = "https://texto-vozdaniel.streamlit.app/"
 st.write(f"Texto a Voz: [Enlace]({url})")

 st.subheader("Reconocimiento de Texto (Estado)")
 image = Image.open('Estados.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar tu estado de animo con un texto.") 
 url = "https://txt-2-daniel.streamlit.app/"
 st.write(f"Enlace: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Analizador de Textos")
 image = Image.open('Analizador.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que analiza textos.") 
 url = "https://texto-anadaniel.streamlit.app/"
 st.write(f"Enlace: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos en Imagenes")
 image = Image.open('Reconocimiento.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en los objetos en las imagenes.") 
 url = "https://reconocimientoy.streamlit.app/
 st.write(f"Reconocimiento: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


