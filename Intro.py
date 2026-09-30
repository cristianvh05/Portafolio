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
 st.subheader("Monitoreo Ambiental y Calidad de Datos")
 st.image("cornare_ambiental.webp", width=200)
 st.write(
    "Aplicación basada en la metodología CRISP-DM para el procesamiento de datos ambientales "
    "en tiempo real mediante la API de Cornare (MARCO). Permite explorar, limpiar y transformar registros "
    "meteorológicos, además de evaluar la fiabilidad de las estaciones mediante un Índice de Calidad de Datos (ICD)."
 )
 url = "https://cornarenivel-mve23atux8d3sjnrwwb8rg.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("Modelos de Regresión")
 st.image("regresion_modelos.png", width=200)
 st.write(
    "Herramienta de aprendizaje supervisado con regresión lineal simple y múltiple. Examina la función "
    "de costo y evalúa la precisión del modelo mediante métricas R², MAE y RMSE."
 )
 st.write("[Acceder a la app](https://regresion-ejvcypy27nacxbrbrdce9z.streamlit.app/)")

 st.subheader("Pronóstico y Análisis de Series de Tiempo")
 st.image("series_tiempo.webp", width=200)
 st.write(
    "Aplicación enfocada en la inteligencia predictiva mediante el análisis de series de tiempo. "
    "Descompone la información en tendencia, estacionalidad y ruido, e implementa modelos "
    "estadísticos como ARIMA y Suavizado Exponencial para anticipar lecturas de sensores IoT."
 )
 url = "https://seriestiempo-o9ybzx22blbnb6bzrgcqfp.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("Pronóstico de Calidad del Aire (PM2.5 y PM10)")
 st.image("calidad_aire.jpg", width=200)
 st.write(
    "Aplicación orientada a predecir la presencia de contaminantes (PM2.5 y PM10) mediante "
    "series de tiempo (ARIMA, SARIMA, Holt-Winters) y técnicas de ventanas deslizantes. "
    "Permite analizar tendencias y estacionalidades históricas para la gestión ambiental."
 )
 url = "https://pronosticocornare-pcgfjjubr7gjyviksekbsf.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

with col3: 
 st.subheader("Captura de Datos IoT y Predicción Térmica")
 st.image("prediccion_termica_iot.webp", width=200)
 st.write(
    "Aplicación que integra un flujo completo de ciencia de datos e IoT[cite: 2]. "
    "Permite la captura de telemetría propia (temperatura y humedad) mediante InfluxDB[cite: 2], "
    "procesamiento de series temporales con Pandas y entrenamiento de modelos de regresión "
    "para estimar la sensación térmica en tiempo real[cite: 2]."
 )
 url = "https://predicciontermica-agtwmkztyy6rfotnrggxt3.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")

 st.subheader("De la Regresión Lineal a la Logística")
 st.image("regresion_logistica.png", width=200)
 st.write(
    "Aplicación enfocada en la transición de la predicción numérica continua a la "
    "clasificación categórica binaria[cite: 3]. Explora la combinación de un motor lineal "
    "con el filtro sigmoide para transformar valores crudos en probabilidades[cite: 3], "
    "el establecimiento de umbrales de decisión y la evaluación con matrices de confusión[cite: 3]."
 )
 url = "https://regresionlogistica-aacyhsnjdc8bbwgsndqx7n.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")
 
 st.subheader("Clasificación de Fertilidad de Suelos (KNN)")
 st.image("knn_fertilidad_suelos.jpg", width=200)
 st.write(
    "Aplicación basada en el algoritmo de K-Vecinos Más Cercanos (KNN) para "
    "estimar la fertilidad de suelos (baja, media o alta) a partir de análisis "
    "químicos de AGROSAVIA. Permite analizar la influencia del valor de K, "
    "el escalado de variables y la evaluación del desempeño del modelo."
 )
 url = "https://ffk9axmzdge2itmhzun2lc.streamlit.app/"
 st.write(f"Acceder a la app: [Enlace]({url})")
