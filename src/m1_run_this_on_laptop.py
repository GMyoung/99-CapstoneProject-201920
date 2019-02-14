"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Yicheng Yang.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui

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
    forward_button = ttk.Button(frame, text="chase object")
    initial_label = ttk.Label(frame, text="initial speed(0 to 10)")
    rate_label = ttk.Label(frame, text="beep rate(0 to 10)")
    initial_speed_entry = ttk.Entry(frame, width=8)
    initial_speed_entry.insert(0, "0")
    rate_entry = ttk.Entry(frame, width=8)
    rate_entry.insert(0, "0")
    forward_button.grid(row=0, column=1)
    initial_label.grid(row=1, column=0)
    initial_speed_entry.grid(row=1, column=2)
    rate_entry.grid(row=2, column=2)
    rate_label.grid(row=2, column=0)
    forward_button["command"] = lambda: going_foward(mqtt_sender, initial_speed_entry, rate_entry)
    stop_button = ttk.Button(frame, text='stop')
    stop_button.grid(row=0, column=1)
    stop_button['command'] = lambda: handle_stop(mqtt_sender)

    camera_clock_label = ttk.Label(frame, text="cw=0, ccw=1")
    camera_clock_label.grid(row=3, column=1)
    camera_clock_entry = ttk.Entry(frame, width=8)
    camera_clock_entry.grid(row=4, column=1)
    camera_speed_label = ttk.Label(frame, text="speed")
    camera_speed_label.grid(row=3, column=2)
    camera_speed_entry = ttk.Entry(frame, width=8)
    camera_speed_entry.grid(row=4, column=2)
    camera_button = ttk.Button(frame, text='camera')
    camera_button.grid(row=4, column=0)
    camera_button['command'] = lambda: mqtt_sender.send_message("go_and_pick", [int(camera_clock_entry.get()),
                                                                                int(camera_speed_entry.get())])

    proximity_go_inch_label = ttk.Label(frame, text='inch')
    proximity_go_inch_label.grid(row=5, column=0)
    proximity_go_inch_entry = ttk.Entry(frame, width=8)
    proximity_go_inch_entry.grid(row=6, column=0)
    proximity_go_speed_label = ttk.Label(frame, text='speed')
    proximity_go_speed_label.grid(row=5, column=1)
    proximity_go_speed_entry = ttk.Entry(frame, width=8)
    proximity_go_speed_entry.grid(row=6, column=1)
    proximity_go_delta_label = ttk.Label(frame, text='delta')
    proximity_go_delta_label.grid(row=5, column=2)
    proximity_go_delta_entry = ttk.Entry(frame, width=8)
    proximity_go_delta_entry.grid(row=6, column=2)
    proximity_go_less = ttk.Button(frame, text='go until less')
    proximity_go_less.grid(row=7, column=0)
    proximity_go_less['command'] = lambda: mqtt_sender.send_message("go_less", [int(proximity_go_inch_entry.get()),
                                                                                int(proximity_go_speed_entry.get())])
    proximity_go_great = ttk.Button(frame, text='go until greater')
    proximity_go_great.grid(row=7, column=1)
    proximity_go_great['command'] = lambda: mqtt_sender.send_message("go_greater", [int(proximity_go_inch_entry.get()),
                                                                                    int(
                                                                                        proximity_go_speed_entry.get())])
    proximity_go_within = ttk.Button(frame, text='go until within')
    proximity_go_within.grid(row=7, column=2)
    proximity_go_within['command'] = lambda: mqtt_sender.send_message("go_within", [int(proximity_go_delta_entry.get()),
                                                                                    int(proximity_go_inch_entry.get()),
                                                                                    int(
                                                                                        proximity_go_speed_entry.get())])

    proximity_speed_label = ttk.Label(frame, text="speed")
    proximity_speed_label.grid(row=1, column=1)



    root.mainloop()

def going_foward(mqtt_sender, initial_speed_entry, rate_entry):
    print("go_foward_until")
    speed = initial_speed_entry.get()
    rate_entry = rate_entry.get()
    mqtt_sender.send_message('go_foward_until', [speed, rate_entry])
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
def handle_stop(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message('quit',[] )
main()