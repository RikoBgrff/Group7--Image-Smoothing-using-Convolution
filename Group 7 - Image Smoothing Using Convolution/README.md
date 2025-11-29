Image Smoothing Using Convolution

This repository contains the full implementation and documentation for the "Image Smoothing Using Convolution" project, developed as part of the EEE309 / EEE311 Signals and Systems Interdisciplinary Term Project. The aim of the project is to apply convolution-based smoothing techniques to a real-world image using Python.

Project Structure
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

Description

This project demonstrates the use of convolution for image smoothing by applying two filtering techniques:

Gaussian Smoothing

Box (Mean) Smoothing

The Python script resizes the input image, converts it to grayscale, applies both filters, and saves the resulting output images.

Requirements

Python 3.x
Required libraries:

Pillow

Matplotlib

Install dependencies with:

pip install pillow matplotlib

How to Run

Clone or download the repository.

Open the project folder in Visual Studio Code.

Open the terminal inside VS Code.

Navigate to the code folder:

cd code


Run the script:

python main.py


Or if required:

python3 main.py


Processed images will be saved in code/assets/.

Documentation

The complete project report is located in the documents folder:

GROUP7- Image Smoothing using Convolution.docx

GROUP7- Image Smoothing using Convolution.pdf

Purpose

This repository serves as a structured, reproducible, and academically aligned example of convolution-based filtering in Python for noise reduction and image preprocessing.
