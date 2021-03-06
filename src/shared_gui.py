"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Yicheng Yang, Shixin Wu, Zhen Yang.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):


    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")
    go_for_seconds_time_label=ttk.Label(frame,text='time')
    go_for_seconds_speed_label = ttk.Label(frame, text='speed(0-100)')
    go_for_distance_inch_label=ttk.Label(frame,text='inch')
    go_for_distance_speed_label=ttk.Label(frame,text='speed(0-100)')
    go_for_degree_inch_label = ttk.Label(frame, text='degrees')
    go_for_degree_speed_label = ttk.Label(frame, text='speed(0-100)')

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")
    go_for_seconds_time_entry=ttk.Entry(frame,width=8)
    go_for_seconds_time_entry.insert(0,'0')
    go_for_seconds_speed_entry = ttk.Entry(frame, width=8)
    go_for_seconds_speed_entry.insert(0, '0')
    go_for_distance_inch_entry=ttk.Entry(frame,width=8)
    go_for_distance_inch_entry.insert(0,'0')
    go_for_distance_speed_entry = ttk.Entry(frame, width=8)
    go_for_distance_speed_entry.insert(0, '0')
    go_for_degree_inch_entry = ttk.Entry(frame, width=8)
    go_for_degree_inch_entry.insert(0, '0')
    go_for_degree_speed_entry = ttk.Entry(frame, width=8)
    go_for_degree_speed_entry.insert(0, '0')


    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")
    go_for_seconds_button=ttk.Button(frame,text='go for seconds')
    go_for_distance_button=ttk.Button(frame,text='go for distance using inches')
    go_for_degree_button=ttk.Button(frame,text='go for distance using encoder')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    go_for_seconds_time_label.grid(row=6,column=1)
    go_for_seconds_speed_label.grid(row=6, column=2)
    go_for_distance_inch_label.grid(row=8,column=1)
    go_for_distance_speed_label.grid(row=8,column=2)
    go_for_seconds_time_entry.grid(row=7, column=1)
    go_for_seconds_speed_entry.grid(row=7,column=2)
    go_for_distance_inch_entry.grid(row=9,column=1)
    go_for_distance_speed_entry.grid(row=9, column=2)
    go_for_degree_inch_label.grid(row=10, column=1)
    go_for_degree_speed_label.grid(row=10, column=2)
    go_for_degree_inch_entry.grid(row=11,column=1)
    go_for_degree_speed_entry.grid(row=11, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)
    go_for_seconds_button.grid(row=7,column=0)
    go_for_distance_button.grid(row=9,column=0)
    go_for_degree_button.grid(row=11,column=0)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    go_for_seconds_button["command"]=lambda :handle_go_straight_for_seconds(
        go_for_seconds_time_entry,go_for_seconds_speed_entry,mqtt_sender)
    go_for_distance_button['command']=lambda :handle_go_straight_for_distance(
        go_for_distance_inch_entry,go_for_distance_speed_entry,mqtt_sender)
    go_for_degree_button['command']=lambda :handle_go_straight_for_degrees(
        go_for_degree_inch_entry,go_for_degree_speed_entry,mqtt_sender)


    return frame


def get_arm_frame(window, mqtt_sender):
    """
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
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################
def get_sound_system(window,mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Sound System")
    beeper_label=ttk.Label(frame,text='time')
    tone_maker_frequency_label=ttk.Label(frame,text='frequency')
    tone_maker_duration_label=ttk.Label(frame,text='duration')
    speech_label=ttk.Label(frame,text='enter your phrase')

    beeper_entry = ttk.Entry(frame, width=8)
    tone_maker_frequency_entry=ttk.Entry(frame, width=8)
    tone_maker_duration_entry=ttk.Entry(frame,width=8)
    speech_entry=ttk.Entry(frame,width=30)



    beeper_button=ttk.Button(frame,text='beeper')
    tone_maker_button=ttk.Button(frame,text='tone maker')
    speech_button=ttk.Button(frame,text='speak')

    frame_label.grid(row=0,column=1)
    beeper_label.grid(row=1,column=1)
    beeper_button.grid(row=2,column=0)
    beeper_entry.grid(row=2,column=1)
    tone_maker_frequency_label.grid(row=3,column=1)
    tone_maker_duration_label.grid(row=3,column=2)
    tone_maker_button.grid(row=4,column=0)
    tone_maker_frequency_entry.grid(row=4,column=1)
    tone_maker_duration_entry.grid(row=4,column=2)
    speech_label.grid(row=5,column=1)
    speech_button.grid(row=6,column=0)
    speech_entry.grid(row=6,column=1)


    beeper_button["command"]=lambda :handle_beep(beeper_entry,mqtt_sender)
    tone_maker_button["command"]=lambda :handle_tone(tone_maker_frequency_entry,tone_maker_duration_entry,mqtt_sender)
    speech_button["command"]=lambda :handle_speech(speech_entry,mqtt_sender)


    return frame
###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    print("forward",left_entry_box.get(),right_entry_box.get())
    left = int(left_entry_box.get())
    right = int(right_entry_box.get())
    mqtt_sender.send_message("go", [str(left), str(right)])




    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    print('backward',left_entry_box.get(),right_entry_box.get())
    left = -int(left_entry_box.get())
    right = -int(right_entry_box.get())
    mqtt_sender.send_message("go",[str(left), str(right)])

    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    print("left going",left_entry_box.get(),right_entry_box.get())
    left = -int(left_entry_box.get())
    right = int(right_entry_box.get())
    mqtt_sender.send_message("go",[str(left), str(right)])

    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    print("right going", left_entry_box.get(), right_entry_box.get())
    left = int(left_entry_box.get())
    right = -int(right_entry_box.get())
    mqtt_sender.send_message("go",[str(left), str(right)])
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """


