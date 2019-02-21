"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zhen Yang.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
# import shared_gui

def main():
    private_gui()
    # shared_gui()

def private_gui():
    """
       This code, which must run on a LAPTOP:
         1. Constructs a GUI for my part of the Capstone Project.
         2. Communicates via MQTT with the code that runs on the EV3 robot.
       """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE120 Capstone")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    forward_button_1 = ttk.Button(frame, text="start maze cleaning")
    initial_label_1 = ttk.Label(frame, text="cw=0,ccw=whatever")
    rate_label_1 = ttk.Label(frame, text="speed")
    initial_speed_entry_1 = ttk.Entry(frame, width=8)
    initial_speed_entry_1.insert(0, "0")
    rate_entry_1 = ttk.Entry(frame, width=8)
    rate_entry_1.insert(0, "0")
    forward_button_1.grid(row=0, column=0)
    initial_label_1.grid(row=1, column=0)
    initial_speed_entry_1.grid(row=1, column=2)
    rate_entry_1.grid(row=2, column=2)
    rate_label_1.grid(row=2, column=0)
    forward_button_1["command"] = lambda: going_foward_1(mqtt_sender, initial_speed_entry_1, rate_entry_1)
    stop_button_1 = ttk.Button(frame, text='stop')
    stop_button_1.grid(row=0, column=1)
    stop_button_1['command'] = lambda: handle_stop_1(mqtt_sender)

    forward_button_2 = ttk.Button(frame, text="after_catch_stuff")
    initial_label_2 = ttk.Label(frame, text="cw=0,ccw=whatever")
    rate_label_2 = ttk.Label(frame, text="speed")
    initial_speed_entry_2 = ttk.Entry(frame, width=8)
    initial_speed_entry_2.insert(3, "0")
    rate_entry_2 = ttk.Entry(frame, width=8)
    rate_entry_2.insert(3, "0")
    forward_button_2.grid(row=3, column=0)
    initial_label_2.grid(row=4, column=0)
    initial_speed_entry_2.grid(row=4, column=2)
    rate_entry_2.grid(row=5, column=2)
    rate_label_2.grid(row=5, column=0)
    forward_button_2["command"] = lambda: going_foward_2(mqtt_sender, initial_speed_entry_2, rate_entry_2)
    stop_button_2 = ttk.Button(frame, text='stop')
    stop_button_2.grid(row=3, column=1)
    stop_button_2['command'] = lambda: handle_stop_2(mqtt_sender)

    forward_button_3 = ttk.Button(frame, text="go_chase_target")
    initial_label_3 = ttk.Label(frame, text="cw=0,ccw=whatever")
    rate_label_3 = ttk.Label(frame, text="speed")
    initial_speed_entry_3 = ttk.Entry(frame, width=8)
    initial_speed_entry_3.insert(6, "0")
    rate_entry_3 = ttk.Entry(frame, width=8)
    rate_entry_3.insert(6, "0")
    forward_button_3.grid(row=6, column=0)
    initial_label_3.grid(row=7, column=0)
    initial_speed_entry_3.grid(row=7, column=2)
    rate_entry_3.grid(row=8, column=2)
    rate_label_3.grid(row=8, column=0)
    forward_button_3["command"] = lambda: going_foward_3(mqtt_sender, initial_speed_entry_3, rate_entry_3)
    stop_button_3 = ttk.Button(frame, text='stop')
    stop_button_3.grid(row=6, column=1)
    stop_button_3['command'] = lambda: handle_stop_3(mqtt_sender)

    # camera_clock_label = ttk.Label(frame, text="cw=0, ccw=1")
    # camera_clock_label.grid(row=3, column=1)
    # camera_clock_entry = ttk.Entry(frame, width=8)
    # camera_clock_entry.grid(row=4, column=1)
    # camera_speed_label = ttk.Label(frame, text="speed")
    # camera_speed_label.grid(row=3, column=2)
    # camera_speed_entry = ttk.Entry(frame, width=8)
    # camera_speed_entry.grid(row=4, column=2)
    # camera_button = ttk.Button(frame, text='robot dog chasing')
    # camera_button.grid(row=4, column=0)
    # camera_button['command'] = lambda: mqtt_sender.send_message("start_to_catch", [
    #     int(camera_speed_entry.get()),int(camera_clock_entry.get())])



    root.mainloop()

