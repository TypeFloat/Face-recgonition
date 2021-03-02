import cv2
import base64


def capture_photo():

    """
    Take photo and save.
    Take photo from camero with pressing 'c' and exit with pressing 'q'.
    """

    capture = cv2.VideoCapture(0)

    width = 640
    height = 480
    w = 360

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    crop_w_start = (width - w) // 2
    crop_h_start = (height - w) // 2

    while 1:
        ret, frame = capture.read()
        frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
        frame = cv2.flip(frame, 1, dst=None)
        cv2.imshow('capture', frame)
        event = cv2.waitKey(1)
        if event == ord('c'):
            cv2.imwrite('photo.png', cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA))
            break


def image_read(filename):
    f = open(filename, 'rb')
    image = f.read()
    image = base64.b64encode(image)
    return image