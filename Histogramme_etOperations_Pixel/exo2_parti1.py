import cv2
import numpy as np
import matplotlib.pyplot as plt

# Liste des images
images = [
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/aqui.pgm",
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/pont.pgm",
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/Loup-noir.jpg"
]

for path in images:

    print("Traitement de :", path)

    # Charger image en gris
    img = cv2.imread(path, 0)

    if img is None:
        print("Erreur chargement")
        continue

    # Histogramme original
    plt.hist(img.ravel(), 256)
    plt.title("Histogramme original")
    plt.show()

    # Egalisation d'histogramme
    img_eq = cv2.equalizeHist(img)

    # Sauvegarder image
    name = path.split("/images_egalise")[-1]
    cv2.imwrite("egalise_" + name, img_eq)

    # Histogramme après égalisation
    plt.hist(img_eq.ravel(), 256)
    plt.title("Histogramme egalise")
    plt.show()

    # Min et Max
    Imin = img_eq.min()
    Imax = img_eq.max()

    print("Imin =", Imin)
    print("Imax =", Imax)

    # Contraste Michelson
    michelson = (Imax - Imin) / (Imax + Imin)
    print("Michelson =", michelson)

    # Contraste RMS
    mean = np.mean(img_eq)
    rms = np.sqrt(np.mean((img_eq - mean)**2))
    print("RMS =", rms)