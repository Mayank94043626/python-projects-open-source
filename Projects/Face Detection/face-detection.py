import cv2
 
# Get the camera object
cam = cv2.VideoCapture(0)

# Initialize the haar cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Main Loop
while True:
    # Read the frame from the camera
    _, frame = cam.read()

    # Convert the frame into grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect all the faces in the grayscale frame
    faces = face_cascade.detectMultiScale(frame_gray, 1.3, 5)

    # Draw a blue rectangle for each face in the frame
    for x, y, width, height in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

    # Display the frame
    cv2.imshow("image", frame)

    # Quit button
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
