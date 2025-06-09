import streamlit as st
from model import generate_image

# Título de la app
st.set_page_config(page_title="Generador IA de Imágenes", layout="centered")
st.title("🖼️ Generador de Imágenes con Estilo Naruto")

# Descripción
st.markdown("Introduce una descripción (prompt) y genera una imagen con el modelo entrenado.")
st.warning("Se recomienda escribir el prompt en inglés para un mejor resultado")

# Entrada de texto
prompt = st.text_area("✏️ Escribe tu prompt aquí:", height=150, placeholder="Ej: A strong man with mangekyo sharingan eyes...")


# Botón de generación
if st.button("Generar Imagen") and prompt.strip() != "":
    with st.spinner("🧠 Generando imagen..."):
        try:
            image = generate_image(prompt)
            st.image(image, caption="Imagen generada", use_column_width=True)
        except Exception as e:
            st.error(f"Ocurrió un error al generar la imagen: {e}")
else:
    st.info("Escribe un prompt y haz clic en 'Generar Imagen'.")

# Pie de página
st.markdown("---")
st.caption("Desarrollado con Streamlit · Modelo fine-tuneado de StableDiffusion v1.5 · © 2025")
