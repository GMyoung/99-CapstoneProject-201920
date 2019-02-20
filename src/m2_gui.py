import tkinter
from tkinter import ttk
import numpy as np
import random

def control_panel(window, mqtt_sender):
    """"
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    title_label=ttk.Label(frame,text='Boba Fett')
    title_label.grid(row=0,column=1)

    forward_button=ttk.Button(frame,text='charge on️')
    forward_button.grid(row=1,column=1)
    forward_button["command"]=lambda :mqtt_sender.send_message('go_less',[7,100])
    backward_button=ttk.Button(frame,text='retreat')
    backward_button.grid(row=3, column=1)
    backward_button["command"]=lambda :mqtt_sender.send_message('go_greater',[10,100])
    left_button = ttk.Button(frame, text='show off')
    left_button.grid(row=2, column=0)
    left_button["command"] = lambda: mqtt_sender.send_message('calibrate_arm', [])
    right_button = ttk.Button(frame, text='show off')
    right_button.grid(row=2, column=2)
    right_button["command"] = lambda: mqtt_sender.send_message('calibrate_arm', [])
    stop_button = ttk.Button(frame, text='stop')
    stop_button.grid(row=2, column=1)
    stop_button["command"] = lambda: mqtt_sender.send_message('stop', [])
    pick_up_button=ttk.Button(frame,text='BLAST HIM!')
    pick_up_button.grid(row=4,column=0)
    pick_up_button["command"]=lambda :mqtt_sender.send_message('pick_up',[])
    pick_up_button = ttk.Button(frame, text='get your medal')
    pick_up_button.grid(row=4, column=1)
    pick_up_button["command"] = lambda: mqtt_sender.send_message('raise_arm', [])
    exit_button = ttk.Button(frame, text='exit')
    exit_button.grid(row=4, column=2)
    exit_button["command"] = lambda: exit()

    blank=ttk.Label(frame,text='')
    blank.grid(row=3,column=1)

    window.bind_all('<Key-l>',lambda event:mqtt_sender.send_message('stop', []))
    window.bind_all('<Key-w>',lambda event:mqtt_sender.send_message('forward',[]))
    window.bind_all('<Key-s>', lambda event: mqtt_sender.send_message('backward', []))
    window.bind_all('<Key-a>', lambda event: mqtt_sender.send_message('left', []))
    window.bind_all('<Key-d>', lambda event: mqtt_sender.send_message('right', []))

    return frame

def canvas(window):
    ori_list=['Red','Blue','Black','Yellow','White','Brown','Green']
    list=random.shuffle(ori_list)
    out_list = []
    for k in range (3):
        out_list.append(ori_list[k])

    out_list = ', '.join(out_list)

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    # root = tkinter.Tk()

    cv = tkinter.Canvas(frame, bg='white', width=1000, height=500)
    cv.grid(row=1,column=0)

    cv.create_text(500,30,text='Jedi with these colors of light saber occur!',fill='black')
    cv.create_text(500,50,text="They are: " +out_list+". BLAST THEM! and get their light sabers!',")
    cv.create_text(500, 80, text="This is your light saber collection: ")
    return frame,cv

# def count_blast():
#     click+=1


    # root=
    # cv=tkinter.Canvas