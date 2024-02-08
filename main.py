import streamlit as st
from streamlit_modal import Modal
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
        "physical_damage": [1, "Physical Damage"],
        "magical_damage": [1, "Magical Damage"],
        "health": [1, "Health"],
        "armor": [1, "Armor"],
        "magic_resist": [1, "Magic Resist"],
        "speed": [1, "Speed"]
    }

    st.set_page_config(layout="wide")
    st.title("Dark and Darker Optimizer")
    st.header("Welcome to the Dark and Darker optimizer!")

    modal = Modal(
        "Instructions", 
        key="instructions-modal",
        
        # Optional
        padding=20,    # default value
        max_width=744  # default value
    )   

    open_modal = st.button("Instructions")

    if open_modal:
        modal.open()

    # Instructions button
    if modal.is_open():
        with modal.container():
            st.write("First you need to take screenshots of all items (must be taken like the example below)")
            st.image("./images/example0.png", use_column_width=False)
            st.write("Then you select the class, upload the screenshots and select the values that you want to optimize for your character and press the optimize button. The optimizer will return the best items for your character and the stats of the character with the equipment.")

    # Widget selectbox para seleccionar el personaje
    character = create_character(st.selectbox("Select your character:", data.character))

    # Widget file_uploader para cargar imágenes
    uploaded_images = st.file_uploader("Upload Items:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    # Widget sliders para ajustar los pesos
    st.header("Adjust the weights for the optimization:")

    for weight in weights:
        weights[weight][0] = st.slider(f"Weight for {weights[weight][1]}", 0, 10, 1)

    # Widget button para ejecutar la función
    if st.button("Optimize"):
        if uploaded_images is not None:
            for uploaded_image in uploaded_images:
                item = image_to_item(Image.open(uploaded_image))
                items.append(item)
        best_items = optimize_equipment(character, items, weights)
        
    if best_items is not None:
        st.header("Best items for the character:")
        # Display the images in a 2x5 grid
        col = st.columns(5)
        for i, item in enumerate(best_items):
            col[i % 5].image(item.image, use_column_width=True)

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
