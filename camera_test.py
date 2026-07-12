import cv2  
import os
import photostrip

from datetime import datetime

def create_session():   
    if not os.path.exists("Sessions"):
        os.mkdir("Sessions") 
    session_name = datetime.now().strftime("Session_%Y_%m_%d_%H_%M_%S")
    session_path = os.path.join( "Sessions", session_name )
    os.makedirs(session_path, exist_ok=True) 
    return session_path

def save_photo(frame, session_path, photo_number):
    #Save frame as photo{photo_number}.jpg inside session_path.
    filename = os.path.join(session_path, f"photo{photo_number}.jpg")
    cv2.imwrite(filename, frame)
    return filename

def build_photostrip(session_path, photo_count=4):
    #Combine the session's photos into a single photostrip.jpg."""
    image_paths = [
        os.path.join(session_path, f"photo{i}.jpg")
        for i in range(1, photo_count + 1)
    ]
    output_path = os.path.join(session_path, "photostrip.jpg")
    return photostrip.combine_images(image_paths, output_path)
