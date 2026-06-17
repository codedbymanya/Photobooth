import time

def greet():
    print("Hello!")
    print("Welcome to photobooth")

def countdown(n):
    for i in range(0,n):
        print(n-i)
        time.sleep(2)
    print("Smile!")

def take_photos(count):
    photos = []
    for i in range(1,count+1):
        photos.append("photo"+str(i)+".jpg")
    return photos


greet()

n = input("TIMER (seconds): ")
if int(n)<=0:
    print("Invalid timer")
else:
    countdown(int(n))

print(take_photos(4))