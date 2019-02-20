"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Yicheng Yang, Shixin Wu, Zhen Yang.
  Winter term, 2018-2019.
"""
import rosebot
import mqtt_remote_method_calls as com
class ResponderToGUIMessages(object):
    def __init__(self,robot):
        """

        :type robot: rosebot.Rosebot
        """
        self.robot = robot
        self.stop_program=False
        self.count=0
        self.mqtt_sender=None
        self.going=False
    def forward(self):
        print('forward')
        if not self.going:
            self.robot.drive_system.go(30, 30)
            self.going=True
        # if self.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 5:
        #     self.stop()

    def backward(self):
        print('backward')
        self.robot.drive_system.go(-30, -30)
    def left(self):
        print('left')
        self.robot.drive_system.go(-30, 30)
    def right(self):
        print('right')
        self.robot.drive_system.go(30, -30)
    def stop(self):
        print('receive stop')
        self.going=False
        self.robot.drive_system.stop()
    def pick_up(self):
        # mqtt_sender = com.MqttClient()
        # mqtt_sender.connect_to_ev3()
        color=self.robot.sensor_system.color_sensor.get_color_as_name()
        print(color)
        # self.speech_make("This is ",color)
        # if color=='Red':
            # print('red')
        self.robot.sound_system.speech_maker.speak("He has been terminated. I have seized another light saber of the color"+ color)
        # self.robot.sound_system.speech_maker.speak("I have seized another light saber of the color" + color)
        self.mqtt_sender.send_message("blast", [color,self.count])
        self.count = self.count+1
        # elif color=='orange':
        #     self.mqtt_sender.send_message("points", [2])
        # else:
        #     print('else')
        #     self.mqtt_sender.send_message('test',[])
    def go_less(self, inches, speed):
        print("receive go less")
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)
        self.robot.sound_system.speech_maker.speak("Hey you almost hit me!")

    def go_greater(self, inches, speed):
        print("receive go greater")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)
        self.robot.sound_system.speech_maker.speak("There we go")

    def speech_make(self,phrase):
        print("receive speech make")
        self.robot.sound_system.speech_maker.speak(phrase)
    def test(self):
        print('test10')
    def raise_arm(self):
        print('recieve raise arm')
        self.robot.arm_and_claw.raise_arm()
    def calibrate_arm(self):
        print('recieve calib arm')
        self.robot.arm_and_claw.calibrate_arm()
