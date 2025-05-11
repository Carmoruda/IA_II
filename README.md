# 🧠 Inteligencia Artificial II - Prácticas 2024/25

Repositorio correspondiente a la asignatura **Inteligencia Artificial II**, compuesto por prácticas centradas en el desarrollo de modelos neuronales, mapas autoorganizados, redes profundas y algoritmos genéticos.
Todas las prácticas se han desarrollado en Python utilizando `NumPy`, `PyTorch`, `matplotlib`, `pandas` y otros recursos específicos.

---

## 📌 Contenido por Laboratorio

### 🟡 LAB01 - Mapas Autoorganizados (SOM)

-   **Práctica 1:** _Clasificación de colores RGB_ 🎨
    Implementación de una red SOM desde cero para agrupar colores aleatorios en el espacio RGB. Incluye visualización de pesos y mapas de clasificación, activación y distancia.

-   **Práctica 2:** _Clasificación de Pokémon_ 🧬
    Adaptación del modelo SOM para clasificar Pokémon en función de su resistencia a distintos tipos de ataque. Entrenamiento y análisis de agrupaciones.

---

### 🟠 LAB02 - Modelos neuronales supervisados

-   **Práctica 1:** _Perceptrón para funciones lógicas_ 🔗
    Implementación manual del algoritmo Perceptrón desde cero para resolver funciones AND y XOR. Comparación de learning rates y umbrales.

-   **Práctica 2:** _MLP para funciones no lineales_ 🧮
    Uso de **PyTorch** para construir redes multicapa (MLP) capaces de resolver XOR. Comparación de funciones de activación y arquitecturas.

-   **Práctica 3:** _Predicción de muertes en Juego de Tronos_ ⚔️
    Aplicación de un MLP para predecir la probabilidad de muerte de personajes de GoT. Análisis de pesos, entradas relevantes y predicciones modificadas.

---

### 🔵 LAB03 - Deep Learning (CNN)

-   **Práctica 1:** _Clasificador de frutas y verduras_ 🍎🥦
    Creación de una red convolucional (CNN) para clasificar imágenes RGB del dataset Fruits and Vegetables. Entrenamiento con distintas arquitecturas y evaluación de precisión.

-   **Práctica 2:** _Detección de neumonía en radiografías_ 🩻
    Clasificación binaria (Normal/Pneumonía) y multiclase (Bacteriana/Vírica/Normal) a partir de imágenes de rayos X. Uso de técnicas de augmentación y análisis de errores.

---

### 🟢 LAB04 - Algoritmos Genéticos

-   **Práctica 1:** _Generación de frases con mutaciones_ 🧬
    Implementación de un algoritmo genético que busca reconstruir una frase objetivo mediante mutaciones y selección probabilística.

-   **Práctica 2:** _Algoritmo genético con elitismo_ 👑
    Mejora del algoritmo anterior añadiendo elitismo. Evaluación de convergencia, mejores porcentajes de selección y comparación de resultados con y sin elitismo.

---

## 📂 Estructura de carpetas

```bash
📁 IA_II
├── 📁 Practica 1
│   ├── L1P1-SOM_colores-resultado.ipynb
│   ├── L1P2-SOM_pokemon-resultado.ipynb
│   ├── LAB01 SOM 24-25.pdf
│   ├── data
│   │   ├── pokemon_classified.csv
│   │   ├── pokemon_classify.csv
│   │   └── pokemon_train.csv
│   ├── media
│   │   ├── comparación_mejores_valores_rango_persona_1_pokemon.png
│   │   ├── comparación_mejores_valores_rango_persona_2_pokemon.png
│   │   └── comparación_mejores_valores.png
│   └── README.md
├── 📁 Practica 2
│   ├── L2P1-Perceptron.ipynb
│   ├── L2P2-MLP.ipynb
│   ├── L2P3-MLP_GoT.ipynb
│   ├── LAB02 PMC 24-25.pdf
│   ├── data
│   │   ├── got_predict.csv
│   │   ├── got_train.csv
│   │   └── tutorial-pytorch.ipynb
│   ├── media
│   │   ├── Estrucutra perceptrón.png
│   │   └── red_neuronal.png
│   ├── output
│   │   ├── L2P1-Perceptron.csv
│   │   └── red_neuronal
│   └── utils
│       └── grafica.py
├── 📁 Practica 3
│   ├── L3P1-FandV.ipynb
│   ├── L3P2-Pneumonia.ipynb
│   ├── LAB03 DL 24-25.pdf
│   ├── data
│   │   ├── FandV
│   │   └── Pneumonia
│   ├── media
│   │   ├── Arquitectura cnn.png
│   │   └── Estructura cnn.png
│   └── output
│       ├── FandV
│       └── Pneumonia
├── 📁 Practica 4
│   ├── L4P1-Frase.ipynb
│   ├── L4P2-Frase_Elite.ipynb
│   └── LAB04 AG 24-25.pdf
├── .gitignore
└── README.md
```

> 📌 **Notas:**
>
> -   La estructura de carpetas está organizada por laboratorio. Cada práctica es independiente y contiene los pasos detallados para su ejecución.

---

## 📬 Contacto

Para dudas o sugerencias, por favor deja una issue en este repositorio.
