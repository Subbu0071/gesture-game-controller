import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

        self.mp_draw = mp.solutions.drawing_utils

        # Fingertip landmark IDs
        self.tip_ids = [4, 8, 12, 16, 20]

    def detect_hands(self, image):

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_image)

        landmarks_list = []

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_draw.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                for id, landmark in enumerate(hand_landmarks.landmark):

                    h, w, c = image.shape

                    cx = int(landmark.x * w)
                    cy = int(landmark.y * h)

                    landmarks_list.append((id, cx, cy))

        return image, landmarks_list

    def fingers_up(self, landmarks_list):

        fingers = []

        if len(landmarks_list) == 0:
            return fingers

        # Thumb
        if landmarks_list[self.tip_ids[0]][1] > landmarks_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        for id in range(1, 5):

            if landmarks_list[self.tip_ids[id]][2] < landmarks_list[self.tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers