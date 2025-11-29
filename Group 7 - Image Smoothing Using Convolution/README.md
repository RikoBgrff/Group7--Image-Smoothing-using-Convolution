# Image Smoothing Using Convolution

This repository contains the full implementation and documentation for the **Image Smoothing Using Convolution** project, developed as part of the **EEE309 / EEE311 Signals and Systems Interdisciplinary Term Project**.  
The project demonstrates the application of **convolution-based filters** (Gaussian and Box) to smooth a real-world image using Python.

---

## Project Structure

```
Image Smoothing Using Convolution/
│
├── code/
│   ├── main.py
│   ├── assets/
│   │   ├── realPhoto.jpg
│   │   ├── resized_500x500.jpg
│   │   ├── grayscale.jpg
│   │   ├── gaussian_filtered.jpg
│   │   └── box_filtered.jpg
│
└── documents/
    ├── GROUP7- Image Smoothing using Convolution.docx
    └── GROUP7- Image Smoothing using Convolution.pdf
```

---

## Overview

This project focuses on **image smoothing** using two classical convolutional filtering techniques:

### Gaussian Smoothing
Uses a Gaussian kernel to produce smooth, natural blur while preserving structure.

### Box (Mean) Smoothing
Uses an averaging kernel to uniformly smooth local regions.

The Python script processes an input image by:
1. Resizing it to 500×500  
2. Converting it to grayscale  
3. Applying Gaussian smoothing  
4. Applying Box (mean) smoothing  
5. Saving the processed images  

---

## Requirements

- Python 3.x  
- Pillow  
- Matplotlib  

Install dependencies:

```
pip install pillow matplotlib
```

---

## How to Run

1. Download or clone the repository.
2. Open the project in Visual Studio Code.
3. Open the terminal (Ctrl + J).
4. Navigate to the code folder:

```
cd code
```

5. Run the script:

```
python main.py
```

or

```
python3 main.py
```

All output images will appear inside `code/assets/`.

---

## Documentation

The full project report is included in the `documents/` folder:

- `GROUP7- Image Smoothing using Convolution.docx`
- `GROUP7- Image Smoothing using Convolution.pdf`

---

## Purpose

This repository provides a clean, structured, and reproducible implementation of convolution-based image smoothing.  
It is intended for educational use and as a reference for students studying signal processing and image filtering.

---
