import cv2

# Load Haar cascade
harcascade = "model/haarcascade_russian_plate_number.xml"
plate_cascade = cv2.CascadeClassifier(harcascade)

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=7)

    roi_found = False
    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            roi_found = True
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
            img_roi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        if roi_found:
            filename = f"captured/scanned_plate_{count}.jpg"
            cv2.imwrite(filename, img_roi)
            print(f"Image saved: {filename}")
            cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "Captured!", (150, 260), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.imshow("Result", img)
            cv2.waitKey(500)
            count += 1
        else:
            print("⚠️ No number plate detected to capture.")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
