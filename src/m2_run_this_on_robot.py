"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Yicheng Yang..
  Winter term, 2018-2019.
"""

import M2_rosebot
import mqtt_remote_method_calls as com
import time
import m2_gui_delegate

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_run()
    # go_along_black()
    # go_straight_for_seconds(99999,50)


def real_run():
    robot = M2_rosebot.RoseBot()
    delegate = m2_gui_delegate.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()
    delegate.mqtt_sender=mqtt_receiver

    while True:
        if delegate.stop_program:
            break
        time.sleep(0.01)


# def main():
#     robot = rosebot.RoseBot()
#     rc = RemoteControlEtc(robot)
#     client = com.MqttClient(rc)
#     client.connect_to_pc()
#     rc.client = client
#
#     while True:
#         if robot.color_sensor.get_color() == 6:
#             time.sleep(1.5)
#             robot.drive_system.turn_degrees(-95)
#         if robot.proximity_sensor.get_distance_to_nearest_object() <= 10:
#             ev3.Sound.speak('mission complete').wait()
#             robot.drive_system.stop_moving()
#         time.sleep(0.01)  # For the delegate to do its work
    # real_run()
    # run_test_arm()
    # run_caliberate_arm()
    # run_mov3_arm_to_position(5000)
    # lower_arm()
    # go(100, 50)
    # stop()
    # go_straight_for_seconds(10,70)
    # go_straight_for_inches_using_time(30, 50)
# class RemoteControlEtc(object):
# def __init__(self, robot):
#     """
#
#     Stores the robot.
#       :type robot: rb.Snatch3rRobot
#     """
#     self.robot = robot
#     self.client = None
#     pass
# def go():

# def run_test_arm():
#     robot=M2_rosebot.RoseBot()
#     robot.arm_and_claw.raise_arm()
#
# def run_caliberate_arm():
#     robot=M2_rosebot.RoseBot()
#     print('running')
#     robot.arm_and_claw.calibrate_arm()
#
# def run_mov3_arm_to_position(pos):
#     robot=M2_rosebot.RoseBot()
#     robot.arm_and_claw.move_arm_to_position(pos)
#
# def lower_arm():
#     robot =M2_rosebot.RoseBot()
#     robot.arm_and_claw.lower_arm()
# def go(left, right):
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go(left , right)
# def stop():
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.stop()
# def go_straight_for_seconds(second, speed):
#     print('running')
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go_straight_for_seconds(second, speed)
# def go_straight_for_inches_using_time(inch, speed):
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go_straight_for_inches_using_time(inch, speed)
# def go_straight_for_inches_using_encoder(inch, speed):
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go_straight_for_inches_using_encoder(inch, speed)
# def beeper(time):
#     robot = M2_rosebot.RoseBot()
#     robot.sound_system.beeper.beep(time)
# def tone_make(frequency, duration):
#     robot = M2_rosebot.RoseBot()
#     robot.sound_system.tone_maker.play_tone(frequency,duration).wait()
#
#
# def speak(str):
#     robot = M2_rosebot.RoseBot()
#     robot.sound_system.speech_maker.speak(str)
#
#
# def go_and_increase_frequency(speed,frequency_step):
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go_and_increase_frequency(speed,frequency_step)
# def go_along_black():
#     robot = M2_rosebot.RoseBot()
#     robot.drive_system.go_along_black_line()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()