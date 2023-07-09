```python
import cv2
from file_manager import updateFile, userFiles

def processVideo(file_id, crop=None, resolution=None):
    """
    Function to process video files. It can crop the video and adjust its resolution.
    """
    # Find the file in the userFiles
    for file in userFiles:
        if file['id'] == file_id and file['type'] == 'video':
            video = file
            break
    else:
        print("File not found.")
        return

    # Load the video
    cap = cv2.VideoCapture(video['path'])

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error opening video file.")
        return

    # Get original video's width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # If crop is specified, adjust frame width and height
    if crop:
        x, y, w, h = crop
        frame_width = w
        frame_height = h

    # If resolution is specified, adjust frame width and height
    if resolution:
        frame_width, frame_height = resolution

    # Define the codec and create a VideoWriter object
    out = cv2.VideoWriter('processed_video.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # If crop is specified, crop the frame
            if crop:
                x, y, w, h = crop
                frame = frame[y:y+h, x:x+w]

            # Write the frame into the file 'processed_video.avi'
            out.write(frame)

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything when job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Update the file in userFiles
    video['path'] = 'processed_video.avi'
    updateFile(video)
```