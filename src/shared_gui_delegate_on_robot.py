"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Yicheng Yang, Shixin Wu, Zhen Yang.
  Winter term, 2018-2019.
"""
import rosebot
class ResponderToGUIMessages(object):
    def __init__(self,robot):
        """

        :type robot: rosebot.Rosebot
        """
        self.robot = robot
    def go(self,left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left, right)
    def stop(self):
        self.robot.drive_system.stop()
    def raise_arm(self):
        print('recieve raise arm')
        self.robot.arm_and_claw.raise_arm()
    def lower_arm(self):
        print('recieve lower arm')
        self.robot.arm_and_claw.lower_arm()
    def calibrate_arm(self):
        print('recieve calib arm')
        self.robot.arm_and_claw.calibrate_arm()
    def move_arm_to_position(self,pos):
        self.robot.arm_and_claw.move_arm_to_position(int(pos))
    def go_straight_for_seconds(self,seconds,speed):
        print('recieve go straight for seconds')
        self.robot.drive_system.go_straight_for_seconds(seconds, speed)
    def go_straight_for_inches(self,inch,speed):
        print('recieve go straight for inches')
        self.robot.drive_system.go_straight_for_inches_using_time(inch,speed)
    def go_straight_for_degrees(self,inch,speed):
        print('recieve go straight for inches')
        self.robot.drive_system.go_straight_for_inches_using_encoder(inch,speed)
