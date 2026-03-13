# QR Code Generator (Python)

Simple Python project that generates a QR code from a text or a URL and lets the user choose where to save the image.

This project uses the **qrcode** library to generate the QR code and **tkinter** to open a file dialog so the user can select the save location.

---

## Features

* Generate a QR code from any text or URL
* Save the image as a **PNG file**
* File explorer window to choose where to save the QR code
* Works from the terminal
* Automatically keeps the save window on top (Windows)

---

## Technologies Used

* Python
* qrcode
* Pillow
* Tkinter

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

2. Install the required library

```bash
pip install qrcode[pil]
```

---

## Usage

Run the script:

```bash
python qr_generator.py
```

Then:

1. Enter a **text or URL** in the terminal.
2. A window will appear asking where you want to save the QR code.
3. Choose a location and the image will be saved as a `.png` file.

Example:

```
Enter a text or URL: https://github.com
```

The program will generate a QR code and save it to the selected location.

---

## Author

Samy BOUSSAD
