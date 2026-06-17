import cv2
import time

i=1
camera = cv2.VideoCapture(0)

countdown = False
countdown_start = 0

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
    if countdown:
        elapsed = time.time()-countdown_start
        
        if elapsed < 1:
            number = "3"
        elif elapsed < 2:
            number = "2"
        elif elapsed <3:
            number = "1"
        else:
            cv2.imwrite("photo"+str(i)+".jpg", frame)
            i=i+1
            countdown = False
            number = ""
        
        if countdown:
            cv2.putText(frame, number, (300, 250),
                        cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 8)
            
    cv2.imshow("Photobooth",frame)
    
    k = cv2.waitKey(1)
    
    if k == ord('s') and not countdown:
        countdown = True
        countdown_start = time.time()

    # if k == ord('s'):

      #  countdown(3)
      #  cv2.imwrite("photo"+str(i)+".jpg", frame)
      #  i=i+1
        
    elif k == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