def going_foward_1(mqtt_sender, initial_speed_entry, rate_entry):
    print("going forward_1 for start to catch")
    speed = initial_speed_entry.get()
    rate_entry = rate_entry.get()
    mqtt_sender.send_message('start_to_catch', [int(rate_entry),int(speed)])

def going_foward_2(mqtt_sender, initial_speed_entry, rate_entry):
    print("going forward 2 for after catch stuff")
    speed = initial_speed_entry.get()
    rate_entry = rate_entry.get()
    mqtt_sender.send_message('after_catch_stuff', [int(rate_entry),int(speed)])

def going_foward_3(mqtt_sender, initial_speed_entry, rate_entry):
    print("going forward 3 for go chase target")
    speed = initial_speed_entry.get()
    rate_entry = rate_entry.get()
    mqtt_sender.send_message('go_chase_target', [int(rate_entry),int(speed)])
# def main():
#     """
#     This code, which must run on a LAPTOP:
#       1. Constructs a GUI for my part of the Capstone Project.
#       2. Communicates via MQTT with the code that runs on the EV3 robot.
#     """
#     # -------------------------------------------------------------------------
#     # Construct and connect the MQTT Client:
#     # -------------------------------------------------------------------------
#     mqtt_sender=com.MqttClient()
#     mqtt_sender.connect_to_ev3()
#
#     # -------------------------------------------------------------------------
#     # The root TK object for the GUI:
#     # -------------------------------------------------------------------------
#     root=tkinter.Tk()
#     root.title("CSSE120 Capstone")
#
#     # -------------------------------------------------------------------------
#     # The main frame, upon which the other frames are placed.
#     # -------------------------------------------------------------------------
#     main_frame=ttk.Frame(root,padding=10,borderwidth=5,relief='groove')
#     main_frame.grid()
#
#     # -------------------------------------------------------------------------
#     # Sub-frames for the shared GUI that the team developed:
#     # -------------------------------------------------------------------------
#     teleop_frame,arm_frame,control_frame,sound_frame,go_and_beep_frame=get_shared_frames(main_frame,mqtt_sender)
#
#
#     # -------------------------------------------------------------------------
#     # Frames that are particular to my individual contributions to the project.
#     # -------------------------------------------------------------------------
#     # Done: Implement and call get_my_frames(...)
#
#     # -------------------------------------------------------------------------
#     # Grid the frames.
#     # -------------------------------------------------------------------------
#     grid_frames(teleop_frame,arm_frame,control_frame,sound_frame,go_and_beep_frame)
#
#     # -------------------------------------------------------------------------
#     # The event loop:
#     # -------------------------------------------------------------------------
#     root.mainloop()
#
#
# def get_shared_frames(main_frame, mqtt_sender):
#     teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
#     arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
#     control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
#     sound_frame=shared_gui.get_sound_system(main_frame,mqtt_sender)
#     go_and_beep_frame = shared_gui.go_and_beep_frame(main_frame,mqtt_sender)
#     return teleop_frame,arm_frame,control_frame,sound_frame,go_and_beep_frame
#
#
# def grid_frames(teleop_frame, arm_frame, control_frame,sound_frame,go_and_beep_frame):
#     teleop_frame.grid(row=0,column=0)
#     arm_frame.grid(row=1,column=0)
#     control_frame.grid(row=2, column=0)
#     sound_frame.grid(row=3,column=0)
#     go_and_beep_frame.grid(row = 3, column = 1)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def handle_stop_1(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message('stop',[] )

def handle_stop_2(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message('stop',[] )

def handle_stop_3(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message('stop',[] )
main()