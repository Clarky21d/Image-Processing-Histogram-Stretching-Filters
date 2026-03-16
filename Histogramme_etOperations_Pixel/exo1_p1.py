import cv2
import numpy as np
import matplotlib.pyplot as plt
# list des chemins d'images à traiter
images = [
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/aqui.pgm",
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/pont.pgm",
    "D:/TP VO/TP1/Histogramme_etOperations_Pixel/images/Loup-noir.jpg"
]
# boucle pour traiter chaque image
for path in images:

    print("\nTraitement de :", path)
    img = cv2.imread(path, 0)

    if img is None:
        print("Erreur : image non trouvée")
        continue

    # affichage de l'histogramme original
    plt.figure()
    plt.hist(img.ravel(), bins=256)
    plt.title("Histogramme original")
    plt.show()

    # calcul de Imin et Imax
    Imin = img.min()
    Imax = img.max()

    print("Imin =", Imin)
    print("Imax =", Imax)

    # étirement de l'histogramme
    img_stretch = (img - Imin) * (255 / (Imax - Imin))
    img_stretch = img_stretch.astype(np.uint8)

    # sauvegarde de l'image étirée
    name = path.split("/images_etire/")[-1]
    output_name = "etire_" + name
    cv2.imwrite(output_name, img_stretch)

    # affichage de l'histogramme étiré
    plt.figure()
    plt.hist(img_stretch.ravel(), bins=256)
    plt.title("Histogramme étiré")
    plt.show()

   # calcul du contraste de Michelson
    michelson = (Imax - Imin) / (Imax + Imin)
    print("Contraste Michelson =", michelson)

 
    mean = np.mean(img)

    rms = np.sqrt(np.mean((img - mean)**2))

    print("Contraste RMS =", rms)