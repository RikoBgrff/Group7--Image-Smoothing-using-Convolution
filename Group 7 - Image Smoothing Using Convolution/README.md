Image Smoothing Using Convolution – README

This project demonstrates convolution-based image smoothing using Gaussian and Box (mean) filters. It was developed for the EEE309 / EEE311 Signals and Systems Interdisciplinary Term Project.

📁 Project Structure
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
    ├── GROUP7 - Image Smoothing using Convolution.docx
    └── GROUP7 - Image Smoothing using Convolution.pdf

code/

Contains:

main.py → Python implementation of the convolution-based smoothing

assets/ → input image and all automatically generated output images

code/assets/

realPhoto.jpg → the original input image

Generated outputs:

resized_500x500.jpg

grayscale.jpg

gaussian_filtered.jpg

box_filtered.jpg

documents/

Contains the official project report in both formats:

GROUP7- Image Smoothing using Convolution.docx

GROUP7- Image Smoothing using Convolution.pdf

🚀 How to Run the Project
1. Extract the ZIP File

Unzip the folder named:

Image Smoothing Using Convolution

2. Open the Project in Visual Studio Code

Open VS Code

Press Ctrl + K, then O

Select the Image Smoothing Using Convolution folder

3. Install Required Python Libraries

Open the terminal:

Press Ctrl + J (or Ctrl + `)

Install dependencies:

pip install pillow matplotlib


If Python 3 specifically is required:

pip3 install pillow matplotlib

4. Run the Python Script

Navigate to the code folder (if needed):

cd code


Then run:

python main.py


or

python3 main.py

📤 Output

Upon running the script, all processed images will be saved in:

code/assets/


Generated files:

resized_500x500.jpg

grayscale.jpg

gaussian_filtered.jpg

box_filtered.jpg

A visualization window will also appear displaying all 4 results.

🛠️ Tools & Technologies

Python

Pillow (PIL)

Matplotlib

Visual Studio Code

📚 Project Documentation

Located in the documents/ folder:

GROUP7 - Image Smoothing using Convolution.docx

GROUP7 - Image Smoothing using Convolution.pdf