import cv2
import numpy as np
import face_recognition
import os
import streamlit as st

# # def find_similar_images(input_image):
# #     input_image = cv2.imread(input_image)
    
# #     # Charger la base de données d'images et d'encodages
# #     database = np.load('Faces_Signatures_db.npy', allow_pickle=True)
    
# #     # Extraire les caractéristiques faciales et les chemins d'accès aux images de la base de données
# #     known_face_encodings = []
# #     image_paths = []
# #     for item in database:
# #         face_encoding = item[:-1]  # Caractéristiques du visage (toutes les valeurs sauf la dernière)
# #         image_path = item[-1]  # Chemin d'accès à l'image (dernière valeur)
# #         known_face_encodings.append(np.array(face_encoding, dtype=np.float64))  # Convertir en tableau numpy de float64
# #         image_paths.append(image_path)
    
# #     # Encoder les caractéristiques faciales de l'image entrante
# #     input_encoding = face_recognition.face_encodings(input_image)[0]
    
# #     # Convertir l'encodage d'entrée en tableau numpy de float64
# #     input_encoding = np.array(input_encoding, dtype=np.float64)
    
# #     # Comparer les caractéristiques faciales avec la base de données
# #     matches = face_recognition.compare_faces(known_face_encodings, input_encoding)
    
# #     # Récupérer les chemins d'accès aux images correspondantes
# #     matching_image_paths = [image_paths[i] for i, match in enumerate(matches) if match]
    
# #     return matching_image_paths

# def find_similar_images(input_image):
#     input_image = cv2.imread(input_image)
    
#     # Charger la base de données d'images et d'encodages
#     database = np.load('Faces_Signatures_db.npy', allow_pickle=True)
    
#     # Extraire les caractéristiques faciales et les chemins d'accès aux images de la base de données
#     known_face_encodings = []
#     image_paths = []
#     for item in database:
#         face_encoding = item[:-1]  # Caractéristiques du visage (toutes les valeurs sauf la dernière)
#         image_path = item[-1]  # Chemin d'accès à l'image (dernière valeur)
#         known_face_encodings.append(np.array(face_encoding, dtype=np.float64))  # Convertir en tableau numpy de float64
#         image_paths.append(image_path)
    
#     # Encoder les caractéristiques faciales de l'image entrante
#     input_encoding = face_recognition.face_encodings(input_image)[0]
    
#     # Convertir l'encodage d'entrée en tableau numpy de float64
#     input_encoding = np.array(input_encoding, dtype=np.float64)
    
#     # Calculer la distance euclidienne entre l'encodage d'entrée et les encodages de la base de données
#     distances = np.linalg.norm(known_face_encodings - input_encoding, axis=1)
    
#     # Trouver l'index de l'image avec la distance minimale
#     min_distance_index = np.argmin(distances)
    
#     # Récupérer le chemin d'accès à l'image correspondante
#     matching_image_path = []
#     matching_image_path.append(image_paths[min_distance_index])

    
#     return matching_image_path



def find_similar_images(input_image):
    input_image = cv2.imread(input_image)
    
    # Charger la base de données d'images et d'encodages
    database = np.load('Faces_Signatures_db.npy', allow_pickle=True)
    
    # Extraire les caractéristiques faciales et les chemins d'accès aux images de la base de données
    known_face_encodings = []
    image_paths = []
    for item in database:
        face_encoding = item[:-1]  # Caractéristiques du visage (toutes les valeurs sauf la dernière)
        image_path = item[-1]  # Chemin d'accès à l'image (dernière valeur)
        known_face_encodings.append(np.array(face_encoding, dtype=np.float64))  # Convertir en tableau numpy de float64
        image_paths.append(image_path)
    
    # Encoder les caractéristiques faciales de l'image entrante
    input_encoding = face_recognition.face_encodings(input_image)[0]
    
    # Convertir l'encodage d'entrée en tableau numpy de float64
    input_encoding = np.array(input_encoding, dtype=np.float64)
    
    # Comparer les caractéristiques faciales avec la base de données
    matches = face_recognition.compare_faces(known_face_encodings, input_encoding)
    
    # Récupérer les chemins d'accès aux images correspondantes
    matching_image_paths = [image_paths[i] for i, match in enumerate(matches) if match]
    
    return matching_image_paths