def handle_stop(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message('stop',[] )
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
def handle_go_straight_for_seconds(time_entry_box, speed_entry_box, mqtt_sender):
    print('go straight for seconds')
    time=int(time_entry_box.get())
    speed=int(speed_entry_box.get())
    mqtt_sender.send_message('go_straight_for_seconds', [time,speed])

def handle_go_straight_for_distance(inch_entry_box,speed_entry_box,mqtt_sender):
    print('go straight for inches')
    inch=int(inch_entry_box.get())
    speed=int(speed_entry_box.get())
    mqtt_sender.send_message('go_straight_for_inches',[inch,speed])
def handle_go_straight_for_degrees(inch_entry_box,speed_entry_box,mqtt_sender):
    print('go straight for degrees')
    inch = int(inch_entry_box.get())
    speed = int(speed_entry_box.get())
    mqtt_sender.send_message('go_straight_for_degrees', [inch, speed])
###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("raise arm")

    mqtt_sender.send_message('raise_arm', [])


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower arm')
    mqtt_sender.send_message('lower_arm',[])



def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('caliberate arm')
    mqtt_sender.send_message('calibrate_arm',[])

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move arm to position')
    mqtt_sender.send_message('move_arm_to_position',[str(int(arm_position_entry.get()))])





###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    mqtt_sender.send_message('stop',[])

    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit',[])


def handle_exit(mqtt_sender):
    mqtt_sender.send_message('stop', [])
    mqtt_sender.send_message("exit")
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """



def handle_beep(beeper_entry,mqtt_sender):
    print('beeper')
    mqtt_sender.send_message('beeper',[int(beeper_entry.get())])

def handle_tone(frequency_entry,duration_entry,mqtt_sender):
    print('tone making')
    f=int(frequency_entry.get())
    d=int(duration_entry.get())
    mqtt_sender.send_message('tone_make',[f,d])

def handle_speech(phrase,mqtt_sender):
    print("speeking phrase")
    phrase=phrase.get()
    mqtt_sender.send_message('speech_make',[phrase])
def beep_while_go_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)
    return frame
def go_and_beep_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    forward_button = ttk.Button(frame, text="chase object")
    initial_label = ttk.Label(frame, text="initial speed(0 to 10)")
    rate_label = ttk.Label(frame, text="beep rate(0 to 10)")
    initial_speed_entry = ttk.Entry(frame, width=8)
    initial_speed_entry.insert(0, "0")
    set_speed_button = ttk.Button(frame, text="set speed")
    rate_entry = ttk.Entry(frame, width=8)
    rate_entry.insert(0, "0")
    set_rate_button = ttk.Button(frame, text="set rate")
    forward_button.grid(row=0, column=1)
    initial_label.grid(row=1, column=0)
    set_speed_button.grid(row = 1, column = 1)
    initial_speed_entry.grid(row=1, column=2)
    rate_entry.grid(row=2, column=2)
    rate_label.grid(row=2, column = 0)
    set_rate_button.grid(row=2, column = 1)
    forward_button["command"] = lambda: going_foward(mqtt_sender)
    return frame

def going_foward(mqtt_sender):
    print("go_foward_until")
    mqtt_sender.send_message('go_foward_until')