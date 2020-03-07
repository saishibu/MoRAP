# import libraries
import cv2
import face_recognition

# Get a reference to webcam 
video_capture = cv2.VideoCapture("/home/wnaadmin/Downloads/video.mp4")
input_movie = cv2.VideoCapture("/home/wnaadmin/Downloads/video.mp4")
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize variables
face_locations = []
frame_number = 0

codec = int(input_movie.get(cv2.CAP_PROP_FOURCC))
fps = int(input_movie.get(cv2.CAP_PROP_FPS))
frame_width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
output_movie = cv2.VideoWriter("output.mp4", codec, fps, (frame_width,frame_height))


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    frame_number += 1
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
output_movie.release()
cv2.destroyAllWindows()
