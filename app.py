import streamlit as st
from PIL import Image
default_image = "images/knn.png"

desiciontree_url = "https://decisiontreejuank.streamlit.app/"
desiciontree_image = "images/desiciontree.jpeg"

predictor_url = "https://app-preview-jesduhbggg3wn7jdror8pb.streamlit.app/"
predictor_image = "images/knn.jpeg"

logistic_url = "https://logisticregressionjuank.streamlit.app/"
logistic_image = "images/logistic_image.jpeg"

desiciontree_image = "images/desiciontree.jpeg"
desiciontree_url = "https://decisiontreejuank.streamlit.app/"

kmeans_image = "images/kmeans.jpeg"
kmeans_url = "https://kmeans-logisticregression-svc.streamlit.app/"

st.title("Aplicaciones de Machine Learning.")

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning.")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ml})")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Predisctor en vivo")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open(predictor_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = predictor_url
    st.write(f"Predictor: [Enlace]({url})")

with col2:
    st.subheader("Agrupamiento con K-Means")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open(kmeans_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = kmeans_url
    st.write(f"K-Means: [Enlace]({url})")

with col3:
    st.subheader("Árboles de Decisión")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open(desiciontree_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = desiciontree_url
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col4:
    st.subheader("Regresión Logística")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open(logistic_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona la regresión logística.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = logistic_url
    st.write(f"Regresión Logística: [Enlace]({url})")
