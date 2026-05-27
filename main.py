import cv2

from core.hand_detector import HandDetector
from core.gesture_logic import GestureController

cap = cv2.VideoCapture(0)

detector = HandDetector()

gesture_controller = GestureController()

while True:

    success, img = cap.read()

    if not success:
        break

    img, landmarks = detector.detect_hands(img)

    if landmarks:

        fingers = detector.fingers_up(landmarks)

        gesture = gesture_controller.detect_gesture(fingers)

        print(gesture)

        cv2.putText(
            img,
            gesture,
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            3
        )

    cv2.imshow("Gesture Game Controller", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()