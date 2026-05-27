class GestureController:

    def detect_gesture(self, fingers):

        # No hand detected
        if len(fingers) == 0:
            return "NO HAND"

        # Fist
        if fingers == [0, 0, 0, 0, 0]:
            return "SLIDE"

        # Index finger
        elif fingers == [0, 1, 0, 0, 0]:
            return "JUMP"

        # Peace sign
        elif fingers == [0, 1, 1, 0, 0]:
            return "RIGHT"

        # Open palm
        elif fingers == [1, 1, 0, 0, 0]:
            return "LEFT"

        else:
            return "UNKNOWN"