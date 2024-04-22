import cv2

def main():
    # Open the video file
    cap = cv2.VideoCapture(0)

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Set up RTSP server
    rtsp_url = 'rtsp://localhost:8554/live'
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter(
        filename=rtsp_url,
        fourcc=cv2.VideoWriter.fourcc(*'H264'),
        fps=fps,
        frameSize=(width, height)
                          )
    # out = cv2.VideoWriter(rtsp_url, fourcc, fps, (width, height))

    # Read and stream frames
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # out.write(frame)

    # Release resources
    cap.release()
    #out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
