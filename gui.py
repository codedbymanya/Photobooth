import customtkinter as ctk    
import cv2  
from PIL import Image, ImageTk 
import camera_test
import time 
import countdown as countdown_module
#import filters
#import sessions

# ---------- Global variables ----------
PHOTOS_PER_SESSION = 4
PAUSE_SECONDS = 2

class PhotoboothApp:
    def __init__(self):
        self.app = ctk.CTk() 
        self.app.title("Manya Photobooth")   
        self.app.geometry("1100x1000")   
        
        ctk.set_appearance_mode("light")     # Light mode
        self.app.configure(fg_color="#FFF8F0")  # Pastel theme
        self.camera = cv2.VideoCapture(0)   
    #self.cap = cv2.VideoCapture(0)

        self.current_frame = None
        self.countdown_active = False
        self.countdown_start = 0
        self.pause_active = False
        self.pause_start = 0
        self.photo_number = 1
        self.session_path = None
        self.filter_mode = "normal"

        self._build_home_frame()
        self._build_camera_frame()

        self.home_frame.pack(fill="both", expand=True)

# ---------- UI BUILDERS ----------
    def _build_home_frame(self):
        self.home_frame = ctk.CTkFrame(self.app, fg_color="transparent")

        title = ctk.CTkLabel( self.home_frame, 
                             text ="Manya Photobooth", 
                             font =("Arial", 36, "bold"), 
                             text_color="#5B4B49")
        title.pack(pady = (50, 10))

        subtitle = ctk.CTkLabel( self.home_frame, 
                                text="Capture memories, one pose at a time 💕", 
                                font=("Arial", 18), 
                                text_color="#7A6F6D" )
        subtitle.pack(pady=(0, 30))

        photobooth_button = ctk.CTkButton( self.home_frame,
                                          text="Photobooth Mode",
                                          command=self.open_photobooth,
                                          width=300, height=60,
                                          fg_color="#F8C8DC", 
                                          hover_color="#F4B6CF",
                                          text_color="#4A3F35", 
                                          font=("Arial", 18, "bold"),
                                          corner_radius=20)
        photobooth_button.pack(pady = 15)

        polaroid_button = ctk.CTkButton( self.home_frame, 
                                        text = "Polaroid Mode",
                                        command=self.choose_polaroid,
                                        width=300, height=60,
                                        fg_color="#DCCEF9",
                                        hover_color="#CDBCF5",
                                        text_color="#4A3F35",
                                        font=("Arial", 18, "bold"),
                                        corner_radius=20)
        polaroid_button.pack(pady = 10)

    def _build_camera_frame(self):
        self.camera_frame = ctk.CTkFrame(
            self.app, 
            fg_color="transparent")
        
        self.camera_label = ctk.CTkLabel(
            self.camera_frame,
            text="")
        self.camera_label.pack(pady=20)

        button_frame = ctk.CTkFrame(self.camera_frame, 
                                    fg_color="transparent")
        button_frame.pack(pady=15)

        self.capture_button = ctk.CTkButton(
            button_frame, text="Capture",
            command=self.start_countdown,
            width=200, height=60,
            fg_color="#F8C8DC", hover_color="#F4B6CF",
            text_color="#4A3F35", 
            font=("Arial", 18, "bold"),
            corner_radius=20)
        self.capture_button.pack(side="left", padx=10)
        
        self.filter_button = ctk.CTkButton( 
            button_frame,                            
            text = "Filter",
            command=self.cycle_filter,
            width=200,
            height=60, 
            fg_color="#F8C8DC", 
            hover_color="#F4B6CF",
            text_color="#4A3F35",
            font=("Arial", 18, "bold"),
            corner_radius=20)
        self.filter_button.pack(side="left", padx=10)
        
        self.retake_button = ctk.CTkButton( 
            button_frame, 
            text = "Retake", 
            command=self.retake_session,
            width=200,
            height=60,
            fg_color="#F8C8DC",
            hover_color="#F4B6CF",
            text_color="#4A3F35",
            font=("Arial", 18, "bold"),
            corner_radius=20)
        self.retake_button.pack(side="left", padx=10)

# ---------- NAVIGATION ----------
    def open_photobooth():
        self.home_frame.pack_forget()
        self.camera_frame.pack(fill="both", expand=True)
        self.update_camera_preview()

    # app.withdraw()          # Hide the GUI window
    #print("Photobooth selected")
    # camera_test.start_photobooth()
    # app.deiconify()         # Show it again afterwards
             
    def choose_polaroid(self):
            print("Polaroid selected")

# ---------- CAMERA LOOP ----------
    def update_camera_preview():
        success, frame = self.camera.read()

        if success:
            frame = cv2.flip(frame, 1)
            self.current_frame = frame.copy()
            frame = filters.apply_filter(frame, self.filter_mode)
            
            if self.countdown_active:
                elapsed = time.time() - self.countdown_start
                text = countdown_module.get_countdown_text(elapsed)

            if text is None:
                 self._capture_photo()
            else:
                cv2.putText(frame, text, (270, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 8)
            
            if self.pause_active:
                cv2.putText(frame, "Next Pose!", (150, 250),
                            cv2.FONT_HERSHEY_SIMPLEX, 2,
                            (0, 255, 0), 4)
                if time.time() - self.pause_start >= PAUSE_SECONDS:
                    self.pause_active = False

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(img)
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo
    
        self.app.after(10, self.update_camera_preview)
    
    def _capture_photo(self):
        filename = camera_test.save_photo(self.current_frame, 
                                     self.session_path, 
                                     self.photo_number)
        print(filename, "saved")
        
        self.photo_number += 1
        self.countdown_active = False
        
        if self.photo_number > PHOTOS_PER_SESSION:
            camera_test.build_photostrip(self.session_path, PHOTOS_PER_SESSION)
            print("Photostrip built for", self.session_path)
        else:
            self.pause_active = True
            self.pause_start = time.time()

# ---------- BUTTON ACTIONS ----------
    def start_countdown(self):   
        if self.countdown_active:
            return
        if self.session_path is None:
            self.session_path = camera_test.create_session()
        self.countdown_active = True
        self.countdown_start = time.time()

    def cycle_filter(self):
        options = ["normal", "gray"]    #add sepia later
        current_index = options.index(self.filter_mode)
        self.filter_mode = options[(current_index + 1) % len(options)]
        print("Filter set to", self.filter_mode)
 
    def retake_session(self):
        if self.session_path:
            sessions.delete_session(self.session_path)
        self.session_path = None
        self.photo_number = 1
        self.countdown_active = False
        self.pause_active = False
    
    def run(self):
        self.app.mainloop()
        self.cap.release()

def run_app():
    booth = PhotoboothApp()
    booth.run()
