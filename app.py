import streamlit as st
import os
from PIL import Image

default_image = "images/knn.png"

predictor_url = "https://app-preview-jesduhbggg3wn7jdror8pb.streamlit.app/"
predictor_image = "images/knn.jpeg"

kmeans_url = "https://kmeans-logisticregression-svc.streamlit.app/"
kmeans_image = "images/kmeans.jpeg"

desiciontree_url = "https://decisiontreejuank.streamlit.app/"
desiciontree_image = "images/desiciontree.jpeg"

logistic_url = "https://logisticregressionjuank.streamlit.app/"
logistic_image = "images/logistic_image.jpeg"

consumo_energetico_url = "https://consumo-energetico-juank.streamlit.app/"
consumo_energetico_image = "images/consumo_energetico.jpg"

texto_audio_url = "https://texttoaudiojuank.streamlit.app/"
texto_audio_image = "images/texto_a_audio.jpg"

audio_texto_url = "https://translateaudio2text.streamlit.app/"
audio_texto_image = "images/audio_a_texto.jpg"

rnn_url = "https://rnn-energycons.streamlit.app/"
rnn_image = "images/rnn.jpg"

lstm_url = "https://lstmjuank.streamlit.app/"
lstm_image = "images/lstm.jpg"

vision_url = "https://computervision-juank.streamlit.app/"
vision_image = "images/vision_artificial.jpg"

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
    {"title": "Regresión Logística", "image_path": logistic_image, "desc": "En el siguiente enlace veremos cómo funciona la regresión logística.", "url": logistic_url, "link_text": "Regresión Logística"},
    {"title": "Consumo Energetico", "image_path": consumo_energetico_image, "desc": "En el siguiente enlace veremos cómo predecir el consumo energético.", "url": consumo_energetico_url, "link_text": "Consumo Energético"},
    {"title": "Texto a Audio", "image_path": texto_audio_image, "desc": "En el siguiente enlace puedes convertir texto en audio utilizando síntesis de voz.", "url": texto_audio_url, "link_text": "Texto a Audio"},
    {"title": "Audio a Texto", "image_path": audio_texto_image, "desc": "En el siguiente enlace puedes transcribir y traducir grabaciones de audio a texto.", "url": audio_texto_url, "link_text": "Traductor Audio"},
    {"title": "Redes Neuronales Recurrentes (RNN)", "image_path": rnn_image, "desc": "En el siguiente enlace veremos la aplicación de redes neuronales recurrentes para predicción de consumo energético.", "url": rnn_url, "link_text": "RNN Consumo Energético"},
    {"title": "Redes LSTM", "image_path": lstm_image, "desc": "En el siguiente enlace veremos el modelado y predicción de series temporales utilizando redes LSTM.", "url": lstm_url, "link_text": "Redes LSTM"},
    {"title": "Visión Artificial", "image_path": vision_image, "desc": "En el siguiente enlace encontrarás aplicaciones interactivas y modelos de visión computacional.", "url": vision_url, "link_text": "Visión Computacional"}
]

# Helper function to render a single model card
def render_card(col, model):
    with col:
        st.subheader(model["title"])
        img_path = model.get("image_path")
        if not (img_path and os.path.exists(img_path)):
            img_path = default_image
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, use_container_width=True)  # Fills the column nicely
        st.write(model["desc"])
        st.write(f"{model['link_text']}: [Enlace]({model['url']})")

# Render cards in a responsive 2-column grid
for i in range(0, len(models_data), 2):
    cols = st.columns(2, gap="large")
    render_card(cols[0], models_data[i])
    if i + 1 < len(models_data):
        render_card(cols[1], models_data[i + 1])
    if i + 2 < len(models_data):
        st.write("---")
