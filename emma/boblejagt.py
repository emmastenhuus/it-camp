from tkinter import *

# grafiske brugerflade
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title("Boblejagt")
l = Canvas(window, width = WIDTH, height = HEIGHT, bg = "darkblue")
l.pack()

# grafik af ubåd
ubaad_id = l.create_polygon(5, 5, 5, 25, 30, 15, fill = "red")
ubaad_id2 = l.create_oval(0, 0, 30, 30, outline = "red")
UBAAD_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
l.move(ubaad_id, MID_X, MID_Y)
l.move(ubaad_id2, MID_X, MID_Y)
