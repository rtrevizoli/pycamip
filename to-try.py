import cv2
import subprocess

def generate_frames():
    cap = cv2.VideoCapture(0)  # Change to your camera index or video source

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to bytes
        ret, frame_bytes = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        # Write frame to stdout (pipe to ffmpeg)
        frame_bytes.tofile('/proc/self/fd/1')  # Write to stdout (pipe)

    cap.release()

# Command to run ffmpeg for streaming
ffmpeg_cmd = [
    'ffmpeg', '-f', 'image2pipe', '-i', '-', '-c:v', 'libx264', '-preset', 'ultrafast',
    '-tune', 'zerolatency', '-f', 'rtsp', 'rtsp://localhost:8554/live'
]

# Start subprocess to run ffmpeg
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

# Start generating frames
generate_frames()

# Close stdin to signal ffmpeg process to terminate
ffmpeg_process.stdin.close()
