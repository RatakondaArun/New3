# import cv2
# import threading
# from deepface import DeepFace

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# counter = 0
# face_match = False
# reference_img = cv2.imread("Nani1.jpg")

# if reference_img is None:
#     print("Error: Reference image not loaded. Check the path.")
#     exit()

# def check_face(frame):
#     global face_match
#     try:
#         print("Checking face...")
#         result = DeepFace.verify(frame, reference_img.copy())
#         print("DeepFace result:", result)
#         if result['verified']:
#             face_match = True
#         else:
#             face_match = False
#     except Exception as e:
#         print("Error in face verification:", e)
#         face_match = False

# while True:
#     ret, frame = cap.read()

#     if ret:
#         if counter % 30 == 0:
#             try:
#                 check_face(frame.copy())
#             except Exception as e:
#                 print("Error starting thread:", e)
#         counter += 1

#         if face_match:
#             print("match")
#             cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
#         else:
#             print("no match")
#             cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

#         cv2.imshow("video", frame)

#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import os
from deepface import DeepFace


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
counter = 0
face_match = False 

reference_img = cv2.imread ("Nani3.jpg")


directory = "matchpic1s"


if not os.path.exists(directory):
    os.makedirs(directory)

def check_face(frame):
    global face_match
    try:
        print("Checking face...")
       
        result = DeepFace.verify(frame,reference_img.copy())
        print("DeepFace result:", result)
        if result['verified']:
            face_match = True
        else:
            face_match = False
    except Exception as e:
        print("Error in face verification:", e)
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                check_face(frame.copy())
            except Exception as e:
                print("Error starting thread:", e)
        counter += 1

        if face_match:
            print("match")
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            print("no match")
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("video", frame)

       
        img_filename = os.path.join(directory, f"frame_{counter}.jpg")
        cv2.imwrite(img_filename, frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()