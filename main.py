import numpy as np
from tkinter import *
master = Tk()

g_amplitude = 1
g_period = 2*np.pi
g_phase_shift = 0
g_midline = 0

canvas_width = 320
canvas_height = 180
scale = 2
origin = [canvas_width/2, canvas_height/2]

canvas = Canvas(master, width=canvas_width*scale, height=canvas_height*scale)
canvas.grid(row=0, column=2)

def Sine(canvas_width, canvas_height, amplitude=1, period=2*np.pi, phase_shift=0, midline=0, XFLIP=FALSE, YFLIP=TRUE, zoom = 16):
    return [(amplitude*np.sin(((x-origin[0])/zoom*(1-2*int(XFLIP))-phase_shift)*(2*np.pi/period))+midline)*(1-2*int(YFLIP))*zoom + origin[1] for x in range(canvas_width+1)]

def Cosine(canvas_width, canvas_height, amplitude=1, period=2*np.pi, phase_shift=0, midline=0, XFLIP=FALSE, YFLIP=TRUE, zoom = 16):
    return [(amplitude*np.cos(((x-origin[0])/zoom*(1-2*int(XFLIP))-phase_shift)*(2*np.pi/period))+midline)*(1-2*int(YFLIP))*zoom + origin[1] for x in range(canvas_width+1)]

def fxCurve(canvas_width, canvas_height, amplitude=1, period=2*np.pi, phase_shift=0, midline=0):
    values = Cosine(canvas_width, canvas_height, amplitude=amplitude, period=period, phase_shift=phase_shift, midline=midline)
    for i in range(len(values)-1):
        canvas.create_line(i*scale, int(values[i]*scale), (i+1)*scale, int(values[i+1]*scale), fill="blue", width=2)
    
    values = Sine(canvas_width, canvas_height, amplitude=amplitude, period=period, phase_shift=phase_shift, midline=midline)
    for i in range(len(values)-1):
        canvas.create_line(i*scale, int(values[i]*scale), (i+1)*scale, int(values[i+1]*scale), fill="red", width=2)

def updateCanvas(event):
    global origin, g_amplitude, g_period, g_phase_shift, g_midline
    origin[0] = sl_ox.get()
    origin[1] = canvas_height - sl_oy.get()
    g_amplitude = sl_a.get()
    g_period = sl_pd.get()
    g_phase_shift = sl_ps.get()
    g_midline = sl_m.get()
    canvas.create_rectangle(0, 0, canvas_width*scale, canvas_height*scale+2, fill="white")
    canvas.create_line(origin[0]*scale, 0, origin[0]*scale, canvas_height*scale, fill="black")
    canvas.create_line(0, origin[1]*scale, canvas_width*scale, origin[1]*scale, fill="black")
    fxCurve(canvas_width, canvas_height, g_amplitude, g_period, g_phase_shift, g_midline)

w = Label(master, text="Origin x:", relief=SUNKEN, width=20, height=2).grid(row=1, column=0)
sl_ox = Scale(master, from_=0, to=canvas_width, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_ox.set(origin[0])
sl_ox.grid(row=1, column=1)

w = Label(master, text="Origin y:", relief=SUNKEN, width=20, height=2).grid(row=2, column=0)
sl_oy = Scale(master, from_=0, to=canvas_height, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_oy.set(origin[1])
sl_oy.grid(row=2, column=1)

w = Label(master, text="Amplitude:", relief=SUNKEN, width=20, height=2).grid(row=3, column=0)
sl_a = Scale(master, from_=-10, to=10, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_a.set(1)
sl_a.grid(row=3, column=1)

w = Label(master, text="Period:", relief=SUNKEN, width=20, height=2).grid(row=4, column=0)
sl_pd = Scale(master, from_=1, to=30, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_pd.set(2*np.pi)
sl_pd.grid(row=4, column=1)

w = Label(master, text="Phase Shift:", relief=SUNKEN, width=20, height=2).grid(row=5, column=0)
sl_ps = Scale(master, from_=-20, to=20, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_ps.set(0)
sl_ps.grid(row=5, column=1)

w = Label(master, text="Midline:", relief=SUNKEN, width=20, height=2).grid(row=6, column=0)
sl_m = Scale(master, from_=-10, to=10, orient=HORIZONTAL, relief=SUNKEN, length=300, resolution=-1, command=updateCanvas)
sl_m.set(0)
sl_m.grid(row=6, column=1)

w = Text(master, width=40, padx=10, pady=10, wrap=WORD)
w.grid(row=0, column=1)
text= '''
SINE/COSINE GRAPHER
Marten project by Daniel Li
10/27/2023

   This project makes use of python's tkinter package to create an interactive GUI, where one can change the parameters for a sine and cosine graph.
   The sine graph is drawn in red, while the cosine graph is drawn in blue.

Source:
    https://github.com/FallingSky65/Marten-Project-2023
'''
w.insert(END, text)

mainloop()
