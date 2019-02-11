"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Yicheng Yang, Shixin Wu, Zhen Yang.
  Winter term, 2018-2019.
"""

import ev3dev.ev3 as ev3
import time
import math


###############################################################################
#    RoseBot class.
#
# NOTE TO STUDENTS:
#   You should construct a RoseBot for the Snatch3r robot.
#   Do ** NOT ** construct any instances of any other classes in this module,
#   since a RoseBot constructs instances of all the sub-systems that provide
#   ALL of the functionality available to a Snatch3r robot.
#
#   Use those sub-systems (and their instance variables)
#   to make the RoseBot (and its associated Snatch3r robot) do things.
###############################################################################
class RoseBot(object):
    def __init__(self):
        self.sensor_system = SensorSystem()
        self.sound_system = SoundSystem()
        self.led_system = LEDSystem()
        self.drive_system = DriveSystem(self.sensor_system)
        self.arm_and_claw = ArmAndClaw(self.sensor_system.touch_sensor)
        self.beacon_system = BeaconSystem()
        self.display_system = DisplaySystem()

###############################################################################
#    DriveSystem
###############################################################################
class DriveSystem(object):

    """
    Controls the robot's motion via GO and STOP methods,
        along with various methods that GO/STOP under control of a sensor.
    """
    # -------------------------------------------------------------------------
    # NOTE:
    #   Throughout, when going straight:
    #     -- Positive speeds should make the robot move forward.
    #     -- Negative speeds should make the robot move backward.
    #   Throughout, when spinning:
    #     -- Positive speeds should make the robot spin in place clockwise
    #          (i.e., left motor goes at speed S, right motor at speed -S).
    #     -- Negative speeds should make the robot spin in place
    #          counter-clockwise
    #          (i.e., left motor goes at speed -S, right motor at speed S).
    # -------------------------------------------------------------------------

    def __init__(self, sensor_system):
        """
        Stores the given SensorSystem object.
        Constructs two Motors (for the left and right wheels).
          :type sensor_system:  SensorSystem
        """
        self.sensor_system = sensor_system
        self.left_motor = Motor('B')
        self.right_motor = Motor('C')

        self.wheel_circumference = 1.3 * math.pi

    def display_camera_data(self):
        """
        Displays on the GUI the Blob data of the Blob that the camera sees
        (if any).
        """

    def spin_clockwise_until_sees_object(self, speed, area):
        """
        Spins clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """

    def spin_counterclockwise_until_sees_object(self, speed, area):
        """
        Spins counter-clockwise at the given speed until the camera sees an object
        of the trained color whose area is at least the given area.
        Requires that the user train the camera on the color of the object.
        """

    # -------------------------------------------------------------------------
    # Methods for driving with no external sensor (just the built-in encoders).
    # -------------------------------------------------------------------------

    def go(self, left_wheel_speed, right_wheel_speed):
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(right_wheel_speed)
        """ Makes the left and right wheel motors spin at the given speeds. """

    def stop(self):
        self.right_motor.turn_off()
        self.left_motor.turn_off()

        """ Stops the left and right wheel motors. """

    def go_straight_for_seconds(self, seconds, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of seconds.
        """
        seconds=int(seconds)
        speed=int(speed)
        start = time.time()
        self.go(speed, speed)
        # Note: using   time.sleep   to control the time to run is better.
        # We do it with a WHILE loop here for pedagogical reasons.
        while True:
            if time.time() - start >= seconds:
                self.stop()
                break
    def go_straight_for_inches_using_time(self, inches, speed):
        """
        Makes the robot go straight at the given speed
        for the given number of inches, using the approximate
        conversion factor of 10.0 inches per second at 100 (full) speed.
        """
        inperdeg = self.wheel_circumference / 360  # turn circumference of the object to inches per degree
        deg = inches / inperdeg  # degree=inches/inches per degree
        self.left_motor.reset_position()
        self.go(speed, speed)  # object go in speed
        while True:  # if degree exceed the set, stop it
            if abs(self.left_motor.get_position()) >= deg:
                self.stop()
                break

    def go_straight_for_inches_using_encoder(self, inches, speed):
        """
        Makes the robot go straight (forward if speed > 0, else backward)
        at the given speed for the given number of inches,
        using the encoder (degrees traveled sensor) built into the motors.
        """
        inches_per_degree=self.wheel_circumference/360
        self.go(speed,speed)
        while True:
            if abs(self.left_motor.get_position()*inches_per_degree)>=inches:
                self.stop()
                break
        self.left_motor.reset_position()
        self.right_motor.reset_position()

    # -------------------------------------------------------------------------
    # Methods for driving that use the color sensor.
    # -------------------------------------------------------------------------

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is less than the given intensity.
        """

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        """
        Goes straight at the given speed until the intensity returned
        by the color_sensor is greater than the given intensity.
        """

    def go_straight_until_color_is(self, color, speed):
        """
        Goes straight at the given speed until the color returned
        by the color_sensor is equal to the given color.
        """

    def go_straight_until_color_is_not(self, color, speed):
        """
        Goes straight at the given speed until the color returned
        by the color_sensor is NOT equal to the given color.
        """

    # -------------------------------------------------------------------------
    # Methods for driving that use the infrared proximity sensor.
    # -------------------------------------------------------------------------
    def go_forward_until_distance_is_less_than(self, inches, speed):
        """
        Goes forward at the given speed until the robot is less than
        the given number of inches from the nearest object that it senses.
        """

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        """
        Goes straight at the given speed until the robot is greater than
        the given number of inches from the nearest object that it senses.
        Assumes that it senses an object when it starts.
        """


    def go_until_distance_is_within(self, delta, inches, speed):
        """
        Goes forward or backward, repeated as necessary, until the robot is
        within the given delta of the given inches from the nearest object
        that it senses.  Assumes that it senses an object when it starts.

        For example, if delta is 0.3 and inches is 7.1, then
        the robot should move until it is between 6.8 and 7.4 inches
        from the object.
        """

    # -------------------------------------------------------------------------
    # Methods for driving that use the infrared beacon sensor.
    # -------------------------------------------------------------------------

    def spin_clockwise_until_beacon_heading_is_nonnegative(self, speed):
        """
        Spins clockwise at the given speed until the heading to the Beacon
        is nonnegative.  Requires that the user turn on the Beacon.
        """

    def spin_counterclockwise_until_beacon_heading_is_nonpositive(self, speed):
        """
        Spins counter-clockwise at the given speed until the heading to the Beacon
        is nonnegative.  Requires that the user turn on the Beacon.
        """

    def go_straight_to_the_beacon(self, inches, speed):
        """
        Goes forward at the given speed until the robot is less than the
        given number of inches from the Beacon.
        Assumes that the Beacon is turned on and placed straight ahead.
        """

###############################################################################
#    ArmAndClaw
###############################################################################
class ArmAndClaw(object):
    """ Controls the robot's arm and claw (which operate together). """

    # -------------------------------------------------------------------------
    # NOTE:
    #   A POSITIVE speed for the ArmAndClaw's motor moves the arm UP.
    #   A NEGATIVE speed for the ArmAndClaw's motor moves the arm DOWN.
    #   It takes   14.2 revolutions    of the ArmAndClaw's motor
    #     to go from all the way UP to all the way DOWN.
    # -------------------------------------------------------------------------

    def __init__(self, touch_sensor):
        """
        Stores the given touch sensor for stopping the Arm in its UP position.
        Constructs the Arm's motor.
          :type  touch_sensor:  TouchSensor
        """
        self.touch_sensor = touch_sensor
        self.motor = Motor('A', motor_type='medium')

    def raise_arm(self):
        self.motor.turn_on(100)
        while True:
            print(self.motor.get_position())
            if self.touch_sensor.is_pressed():
                self.motor.turn_off()
                break

        """ Raises the Arm until its touch sensor is pressed. """

    def calibrate_arm(self):
        self.raise_arm()
        self.motor.reset_position()
        self.motor.turn_on(-100)
        print('calibrating')
        while True:
            print(self.motor.get_position())
            if abs(self.motor.get_position())>= 14.2*360:
                self.motor.turn_off()
                self.motor.reset_position()
                break

        """
        Calibrates
         its Arm, that is:
          1. Raises its Arm until it is all the way UP
               (i.e., its touch sensor is pressed)
          2. Lowers its Arm until it is all the way down
               (i.e., 14.2 motor revolutions),
          3. Resets the motor's position to 0.
        """

    def move_arm_to_position(self, desired_arm_position):
        self.motor.turn_on(100)
        while True:
            if self.motor.get_position() >= desired_arm_position:
                self.motor.turn_off()
                break

        """
        Move its Arm to the given position, where 0 means all the way DOWN.
        The robot must have previously calibrated its Arm.
        """

    def lower_arm(self):
        self.motor.turn_on(-100)
        while True:
            if self.motor.get_position()<= 0:
                self.motor.turn_off()
                break

        """
        Lowers the Arm until it is all the way down, i.e., position 0.
        The robot must have previously calibrated its Arm.
        """



