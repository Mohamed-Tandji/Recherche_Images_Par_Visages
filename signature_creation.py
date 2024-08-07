

import cv2
import numpy as np
import face_recognition
import os

# Chemin vers le dossier contenant les images
path = './Image_data'
# Liste pour stocker les images
image_list = []

# Liste pour stocker les chemins d'accès aux images
path_list = []

# Parcourir toutes les images dans le dossier
mylist = os.listdir(path)

# Charger les images et leurs chemins d'accès
for img in mylist:
    if os.path.splitext(img)[1].lower() in ['.jpg', '.png', '.jpeg']:
        cur_img = cv2.imread(os.path.join(path, img))
        
        # Ajouter l'image à la liste des images
        image_list.append(cur_img)
        
        # Ajouter le chemin d'accès de l'image à la liste des chemins
        path_list.append(os.path.join(path, img))

# Définir la détection de visage et l'extraction des caractéristiques
def findEncodings(image_list, path_list):
    """Définit la détection de visage et l'extraction des caractéristiques.
    
    Args:
        image_list (list): Liste d'images en BGR.
        path_list (list): Liste des chemins d'accès aux images.
    """
    signature_db = []
    total_images = len(image_list)
    for i, (img, img_path) in enumerate(zip(image_list, path_list)):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(img_rgb)
        if face_encodings:
            # Prendre les caractéristiques du premier visage détecté
            signature = face_encodings[0].tolist()
            # Ajouter le chemin d'accès de l'image à la fin des caractéristiques
            signature.append(img_path)
            signature_db.append(signature)
        print(f'{int((i+1)/total_images*100)} % extrait')
    signature_db = np.array(signature_db)
    np.save('Faces_Signatures_db.npy', signature_db)
    print("Données des visages enregistrées avec succès dans 'Face_Signatures_db.npy'.")

def main():
    findEncodings(image_list, path_list)

if __name__ == "__main__":
    main()
