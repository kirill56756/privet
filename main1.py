import tkinter as tk
import pyautogui
import keyboard
import win32gui
import win32ui
import win32con
from time import sleep

def mywait():
    keyboard.read_key()


#гойда гойда гойда
def _get_windows_bytitle(title_text, exact=False):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, root in windows if title_text == root]
    else:
        return [hwnd for hwnd, root in windows if title_text in root]

#эээ ну тип скриншот тип лол
def screenshot(hwnd=None):
    if not hwnd:
        hwnd = win32gui.GetForegroundWindow()

    l, t, r, b = win32gui.GetWindowRect(hwnd)
    h = b - t
    w = r - l
    hDC = win32gui.GetWindowDC(hwnd)
    myDC = win32ui.CreateDCFromHandle(hDC)
    newDC = myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    myBitMap.CreateCompatibleBitmap(myDC, w, h)

    newDC.SelectObject(myBitMap)

    win32gui.SetForegroundWindow(hwnd)
    sleep(0.2)
    newDC.BitBlt((0, 0), (w, h), myDC, (0, 0), win32con.SRCCOPY)

    myBitMap.SaveBitmapFile(newDC, r'C:\Users\User\Pictures\screenshot.bmp')

    newDC.DeleteDC()
    myDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hDC)
    win32gui.DeleteObject(myBitMap.GetHandle())



keyboard.add_hotkey('\n', screenshot)

#рисовашки

line_id = None
line_points = []
line_options = {}

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



