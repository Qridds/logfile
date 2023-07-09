```python
import cv2

def processVideo(file):
    # Load the video
    video = cv2.VideoCapture(file)

    # Check if video opened successfully
    if not video.isOpened(): 
        print("Error opening video file")

    # Read until video is completed
    while(video.isOpened()):
      
      # Capture frame-by-frame
      ret, frame = video.read()
      if ret == True:
 
        # Display the resulting frame
        cv2.imshow('Frame', frame)
 
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
 
      # Break the loop
      else: 
        break
   
    # When everything done, release the video capture object
    video.release()
   
    # Closes all the frames
    cv2.destroyAllWindows()

def cropVideo(file, x, y, w, h):
    # Load the video
    video = cv2.VideoCapture(file)

    # Check if video opened successfully
    if not video.isOpened(): 
        print("Error opening video file")

    # Read until video is completed
    while(video.isOpened()):
      
      # Capture frame-by-frame
      ret, frame = video.read()
      if ret == True:
 
        # Crop the frame
        crop_frame = frame[y:y+h, x:x+w]

        # Display the resulting frame
        cv2.imshow('Frame', crop_frame)
 
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
 
      # Break the loop
      else: 
        break
   
    # When everything done, release the video capture object
    video.release()
   
    # Closes all the frames
    cv2.destroyAllWindows()

def adjustResolution(file, width, height):
    # Load the video
    video = cv2.VideoCapture(file)

    # Check if video opened successfully
    if not video.isOpened(): 
        print("Error opening video file")

    # Set the video resolution
    video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Read until video is completed
    while(video.isOpened()):
      
      # Capture frame-by-frame
      ret, frame = video.read()
      if ret == True:
 
        # Display the resulting frame
        cv2.imshow('Frame', frame)
 
        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
 
      # Break the loop
      else: 
        break
   
    # When everything done, release the video capture object
    video.release()
   
    # Closes all the frames
    cv2.destroyAllWindows()
```