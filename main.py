from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
import threading
from random import *
from playsound import playsound

window_w = 120
window_h = 100

root = Tk()
root.attributes("-topmost")
root.overrideredirect(1)
root.attributes("-alpha",0)

raw_img = Image.open("sourceengine/textures/grass.png")

def make_window():
    main = Toplevel(root)

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    main.geometry("%dx%d+%d+%d" % (window_w,window_h,randrange(0,ws),randrange(0,hs)))

    main.title("trolled")

    main.overrideredirect(1)

    main.minsize(width=window_w, height=window_h)

    main.attributes("-topmost")

    main.wm_attributes("-topmost", True)
    main.wm_attributes("-disabled", True)
    main.wm_attributes("-transparentcolor", "grey")

    resized_img = raw_img.resize((window_w,window_h))

    img = ImageTk.PhotoImage(resized_img)

    # text = Label(main,text="you've been trolled")
    imgLabel = Label(main,image=img,background="grey")
    imgLabel.image = img

    # text.pack()
    imgLabel.pack()

    main.lift()
    root.lift()

    def topmost_loop():
        while True:
            main.geometry("%dx%d+%d+%d" % (window_w,window_h,randrange(0,ws),randrange(0,hs)))
            time.sleep(0.2)
    topmost_loop_thread = threading.Thread(target=topmost_loop)
    topmost_loop_thread.start()

def play_sound():
    while True:
        playsound("sourceengine/sounds/title.mp3",block=True)

def whileloop():
    while True:
        window_thread = threading.Thread(target=make_window)
        window_thread.start()
        time.sleep(0.15)

loop_thread = threading.Thread(target=whileloop)

sound_thread = threading.Thread(target=play_sound)
sound_thread.daemon = True
sound_thread.start()
loop_thread.start()



root.mainloop()