# Number Plate Detection 🚗🔍

A simple Python-based project to detect vehicle number plates using OpenCV and Tesseract OCR.

## 📁 Project Structure

```
Number_Plate_Detection/
├── capture/               # Folder where captured number plate images are saved
├── number_plate.py        # Main script to run number plate detection
├── ocr.py                 # Extracts text (number) from the plate using OCR
├── model (haarcascade_russian_plate_number.xml)  # Haar Cascade classifier
├── README.md              # Project documentation
```

---

## ⚙️ Requirements

Make sure you have [Anaconda](https://www.anaconda.com/) installed.

Create and activate environment:

```bash
conda create -n npd-env python=3.10
conda activate npd-env
```

Install dependencies:

```bash
pip install opencv-python pytesseract
```

Make sure Tesseract-OCR is installed on your system. Download from:

👉 [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

> **Note:** After installing, set the correct path in your code if needed (example in `ocr.py`).

---

## 🚀 How to Run

1. **Detect and capture number plate**
   Run the main script:

   ```bash
   python number_plate.py
   ```

2. **Extract text from image**
   Run the OCR script:

   ```bash
   python ocr.py
   ```

---

## 📸 Output

Captured number plate images will be saved in the `capture/` folder.

---

## 🧹 Cleaning Up

To replace old images:

* Delete all files from `capture/` folder.
* New captures will overwrite the folder on the next run.

---

## 📌 Notes

* Works best in good lighting and clear plate visibility.
* You can improve detection by training a custom classifier or using YOLO-based models.

---

## 🧑‍💻 Author

**Adarsh Gyan Priyadarshi**
GitHub: [adarshgyan](https://github.com/adarshgyan)
