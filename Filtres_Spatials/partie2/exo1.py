import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# lire image
I = cv2.imread("D:/TP VO/TP1//Filtres_Spatials/images/cameraman.tif", 0) / 255.0

# ajouter bruit gaussien
sigma2 = 0.01
noise = np.random.normal(0, np.sqrt(sigma2), I.shape)
I_noisy = I + noise
I_noisy = np.clip(I_noisy, 0, 1)

# filtre moyenne 5x5
kernel_avg = np.ones((5,5)) / 25
I_avg = convolve2d(I_noisy, kernel_avg, mode='same')

# masque donné (1/81)
kernel_custom = np.ones((5,5)) / 81
I_custom = convolve2d(I_noisy, kernel_custom, mode='same')

# différence entre les deux images
diff = I_avg - I_custom

# affichage
plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.imshow(I, cmap='gray')
plt.title("Image originale")

plt.subplot(2,2,2)
plt.imshow(I_noisy, cmap='gray')
plt.title("Image bruitée")

plt.subplot(2,2,3)
plt.imshow(I_avg, cmap='gray')
plt.title("Filtre moyenne 5x5")

plt.subplot(2,2,4)
plt.imshow(I_custom, cmap='gray')
plt.title("Filtre masque 1/81")

plt.figure()
plt.imshow(diff, cmap='gray')
plt.title("Soustraction des deux images")

plt.show()