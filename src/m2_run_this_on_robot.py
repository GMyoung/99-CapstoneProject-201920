"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Shixin Wu.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # run_caliberate_arm()
    run_mov3_arm_to_position(5000)

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

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()