import numpy as np
import pandas as pd
import streamlit as st
from fonctions import find_similar_images
import os

def main():
    st.header("MT Image Search \U0001F600")
    st.write('-------------------------------------------------------------------')

    filename = st.sidebar.file_uploader(label='Télécharger votre image ici')
    
    if filename is not None:
        # Définissez un chemin de fichier temporaire pour l'image téléchargée
        temporary_file_path = "uploaded_image.jpg"  # Vous pouvez personnaliser le nom du fichier temporaire

        # Écrivez l'image téléchargée sur le disque
        with open(temporary_file_path, "wb") as f:
            f.write(filename.read())
            
        st.write('-------------------------------------------------------------------')
        st.subheader('Image à chercher')
        st.image(filename, width=150)
        st.write('-------------------------------------------------------------------')
        st.subheader('Affichage des résultats')
        
        try:
            myimg = find_similar_images(temporary_file_path)
            
            if len(myimg) == 0:
                st.error("Aucune image correspondante trouvée 😞")
            elif len(myimg) > 1:
                num_images = len(myimg)
                num_cols = 3  # Nombre de colonnes par ligne
                num_rows = (num_images - 1) // num_cols + 1  # Calcul du nombre de lignes nécessaires
                col_width = 1 / num_cols  # Largeur de chaque colonne
                
                for i in range(num_rows):
                    cols = st.columns(num_cols)
                    for j in range(num_cols):
                        idx = i * num_cols + j
                        if idx < num_images:
                            cols[j].image(myimg[idx], width=200)
                            
            else:
                st.image(myimg[0], width=200)
                
        except Exception as e:
            st.error(f"Une erreur s'est produite : {str(e)}")
        
        os.remove(temporary_file_path)

if __name__ == '__main__':
    main()
