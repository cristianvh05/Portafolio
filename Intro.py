import streamlit as st
from PIL import Image
st.title("Aplicaciones desarrolladas en Computación Avanzada.")

with st.sidebar:
  st.subheader("Aplicaciones desarrolladas en Computación Avanzada.")
  parrafo = (
    "Este portafolio reúne las aplicaciones desarrolladas y puestas a prueba durante la asignatura de Programación Avanzada. Cada proyecto explora el potencial de la inteligencia artificial, el procesamiento de datos y la automatización para construir soluciones funcionales mediante código moderno."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En los siguientes enlaces puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Clasificación y Análisis de Frutas")
 st.image("frutas_app.webp", width=200)
 st.write(
    "Aplicación interactiva para evaluar y comparar frutas según sus atributos (peso, diámetro y dulzor). "
    "Permite ingresar nuevos especímenes y calcular métricas de distancia para determinar su similitud con otras frutas."
 )
 url = "https://frutasappclase.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("Detección de Anomalías y Complejidad")
 st.image("anomalias_complejidad.png", width=200)
 st.write(
    "Herramienta orientada al procesamiento eficiente de datos masivos e IA de alto rendimiento. "
    "Analiza la lógica de negocio, evalúa la complejidad computacional (Big-O) y aplica vectorización "
    "para optimizar la ejecución en hardware."
 )
 url = "https://detectoranomalias-my9xdojez9nixnmcayj7r5.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("Optimización y Descenso de Gradiente")
 st.image("descenso_gradiente.webp", width=200)
 st.write(
    "Aplicación matemática orientada a Machine Learning que demuestra cómo las derivadas y el gradiente "
    "transforman problemas de optimización. Visualiza el ajuste iterativo de parámetros en regresiones "
    "para minimizar el margen de error."
 )
 url = "https://detectoranomalias-my9xdojez9nixnmcayj7r5.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("Preparación y Estructura de Datos")
 st.image("preparacion_datos.jpg", width=200)
 st.write(
    "Plataforma interactiva para la refinería y estructuración de datos de sensores IoT. "
    "Permite experimentar en tiempo real con la tipificación de datos, tratamiento de imperfecciones "
    "(missing values y outliers), escalado geométrico, división metodológica (Train/Val/Test) "
    "y análisis estadístico descriptivo."
 )
 url = "https://clase5-2yjvfvzxurjhutb8ovkvoh.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
