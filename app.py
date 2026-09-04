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

models_data = [
    {"title": "Predictor en vivo", "image_path": predictor_image, "desc": "En el siguiente enlace veremos cómo predecir datos con regresión lineal.", "url": predictor_url, "link_text": "Predictor"},
    {"title": "Agrupamiento con K-Means", "image_path": kmeans_image, "desc": "En el siguiente enlace veremos cómo agrupar datos usando K-Means.", "url": kmeans_url, "link_text": "K-Means"},
    {"title": "Árboles de Decisión", "image_path": desiciontree_image, "desc": "En el siguiente enlace veremos cómo funciona un árbol de decisión.", "url": desiciontree_url, "link_text": "Árbol de Decisión"},
    {"title": "Regresión Logística", "image_path": logistic_image, "desc": "En el siguiente enlace veremos cómo funciona la regresión logística.", "url": logistic_url, "link_text": "Regresión Logística"}
]

# Helper function to render a single model card
def render_card(col, model):
    with col:
        st.subheader(model["title"])
        img = Image.open(model["image_path"])
        st.image(img, use_container_width=True)  # Fills the column nicely
        st.write(model["desc"])
        st.write(f"{model['link_text']}: [Enlace]({model['url']})")

# 2. Row 1: First 2 models
row1_col1, row1_col2 = st.columns(2, gap="large")
render_card(row1_col1, models_data[0])
render_card(row1_col2, models_data[1])

# Add some vertical spacing between rows
st.write("---") 

# 3. Row 2: Last 2 models
row2_col1, row2_col2 = st.columns(2, gap="large")
render_card(row2_col1, models_data[2])
render_card(row2_col2, models_data[3])