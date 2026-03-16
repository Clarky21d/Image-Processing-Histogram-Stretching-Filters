# Traitement d'Images : Histogrammes & Filtres Spatiaux

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-orange)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-red)
![TP](https://img.shields.io/badge/TP-Image%20Processing-brightgreen)

## 📋 Table des Matières

* [Description](#description)
* [Structure du Projet](#structure-du-projet)
* [Partie 1 : Histogramme et Opérations Pixel](#partie-1--histogramme-et-opérations-pixel)
* [Partie 2 : Filtres Spatiaux et Débruitage](#partie-2--filtres-spatiaux-et-débruitage)
* [Installation](#installation)
* [Utilisation](#utilisation)
* [Résultats](#résultats)

---

## 📖 Description

Ce dépôt contient les solutions complètes d'un Travail Pratique universitaire en **Traitement d'Images et Vision par Ordinateur**.
Le projet explore les concepts fondamentaux à travers deux parties principales avec des implémentations pratiques en Python.

### Objectifs pédagogiques

* Manipulation des histogrammes et amélioration du contraste
* Étude quantitative du contraste (Michelson, RMS)
* Génération et analyse de différents types de bruit
* Application et comparaison de filtres spatiaux
* Évaluation objective par métrique **PSNR**

---

## 📂 Structure du Projet

```
Image-Processing-Histogram-Stretching-Filters/
│
├── Histogramme_etOperations_Pixel/
│   ├── lecture_image.py
│   ├── histogramme.py
│   ├── etirement_histogramme.py
│   ├── egalisation_histogramme.py
│   └── contraste_metrics.py
│
├── Filtres_Spatials/
│   ├── bruit_gaussien.py
│   ├── bruit_poivre_sel.py
│   ├── filtre_moyenneur.py
│   ├── filtre_median.py
│   ├── filtre_gaussien.py
│   └── calcul_psnr.py
│
├── images/
│   ├── originales/
│   │   ├── aqui.pgm
│   │   ├── pont.pgm
│   │   ├── Loup-noir.jpg
│   │   └── cameraman.tif
│   ├── bruitees/
│   └── resultats/
│
├── docs/
│   ├── TP1- Hist-OpPxl-FiltreSpacial.pdf
│   └── Rapport TP1.pdf
│
├── requirements.txt
└── README.md
```

---

## 🖼️ Partie 1 : Histogramme et Opérations Pixel

### Fonctionnalités implémentées

#### 1. Lecture d'Image

* Chargement d'images **PGM, JPG, TIFF**
* Conversion en niveaux de gris
* Affichage des métadonnées (dimensions, type, valeurs min/max)

#### 2. Calcul d'Histogramme

* Calcul de la distribution des niveaux de gris
* Visualisation avec **Matplotlib**
* Deux méthodes : **OpenCV** et **NumPy**

#### 3. Étirement d'Histogramme

* Identification des valeurs min et max
* Étirement linéaire sur la plage **[0,255]**
* Sauvegarde de l'image transformée

#### 4. Égalisation d'Histogramme

* Calcul de l'histogramme cumulé
* Répartition uniforme des niveaux de gris
* Amélioration automatique du contraste

#### 5. Mesures de Contraste

* **Michelson** : (Imax − Imin) / (Imax + Imin)
* **RMS** : écart-type des niveaux de gris
* Comparaison avant / après traitement

---

## 🎨 Partie 2 : Filtres Spatiaux et Débruitage

### Fonctionnalités implémentées

#### 1. Génération de Bruit

* **Bruit gaussien** : variance variable (σ² = 0.01, 0.05, 0.1)
* **Bruit sel et poivre** : p = 0.05, 0.1, 0.2
* **Bruit speckle** : bruit multiplicatif

#### 2. Filtre Moyenneur

* Masques **3×3, 5×5, 7×7, 9×9**
* Lissage par moyenne des pixels voisins
* Analyse de l’impact de la taille du filtre

#### 3. Filtre Médian

* Filtre **non linéaire**
* Très efficace contre le **bruit sel et poivre**
* Préserve mieux les contours

#### 4. Filtre Gaussien

* Lissage avec distribution gaussienne
* Paramètre **σ ajustable**
* Meilleure conservation des détails

#### 5. Calcul du PSNR

* Mesure objective de qualité
* Comparaison image originale / image filtrée
* Bon résultat : **PSNR > 20 dB**

---

## 🚀 Installation

```bash
# Cloner le dépôt
git clone https://github.com/Clarky21d/Image-Processing-Histogram-Stretching-Filters.git

# Aller dans le dossier
cd Image-Processing-Histogram-Stretching-Filters


---

## ▶️ Utilisation

Exemple :

```bash
python histogramme.py
python etirement_histogramme.py
python filtre_median.py
```

---

## 📊 Résultats

Les résultats des traitements sont sauvegardés dans :

```
images/resultats/
```

Ils incluent :

* images étirées
* images égalisées
* images bruitées
* images débruitées
* comparaison PSNR

---

## 👨‍💻 Auteurs

Projet réalisé dans le cadre d’un **TP universitaire en Vision par Ordinateur**.


