import streamlit as st
from PIL import Image

from tools.optimizer import optimize_equipment
from src.characters import create_character
from tools.image_to_item import image_to_item
import data.game_data as data

def main():
    items = []
    character = None
    best_items = None
    uploaded_images = None

    # Weights for the optimization
    weights = {
        "physical_damage": 1,
        "magical_damage": 1,
        "health": 1,
        "armor": 1,
        "magic_resist": 1,
        "speed": 1
    }

    st.set_page_config(layout="wide")
    st.title("Dark and Darker Optimizer")
    st.header("Welcome to the Dark and Darker optimizer!")

    # Widget selectbox para seleccionar el personaje
    character = create_character(st.selectbox("Select a character:", data.character))

    # Widget file_uploader para cargar imágenes
    uploaded_images = st.file_uploader("Upload an image:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    # Muestra la imagen cargada
    if uploaded_images is not None:
        for uploaded_image in uploaded_images:
            item = image_to_item(Image.open(uploaded_image))
            items.append(item)

    # Widget sliders para ajustar los pesos
    for category, default_value in weights.items():
        weights[category] = st.slider(f"{category.capitalize()} Weight", 0, 10, default_value)

    # Widget button para ejecutar la función
    if st.button("Optimize"):
        best_items = optimize_equipment(character, items, weights)
        
    if best_items is not None:
        st.header("Best items for the character:")
        # Display the images in a 2x5 grid
        col = st.columns(5)
        for i, item in enumerate(best_items):
            col[i % 5].image(item.image, caption=item, use_column_width=True)

        for item in best_items:
            character.equip_item(item)
        
        st.header("Stats of the character with equipment:")
        col = st.columns(5)
        i = 0
        for stat, value in character.get_stats().items():
            col[i % 5].write(f"{stat}: {value}")
            i+=1
    
    st.write("Made with ❤️ for Dark and Darker Community by gonibix23")

if __name__ == "__main__":
    main()
