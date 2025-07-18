import cv2
import numpy as np
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

ocr_config = '--oem 1 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

image_folder = 'captured'

def auto_crop(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blur, 100, 200)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w * h > 5000:
            return image[y:y + h, x:x + w]
    return image

def preprocess_image(img):
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    dilated = cv2.dilate(binary, np.ones((2, 2), np.uint8), iterations=1)
    return dilated

for filename in os.listdir(image_folder):
    if filename.lower().endswith('.jpg'):
        img_path = os.path.join(image_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            img = auto_crop(img)
            processed_img = preprocess_image(img)

            text = pytesseract.image_to_string(processed_img, config=ocr_config)
            cleaned_text = text.replace('\n', '').replace(' ', '').replace('|', '').strip()

            print(f"{filename} → {cleaned_text}")

        else:
            print(f"{filename} → ❌ Failed to load image")
