import cv2
import matplotlib.pyplot as plt
import numpy as np

I = cv2.imread("D:/TP VO/TP1//Filtres_Spatials/images/cameraman.tif", cv2.IMREAD_GRAYSCALE)

# Vérifier l'image
plt.imshow(I, cmap='gray')
plt.title("Image originale")
plt.axis('off')
plt.show()

#Ajouter du bruit gaussien
def add_gaussian_noise(image, sigma2):
    # image normalisée entre 0 et 1
    image_norm = image / 255.0
    gauss = np.random.normal(0, np.sqrt(sigma2), image_norm.shape)
    noisy = image_norm + gauss
    # revenir à l'échelle 0-255
    noisy = np.clip(noisy, 0, 1) * 255
    return noisy.astype(np.uint8)

I2 = add_gaussian_noise(I, sigma2=0.01)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(I, cmap='gray')
plt.title("Originale")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(I2, cmap='gray')
plt.title("Bruit Gaussien σ²=0.01")
plt.axis('off')
plt.show()

# ajouter du bruit poivre et sel
def add_salt_pepper_noise(image, amount):
    noisy = image.copy()
    # nombre de pixels à modifier
    num_salt = np.ceil(amount * image.size * 0.5).astype(int)
    num_pepper = np.ceil(amount * image.size * 0.5).astype(int)
    
    # pixels "sel" (blanc)
    coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[coords[0], coords[1]] = 255
    
    # pixels "poivre" (noir)
    coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1]] = 0
    
    return noisy

I3 = add_salt_pepper_noise(I, amount=0.05)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(I, cmap='gray')
plt.title("Originale")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(I3, cmap='gray')
plt.title("Bruit Poivre et Sel p=0.05")
plt.axis('off')
plt.show()


#comparison des trois images
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)  
plt.imshow(I, cmap='gray')
plt.title("Image originale")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(I2, cmap='gray')
plt.title("Bruit Gaussien σ²=0.01")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(I3, cmap='gray')
plt.title("Bruit Poivre et Sel p=0.05")
plt.axis('off')
plt.show()