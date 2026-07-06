import customtkinter as ctk
import camera_test

# ---------- FUNCTIONS ----------

def choose_photobooth():
    app.withdraw()          # Hide the GUI window
    print("Photobooth selected")
    camera_test.start_photobooth()
    app.deiconify()         # Show it again afterwards

def choose_polaroid():
    print("Polaroid selected")

app = ctk.CTk()
app.title("Manya Photobooth")
app.geometry("1100x1000")

# Light mode
ctk.set_appearance_mode("light")

# Pastel theme
app.configure(fg_color="#FFF8F0")

title = ctk.CTkLabel( 
    app, 
    text ="Manya Photobooth", 
    font =("Arial", 36, "bold"), 
    text_color="#5B4B49")
title.pack(pady = (50, 10))

subtitle = ctk.CTkLabel( 
    app, 
    text="Capture memories, one pose at a time 💕", 
    font=("Arial", 18), 
    text_color="#7A6F6D" )

photobooth_button = ctk.CTkButton( 
    app, 
    text = "Photobooth Mode", 
    command=choose_photobooth,
    width=300,
    height=60,
    fg_color="#F8C8DC",
    hover_color="#F4B6CF",
    text_color="#4A3F35",
    font=("Arial", 18, "bold"),
    corner_radius=20)

photobooth_button.pack(pady = 15)

polaroid_button = ctk.CTkButton( 
    app, 
    text = "Polaroid Mode",
    command=choose_polaroid,
    width=300,
    height=60,
    fg_color="#DCCEF9",
    hover_color="#CDBCF5",
    text_color="#4A3F35",
    font=("Arial", 18, "bold"),
    corner_radius=20)
polaroid_button.pack(pady = 10)

app.mainloop()