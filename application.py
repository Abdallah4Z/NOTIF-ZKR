import customtkinter as ctk
from PIL import Image
import read_data
import pygame
import threading

def notification():
    pygame.mixer.init()
    pygame.mixer.music.load("audio/notification/notification_2.wav")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    pygame.mixer.quit()


minute_window = ctk.CTk()
minute_window.iconbitmap('logo.ico')

screen_width = minute_window.winfo_screenwidth()
screen_height = minute_window.winfo_screenheight()
x = screen_width - 100
y = 70
minute_window.geometry(f'{400}x{1400}+{x}+{y}')
minute_window.overrideredirect(True)

minute_window.attributes('-transparentcolor', minute_window.cget('bg'))
CourierB22 = ctk.CTkFont(family='Courier' , size=16, weight='bold')

def start_drag(event):
    minute_window.x = event.x
    minute_window.y = event.y

def drag_window(event):
    x = minute_window.winfo_pointerx() - minute_window.x
    y = minute_window.winfo_pointery() - minute_window.y
    minute_window.geometry(f'+{x}+{y}')

def show_window():
    threading.Thread(target=notification).start()
    minute_window.geometry(f'{400}x{1400}+{x}+{y}')
    minute_window.overrideredirect(True)
    text = read_data.get_data()
    label.configure(text=text)
    time_for_display = 55* len(text)

    minute_window.deiconify()  # Show the window
    minute_window.after(time_for_display, hide_window)  # Hide the window after 3 seconds

def hide_window(t = 600000):
    minute_window.withdraw()  # Hide the window
    minute_window.after(t, show_window)  # Show the window after 10 minutes

minute_window.bind('<Button-1>', start_drag)
minute_window.bind('<B1-Motion>', drag_window)

frame = ctk.CTkFrame(minute_window ,fg_color='#115184' ,corner_radius=12 , width =  300 , height =50 )
frame.pack()

label = ctk.CTkLabel(frame, text=read_data.get_data(), fg_color="transparent" ,justify='right' , font = CourierB22 , wraplength= 250)
label.grid(column = 1 , row =0 , padx = 10 , pady =15)

image = Image.open('logo.ico')
img = ctk.CTkImage(light_image=image , dark_image = image, size=(50 ,50))

img_label = ctk.CTkLabel(frame, text = '' , image= img , justify="center")
img_label.grid(column =0 , row = 0 ,padx =15 ,sticky="ns")

minute_window.attributes('-topmost', True)  # Make the window always appear on top
hide_window(100)  # Start the show/hide cycle

minute_window.mainloop()



