import cv2
from gaze_tracking import GazeTracking
import pyautogui
pyautogui.FAILSAFE = False

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
x, y = 500, 500
# arrX = []
# arrY = []
while True:
    # We get a new frame from the webcam
    

    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # mouse
    try:
        x = 1920 - gaze.horizontal_ratio() * 1920
        y = gaze.vertical_ratio() * 1080
        if x > 990:
            x *= 1.48 * 1.1
        elif x < 300:
            x /= 258
        if y < 540:
            y /= 430
        arrX.append(x)
        arrY.append(y)
    except:
        pass
    pyautogui.moveTo(x, y)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
    # print("maxes:\t", max(arrX), max(arrY))
    # print("mins:\t", min(arrX), min(arrY))


webcam.release()
cv2.destroyAllWindows()
