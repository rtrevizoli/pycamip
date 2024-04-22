import cv2
from flask import Flask, Response

app = Flask(__name__)

class VideoProperties:
    def __init__(self, cam) -> None:
        self.width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(cam.get(cv2.CAP_PROP_FPS))
        self.rtsp_url = 'rtsp://localhost:8554/live'
        self.fourcc = cv2.VideoWriter_fourcc(*'H264')

class RTSPServer(cv2.VideoWriter):
    def __init__(self, properties) -> cv2.VideoWriter:
        super().__init__(
            properties.rtsp_url,
            properties.fourcc,
            properties.fps,
            (properties.width, properties.height)
        )

def main():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print(f"Error | Failed to open camera")
        return 0
    
    properties = VideoProperties(cam)

    rtsp_server = RTSPServer(properties)

    while cam.isOpened():
        ret, frame = cam.read()

        if not ret:
            continue

        rtsp_server.write(frame)
    
    cam.release()
    rtsp_server.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()