import tkinter as tk
import pyautogui
import keyboard
import win32gui

def mywait():
    keyboard.read_key()


line_id = None
line_points = []
line_options = {}



def screenshot():
            window_title = pyautogui.getActiveWindowTitle()
            im = pyautogui.screenshot(window_title)
            im.save(r"c:\desktop\screenshot.png")

keyboard.add_hotkey('\n', screenshot)

def draw_line(event):
    global line_id
    line_points.extend((event.x, event.y))
    if line_id is not None:
        canvas.delete(line_id)
    line_id = canvas.create_line(line_points, **line_options)


def set_start(event):
    line_points.extend((event.x, event.y))


def end_line(event=None):
    global line_id
    line_points.clear()
    line_id = None

root = tk.Tk()
canvas_width= 9999999
canvas_height = 9999999
canvas = tk.Canvas(
           width=canvas_width,
           height=canvas_height)
canvas.pack()

canvas.bind('<Button-1>', set_start)
canvas.bind('<B1-Motion>', draw_line)
canvas.bind('<ButtonRelease-1>', end_line)
root.mainloop()

while True:
    mywait()



