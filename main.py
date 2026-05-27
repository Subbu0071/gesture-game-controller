import cv2
from core.hand_detector import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector()

while True:

    success, img = cap.read()

    if not success:
        break

    img, landmarks = detector.detect_hands(img)

    if landmarks:

        fingers = detector.fingers_up(landmarks)

        print(fingers)

    cv2.imshow("Gesture Game Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()