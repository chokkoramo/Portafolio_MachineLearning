import streamlit as st
from PIL import Image
file_image = "images/knn.png"

kmeans_image = "images/kmeans.png"
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

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Clasificación con KNN")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open(file_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = ""
    st.write(f"KNN: [Enlace]({url})")

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
    image = Image.open(file_image)
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "REEMPLAZA_url_arbol.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")
