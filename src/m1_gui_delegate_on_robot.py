"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Yicheng Yang, Shixin Wu, Zhen Yang.
  Winter term, 2018-2019.
"""
import m1_rosebot
class ResponderToGUIMessages(object):
    def __init__(self,robot):
        """

        :type robot: rosebot.Rosebot
        """
        self.robot = robot
        self.stop_program=False
    def go(self,left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left, right)
    def stop(self):
        print('receive stop')
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
    def beeper(self,time):
        print('receive beeper')
        self.robot.sound_system.beeper.beep(time)
    def tone_make(self,frequency,duration):
        print(('receive tone make'))
        self.robot.sound_system.tone_maker.play_tone(frequency,duration)
    def speech_make(self,phrase):
        print("receive speech make")
        self.robot.sound_system.speech_maker.speak(phrase)
    def quit(self):
        self.stop_program=True
    def go_and_increase_frequency(self,speed,frequency_step):
        print("receive go and increase frequency")
        self.robot.drive_system.go_and_increase_frequency(speed,frequency_step)

    def go_foward_until(self,speed, rate):
        print("let this robot start to find object")
        self.robot.drive_system.go_and_increase_beep(int(speed),int(rate))

    def go_less(self, inches, speed):
        print("receive go less")
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

    def go_greater(self, inches, speed):
        print("receive go greater")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def go_within(self, delta, inches, speed):
        print("receive go within")
        self.robot.drive_system.go_until_distance_is_within(delta, inches, speed)

    def go_and_clean(self, clock, speed):
        print("receive clean commend")
        self.robot.drive_system.go_and_clean(int(clock), int(speed))

    def go_and_changing_led(self, speed, frequency_step):
        print("receive go_and_changing_led")
        self.robot.drive_system.go_and_changing_led(int(speed), int(frequency_step))
    def robot_dog_chase(self,clock, speed):
        print("robot dog chase obj")
        self.robot.drive_system.robot_dog_chase(int(clock), int(speed))