"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Yicheng Yang..
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    run_caliberate_arm()
    real_run()
    # run_test_arm()
    # run_caliberate_arm()
    # run_mov3_arm_to_position(5000)
    # lower_arm()
    # go(100, 50)
    # stop()
    # go_straight_for_seconds(10,70)
    # go_straight_for_inches_using_time(30, 50)
    # tone_make(100, 200)
    # beep(10)
    speak("say hello to my little friend")

def real_run():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        if delegate.stop_program:
            break
        time.sleep(0.01)

def run_test_arm():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_caliberate_arm():
    robot=rosebot.RoseBot()
    print('running')
    robot.arm_and_claw.calibrate_arm()

def run_mov3_arm_to_position(pos):
    robot=rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(pos)

def lower_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()
def go(left, right):
    robot = rosebot.RoseBot()
    robot.drive_system.go(left , right)
def stop():
    robot = rosebot.RoseBot()
    robot.drive_system.stop()
def go_straight_for_seconds(second, speed):
    print('running')
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(second, speed)
def go_straight_for_inches_using_time(inch, speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(inch, speed)
def go_straight_for_inches_using_encoder(inch, speed):
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(inch, speed)
def beeper(time):
    robot = rosebot.RoseBot()
    robot.sound_system.beeper.beep(time)
def tone_make(frequency, duration):
    robot = rosebot.RoseBot()
    robot.sound_system.tone_maker.play_tone(frequency,duration).wait()


def speak(str):
    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker.speak(str)



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
