from tkinter import *
from tkinter import messagebox
import os
from PIL import ImageTk, Image
import time

# globals
off = True
los = False

# modifiable settings
print(os.getcwd())
emerg = False # emergency setting
minute_los = 0 # time for loss-of-signal countdown
seconds_los = 20
minute_aos = 0 # time for acquiring-of-signal countdown
seconds_aos = 30

# display
root = Tk()
root.title("Redesigned Mercury Comms Display")
canvas = Canvas(root, width = 764, height = 200)
canvas.pack()

# background
# background = Image.open("images/comms_display_blank.png")
background = Image.open("images/audio_off.png")
background = background.resize((900,500), Image.ANTIALIAS)
bckgd = ImageTk.PhotoImage(background)
canvas.create_image(0, 0, anchor=NW, image=bckgd)

# audio on/off
audio_on = Image.open("images/audio_on.png")
audio_on = audio_on.resize((50, 50), Image.ANTIALIAS)
on = ImageTk.PhotoImage(audio_on)

audio_off = Image.open("images/audio_off.png")
audio_off = audio_off.resize((50, 50), Image.ANTIALIAS)
of = ImageTk.PhotoImage(audio_off)


# audio indicator and status
canvas.create_oval(55, 85, 120, 150, outline="#000000", fill="#FFFF00") # yellow audio check
audio_status = canvas.create_text(190, 40, font=('Helvetica', 12, 'bold'), fill='yellow', text='INACTIVE')
bbox = canvas.bbox(audio_status)
rect_item = canvas.create_rectangle(bbox, outline="black", fill="gray")
canvas.tag_raise(audio_status,rect_item)

# telemetry indicator and status
canvas.create_oval(358, 110, 423, 175, outline = "#000000", fill="#00FF00")
telemetry_status = canvas.create_text(440, 40, font=('Helvetica', 12, 'bold'), fill="#00FF00", text='INACTIVE')
bbox_2 = canvas.bbox(telemetry_status)
canvas.itemconfig(telemetry_status, text='ACTIVE')
rect_item_2 = canvas.create_rectangle(bbox_2, outline="black", fill="gray")
canvas.tag_raise(telemetry_status,rect_item_2)

# subsystem status
off_nominal = canvas.create_text(390, 90, font=('Helvetica', 12, 'bold'), fill="#00FF00", text='COMMS')
bbox_3 = canvas.bbox(off_nominal)
rect_item_3 = canvas.create_rectangle(bbox_3, outline="black", fill="gray")
canvas.itemconfig(off_nominal, text='NONE')
canvas.tag_raise(off_nominal,rect_item_3)

# emergency shutdown
if emerg:
    canvas.create_oval(55, 85, 120, 150, outline="#000000", fill="#FF0000")
    canvas.itemconfig(audio_status, fill="#ff5c59", text='INACTIVE')
    canvas.create_oval(358, 110, 423, 175, outline = "#000000", fill="#FF0000")
    canvas.itemconfig(telemetry_status, fill="#ff5c59", text='INACTIVE')
    canvas.itemconfig(off_nominal, fill="#ff5c59", text='COMMS')


# audio switch function
def audio_turn():
    global off
    global los
    global emerg
    if off == True and los == False and emerg == False:
        audio_switch.config(image=on)
        canvas.create_oval(55, 85, 120, 150, outline = "#000000", fill="#00FF00")
        canvas.itemconfig(audio_status, fill="#00FF00", text='ACTIVE')
        off = not off
    elif off == False and los == False and emerg == False:
        audio_switch.config(image=of)
        canvas.create_oval(55, 85, 120, 150, outline="#000000", fill="#FFFF00")
        off = not off
        canvas.itemconfig(audio_status, fill="#FFFF00", text='INACTIVE')

# audio switch
label_on = canvas.create_text(178, 75, font=('Helvetica', 12, 'bold'), text = 'ON')
label_off = canvas.create_text(178, 160, font=('Helvetica', 12, 'bold'), text = 'OFF')
audio_switch = Button(image = of, command = audio_turn)
audio_switch.place(x=150, y=90)

