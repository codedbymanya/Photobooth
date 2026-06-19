import cv2
import time

i=1
camera = cv2.VideoCapture(0)

state = "idle"
countdown_start = 0
pause_start = 0

# def countdown(n):
#    for i in range(0,n):
#        print(n-i)
#        time.sleep(2)
#    print("Smile!")

while True: 
    success, frame = camera.read()

    if not success:
        break
    
    frame = cv2.flip(frame, 1)
    
    cv2.putText( frame, "Hello Manya", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    cv2.putText( frame, "Press Q: to quit", (300, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText( frame, "Press S: to save", (300, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Countdown logic
    if state == "countdown":
        elapsed = time.time()-countdown_start
        
        if elapsed < 1:
            number = "3"
        elif elapsed < 2:
            number = "2"
        elif elapsed <3:
            number = "1"
        elif elapsed <4:
            number = "Smile"
        else:
            # cv2.imwrite("photo"+str(i)+".jpg", frame)
            filename = "photo" + str(i) + ".jpg"
            cv2.imwrite(filename, frame)
            print(filename, "saved")

            i=i+1
            
            if i == 5:
                break

            state = "pause"
            pause_start = time.time()
            number = ""
            
        if state == "countdown":
            cv2.putText(frame, number, (270, 250), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 8)

    elif state == "pause":
        cv2.putText(frame, "Next Pose!", (180, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        elapsed = time.time()-pause_start
        if elapsed >= 2:
            state = "countdown"
            countdown_start = time.time()

    cv2.imshow("Photobooth",frame)            
    k = cv2.waitKey(1)

    if k == ord('s') and state == "idle":
        state = "countdown"
        # countdown = True
        countdown_start = time.time()

    # if k == ord('s'):

      #  countdown(3)
      #  cv2.imwrite("photo"+str(i)+".jpg", frame)
      #  i=i+1
        
    elif k == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
