from easytello import tello
my_drone = tello.Tello()

import cv2,socket
import face_recognition

tello_ip='192.168.10.1'
tello_port = 8889
tello_adderss = (tello_ip, tello_port)
my_drone.send_command('streamon')
video_capture = cv2.VideoCapture('udp://'+tello_ip+':11111?overrun_nonfatal=1&fifo_size=50000000')
face_locations = []
my_drone.takeoff()

for i in range(4):
    my_drone.forward(100)
    my_drone.cw(90)


    


    # Grab a single frame of video
    ret, frame = video_capture.read()
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
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        my_drone.land()
my_drone.land()
video_capture.release()
