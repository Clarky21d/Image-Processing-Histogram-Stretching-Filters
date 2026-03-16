import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fonction PSNR
def PSNR(original, denoised):
    mse = np.mean((original - denoised) ** 2)
    if mse == 0:
        return 100
    return 10 * np.log10(1 / mse)

# Bruit sel et poivre
def salt_pepper_noise(image, p):
    noisy = image.copy()
    total_pixels = image.size
    
    num_salt = int(p * total_pixels / 2)
    num_pepper = int(p * total_pixels / 2)

    # sel
    coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[coords[0], coords[1]] = 1

    # poivre
    coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1]] = 0

    return noisy


img = cv2.imread("D:/TP VO/TP1//Filtres_Spatials/images/cameraman.tif", cv2.IMREAD_GRAYSCALE)
img = img / 255.0


noisy = salt_pepper_noise(img, 0.05)

sizes = [3,5,7,9]

psnr_avg = []
psnr_gauss = []
psnr_median = []


for s in sizes:

    # filtre moyenne
    avg = cv2.blur(noisy,(s,s))
    psnr_avg.append(PSNR(img,avg))

    # filtre gaussien
    gauss = cv2.GaussianBlur(noisy,(s,s),0)
    psnr_gauss.append(PSNR(img,gauss))

    # filtre median
    median = cv2.medianBlur((noisy*255).astype(np.uint8),s)
    median = median/255.0
    psnr_median.append(PSNR(img,median))


plt.plot(sizes, psnr_avg, marker='o', label="Filtre moyenne")
plt.plot(sizes, psnr_gauss, marker='o', label="Filtre gaussien")
plt.plot(sizes, psnr_median, marker='o', label="Filtre médian")

plt.xlabel("Taille du filtre")
plt.ylabel("PSNR (dB)")
plt.title("PSNR en fonction de la taille du filtre")

plt.legend()
plt.grid()
plt.show()