# los config
zero1 = ''
zero2 = ''
if minute_los < 10:
    zero1 = '0'
if seconds_los < 10:
    zero2 = '0'
los_text = zero1 + str(minute_los) + ":" + zero2 + str(seconds_los)
los_countdown = canvas.create_text(650, 80, font=('Helvetica', 12, 'bold'), text=los_text)

# aos config
if minute_aos < 10:
    zero1 = '0'
if seconds_aos < 10:
    zero2 = '0'
aos_text = zero1 + str(minute_aos) + ":" + zero2 + str(seconds_aos)
aos_countdown = canvas.create_text(650, 120, font=('Helvetica', 12, 'bold'), fill = 'gray', text=aos_text)


# countdown function
def countdown():
    # set amount
    while True:
        # los countdown
        temp = int(minute_los)*60 + int(seconds_los)
        while temp >-1:

            mins,secs = divmod(temp,60)
            zero1 = ''
            zero2 = ''
            if mins < 10:
                zero1 = '0'
            if secs < 10:
                zero2 = '0'
            los_text = zero1 + str(mins) + ":" + zero2 + str(secs)
            canvas.itemconfig(los_countdown, fill = 'black', text=los_text)
            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            if temp != 0:
                time.sleep(1)

            # after every one sec the value of temp will be decremented
            # by one
            temp -= 1

        # update audio status for los
        canvas.create_oval(55, 85, 120, 150, outline="#000000", fill="#34ebe1")
        canvas.itemconfig(audio_status, fill="#34ebe1", text='INACTIVE')
        audio_switch.config(image=of)


        # update telemetry status for los
        canvas.create_oval(358, 110, 423, 175, outline = "#000000", fill="#34ebe1")
        canvas.itemconfig(telemetry_status, fill="#34ebe1", text='INACTIVE')
        canvas.itemconfig(off_nominal, fill="#34ebe1", text='N/A')

        global los
        los = True

        # reset los countdown
        mins = minute_los
        secs = seconds_los
        zero1 = ''
        zero2 = ''
        if mins < 10:
            zero1 = '0'
        if secs < 10:
            zero2 = '0'
        los_text = zero1 + str(mins) + ":" + zero2 + str(secs)
        canvas.itemconfig(los_countdown, fill = 'gray', text=los_text)

        # aos countdown
        temp2 = int(minute_aos)*60 + int(seconds_aos)
        while temp2 > -1:
            mins,secs = divmod(temp2,60)
            zero1 = ''
            zero2 = ''
            if mins < 10:
                zero1 = '0'
            if secs < 10:
                zero2 = '0'
            aos_text = zero1 + str(mins) + ":" + zero2 + str(secs)
            canvas.itemconfig(aos_countdown, fill = 'black', text=aos_text)
            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            if temp2 != 0:
                time.sleep(1)

            # after every one sec the value of temp will be decremented
            # by one
            temp2 -= 1

        # reset aos countdown
        mins = minute_aos
        secs = seconds_aos
        zero1 = ''
        zero2 = ''
        if mins < 10:
            zero1 = '0'
        if secs < 10:
            zero2 = '0'
        aos_text = zero1 + str(mins) + ":" + zero2 + str(secs)
        canvas.itemconfig(aos_countdown, fill = 'gray', text=aos_text)

        global off
        los = False

        # reset back to normal state
        canvas.create_oval(358, 110, 423, 175, outline = "#000000", fill="#00FF00")
        canvas.itemconfig(telemetry_status, fill="#00FF00", text='ACTIVE')
        canvas.itemconfig(off_nominal, fill="#00FF00", text='NONE')
        if off:
            canvas.create_oval(55, 85, 120, 150, outline="#000000", fill="#FFFF00")
            canvas.itemconfig(audio_status, fill="#FFFF00")
        else:
            canvas.create_oval(55, 85, 120, 150, outline = "#000000", fill="#00FF00")
            canvas.itemconfig(audio_status, fill = "#00FF00", text='ACTIVE')
            audio_switch.config(image=on)

if not emerg:
    countdown()
else:
    canvas.itemconfig(los_countdown, fill = 'gray', text=los_text)

root.mainloop()
